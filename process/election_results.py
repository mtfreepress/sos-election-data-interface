#!/usr/bin/env python3
"""Download and normalize Montana SOS election exports. Run from any directory."""

import argparse
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
from http.cookiejar import CookieJar
import json
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, Request, build_opener

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://electionresults.mt.gov"
COUNTY_NAMES = (
    "BEAVERHEAD", "BIG HORN", "BLAINE", "BROADWATER", "CARBON", "CARTER",
    "CASCADE", "CHOUTEAU", "CUSTER", "DANIELS", "DAWSON", "DEER LODGE",
    "FALLON", "FERGUS", "FLATHEAD", "GALLATIN", "GARFIELD", "GLACIER",
    "GOLDEN VALLEY", "GRANITE", "HILL", "JEFFERSON", "JUDITH BASIN", "LAKE",
    "LEWIS AND CLARK", "LIBERTY", "LINCOLN", "MADISON", "MCCONE", "MEAGHER",
    "MINERAL", "MISSOULA", "MUSSELSHELL", "PARK", "PETROLEUM", "PHILLIPS",
    "PONDERA", "POWDER RIVER", "POWELL", "PRAIRIE", "RAVALLI", "RICHLAND",
    "ROOSEVELT", "ROSEBUD", "SANDERS", "SHERIDAN", "SILVER BOW", "STILLWATER",
    "SWEET GRASS", "TETON", "TOOLE", "TREASURE", "VALLEY", "WHEATLAND",
    "WIBAUX", "YELLOWSTONE",
)
COUNTIES = {f"{i:02}": name for i, name in enumerate(COUNTY_NAMES, 1)}
NORMAL_COLUMNS = ["election", "type", "race", "race_name", "key", "county",
                  "precinct", "party", "candidate", "votes"]


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def identify_race(title, sheet_name):
    """Return stable key, display name, and category; preserve unknown contests."""
    title = re.sub(r"\s+", " ", title).strip()
    upper = title.upper()
    for office, prefix in [("SENATOR", "SD"), ("REPRESENTATIVE", "HD")]:
        match = re.fullmatch(rf"STATE {office} DISTRICT (\d+)", upper)
        if match:
            district = f"{prefix}-{int(match[1])}"
            return district, district, "legislative"
    if upper == "UNITED STATES SENATOR":
        return "us-senate", "U.S. Senate", "statewide"
    match = re.search(r"UNITED STATES REPRESENTATIVE (\d+)(?:ST|ND|RD|TH) CONGRESSIONAL", upper)
    if match:
        number = int(match[1])
        key = {1: "us-house-west", 2: "us-house-east"}.get(number, f"us-house-{number}")
        return key, f"U.S. House {number}", "statewide"
    offices = {
        "PRESIDENT & VICE PRESIDENT": ("president", "President"),
        "GOVERNOR & LT. GOVERNOR": ("governor", "Governor"),
        "SECRETARY OF STATE": ("secretary-of-state", "Secretary of State"),
        "ATTORNEY GENERAL": ("attorney-general", "Attorney General"),
        "STATE AUDITOR": ("state-auditor", "State Auditor"),
        "STATE SUPERINTENDENT OF PUBLIC INSTRUCTION": ("superintendent", "Superintendent of Public Instruction"),
        "CLERK OF THE SUPREME COURT": ("supreme-court-clerk", "Clerk of the Supreme Court"),
        "SUPREME COURT CHIEF JUSTICE": ("supreme-court-chief-justice", "Supreme Court Chief Justice"),
    }
    if upper in offices:
        key, name = offices[upper]
        return key, name, "statewide"
    match = re.search(r"PUBLIC SERVICE COMMISSIONER,? DISTRICT (\d+)", upper)
    if match:
        return f"psc-{int(match[1])}", f"PSC {int(match[1])}", "statewide"
    match = re.fullmatch(r"SUPREME COURT JUSTICE #\s*(\d+)", upper)
    if match:
        return f"supreme-court-{int(match[1])}", f"Supreme Court Justice #{int(match[1])}", "judicial"
    match = re.match(r"(CI|I|LR)\s*-\s*(\d+)\b", upper)
    if match:
        key = f"{match[1].lower()}-{int(match[2])}"
        return key, key.upper(), "ballot"
    if "DISTRICT COURT JUDGE" in upper:
        return slug(title), title, "judicial"
    # SOS exports can include local contests even in the statewide workbook.
    # Keep their source ID so unrelated local contests do not share a key.
    source_id = re.match(r"\d+", sheet_name)
    key = f"sos-{source_id[0]}-{slug(title)}" if source_id else slug(title)
    return key, title, "unmapped"


def election_metadata(frame, year, election):
    text = " ".join(str(v) for v in frame.iloc[:6, 0] if pd.notna(v))
    if not re.search(rf"\b{year}\b.*\b{election}\b.*Election", text, re.I):
        raise ValueError(f"Expected {year} {election} election; found {text[:180]!r}")
    reporting = re.search(r"Precincts (\d+) of (\d+) Reporting", text)
    return {
        "source_header": text,
        "status": ("unofficial" if "unofficial" in text.lower()
                   else "official" if "official" in text.lower() else "unspecified"),
        "precincts_reporting": int(reporting[1]) if reporting else None,
        "precincts_total": int(reporting[2]) if reporting else None,
    }


def parse_workbook(path, year, election, county=None):
    """Parse every sheet, validate candidate totals, and retain source metadata."""
    rows, totals, inventory = [], [], []
    with pd.ExcelFile(path) as workbook:
        for sheet_name in workbook.sheet_names:
            frame = workbook.parse(sheet_name, header=None)
            if frame.empty or frame.shape[1] < 3:
                raise ValueError(f"{path.name}/{sheet_name}: missing result table")
            meta = election_metadata(frame, year, election)
            label = "Precinct" if county else "County"
            matches = frame.index[frame.iloc[:, 1].astype(str).str.strip().eq(label)]
            if len(matches) != 1:
                raise ValueError(f"{path.name}/{sheet_name}: expected one {label} header")
            header = matches[0]
            if pd.isna(frame.iloc[header, 0]):
                raise ValueError(f"{path.name}/{sheet_name}: missing full contest title")
            title = str(frame.iloc[header, 0]).strip()
            key, name, kind = identify_race(title, sheet_name)
            inventory.append({"file": path.name, "sheet": sheet_name, "title": title,
                              "race": key, "race_name": name, "type": kind,
                              "county": county, **meta})
            data = frame.iloc[header + 1:].dropna(how="all")
            labels = data.iloc[:, 1].astype(str).str.strip()
            total_mask = labels.str.upper().eq("TOTALS")
            if total_mask.sum() != 1:
                raise ValueError(f"{path.name}/{sheet_name}: expected one TOTALS row")
            if data.loc[~total_mask].iloc[:, 1].isna().any():
                raise ValueError(f"{path.name}/{sheet_name}: missing {label} label")
            if labels[~total_mask].duplicated().any():
                raise ValueError(f"{path.name}/{sheet_name}: duplicate {label} rows")
            for col in range(2, frame.shape[1]):
                raw = frame.iloc[header, col]
                if pd.isna(raw):
                    if data.iloc[:, col].notna().any():
                        raise ValueError(f"{sheet_name}: values in unlabeled candidate column")
                    continue
                parts = str(raw).split("\n", 1)
                candidate = parts[0].strip()
                party = parts[1].strip() if len(parts) == 2 else ""
                votes = pd.to_numeric(data.iloc[:, col], errors="raise")
                if votes.isna().any() or (votes < 0).any() or (votes % 1 != 0).any():
                    raise ValueError(f"{sheet_name}/{candidate}: missing, negative, or noninteger votes")
                expected = int(votes[total_mask].iloc[0])
                actual = int(votes[~total_mask].sum())
                if actual != expected:
                    raise ValueError(f"{sheet_name}/{candidate}: rows sum to {actual}, TOTALS is {expected}")
                base = {"election": f"{year}-{'gen' if election == 'general' else 'primary'}",
                        "type": kind, "race": key, "race_name": name,
                        "party": party, "candidate": candidate}
                totals.append({**base, "county": county, "votes": expected})
                for idx in data.index[~total_mask]:
                    place = str(data.loc[idx].iloc[1]).strip()
                    county_name = county or place.upper().replace("&", "AND")
                    rows.append({**base, "county": county_name,
                                 "precinct": place if county else "",
                                 "key": f"{county_name}-{place}" if county else county_name,
                                 "votes": int(votes.loc[idx])})
    return rows, totals, inventory


class ExportForm(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = {}
        self.precinct_exports = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "input" and attrs.get("type") == "hidden" and "name" in attrs:
            self.hidden[attrs["name"]] = attrs.get("value", "")
        if tag == "input" and attrs.get("value") == "Precinct Level" and attrs.get("raceid"):
            self.precinct_exports.append(attrs)


def export_page(url):
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    with opener.open(url, timeout=90) as response:
        html = response.read().decode("utf-8")
    form = ExportForm()
    form.feed(html)
    return opener, html, form


def post_export(opener, url, form, target):
    form.hidden.update(__EVENTTARGET=target, __EVENTARGUMENT="")
    request = Request(url, data=urlencode(form.hidden).encode(), headers={"Referer": url})
    with opener.open(request, timeout=120) as response:
        content = response.read()
    if not content.startswith(b"PK"):
        raise ValueError("SOS returned an error page instead of an XLSX workbook")
    return content


def download_export(url, target, destination, year, election, county=None):
    """ASP.NET requires hidden form fields and may require session cookies."""
    opener, html, form = export_page(url)
    if "__VIEWSTATE" not in form.hidden or target not in unescape(html):
        raise ValueError("SOS page is missing the expected export control")
    content = post_export(opener, url, form, target)
    temporary = destination.with_suffix(".part.xlsx")
    try:
        temporary.write_bytes(content)
        parse_workbook(temporary, year, election, county)
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


def canonical_county(value):
    return re.sub(r"\s+", " ", value.upper().replace("&", "AND")).strip()


def race_county_sheet(opener, url, form, control, cache, number, year, election):
    race_id, party = control["raceid"], control.get("party", "")
    if not race_id.isdigit():
        raise ValueError("Invalid SOS race ID")
    cache_key = race_id + (f"-{slug(party)}" if party else "")
    raw_path = cache / f"{cache_key}.xlsx"
    meta_path = raw_path.with_suffix(".json")
    if not raw_path.exists():
        print(f"  Per-race precinct export {cache_key}…", flush=True)
        content = post_export(opener, url, form, control["name"])
        temporary = raw_path.with_suffix(".part.xlsx")
        try:
            temporary.write_bytes(content)
            with pd.ExcelFile(temporary) as workbook:
                if not workbook.sheet_names:
                    raise ValueError("Empty precinct export")
                election_metadata(workbook.parse(0, header=None), year, election)
            temporary.replace(raw_path)
        finally:
            temporary.unlink(missing_ok=True)
        meta_path.write_text(json.dumps({"url": url, "target": control["name"],
                                         "race_id": race_id, "party": party,
                                         "downloaded_at": datetime.now(timezone.utc).isoformat()}, indent=2) + "\n")
    with pd.ExcelFile(raw_path) as workbook:
        matches = [s for s in workbook.sheet_names if canonical_county(s) == COUNTIES[number]]
        if len(matches) != 1:
            raise ValueError(f"Precinct export {race_id} does not contain {COUNTIES[number]}")
        frame = workbook.parse(matches[0], header=None)
    election_metadata(frame, year, election)
    headers = frame.index[frame.iloc[:, 1].astype(str).str.strip().eq("Precinct")]
    if len(headers) != 1:
        raise ValueError(f"Precinct export {race_id} has no unique Precinct header")
    title = str(frame.iloc[headers[0], 0])
    sheet_name = re.sub(r"[\\/*?:\[\]]", " ", race_id[-5:] + party + title)[:31]
    return sheet_name, frame, {"path": str(raw_path.relative_to(cache.parent)),
                                **json.loads(meta_path.read_text())}


def api_table(precincts, county_totals, race_id, number, year, election):
    """Build an export-shaped table, using separately fetched county TOTALS."""
    if not precincts or not county_totals:
        raise ValueError("Empty SOS API results")
    candidates, expected, places, cells = {}, {}, {}, {}
    title = precincts[0]["RaceName"]
    for is_total, records in [(True, county_totals), (False, precincts)]:
        for row in records:
            if (str(row["RaceID"]) != race_id or f"{int(row['CountyID']):02}" != number
                    or canonical_county(row["CountyName"]) != COUNTIES[number]
                    or row["RaceName"] != title):
                raise ValueError("SOS API returned a different race or county")
            candidate_id = str(row["CandidateID"])
            choice = str(row["calcCandidate"]).strip()
            party = str(row.get("PartyName") or "").strip()
            label = choice + (f"\n{party}" if party else "")
            if candidate_id in candidates and candidates[candidate_id] != label:
                raise ValueError("Inconsistent SOS API candidate names")
            candidates[candidate_id] = label
            votes = row["calcCandidateVotes"]
            if isinstance(votes, bool) or votes is None or int(votes) != votes or votes < 0:
                raise ValueError("Invalid SOS API vote count")
            if is_total:
                if candidate_id in expected:
                    raise ValueError("Duplicate SOS API county total")
                expected[candidate_id] = int(votes)
            else:
                precinct_id = str(row["StatePrecinctID"])
                precinct_name = str(row["PrecinctName"]).strip()
                if precinct_id in places and places[precinct_id] != precinct_name:
                    raise ValueError("Inconsistent SOS API precinct names")
                places[precinct_id] = precinct_name
                key = precinct_id, candidate_id
                if key in cells:
                    raise ValueError("Duplicate SOS API precinct/candidate result")
                cells[key] = int(votes)
    if set(candidates) != set(expected):
        raise ValueError("SOS API county and precinct candidates differ")
    if len(cells) != len(places) * len(candidates):
        raise ValueError("SOS API omitted precinct/candidate records")
    # CTY reports the whole county's precinct count even for a city-only issue;
    # PREC reports the precinct count for this specific contest.
    declared = {int(r["TotalPrecincts"]) for r in precincts if r.get("TotalPrecincts") is not None}
    if declared and declared != {len(places)}:
        raise ValueError("SOS API precinct count does not match its declared coverage")
    for candidate_id, total in expected.items():
        if sum(v for (p, c), v in cells.items() if c == candidate_id) != total:
            raise ValueError("SOS API precinct sums do not match its county totals")
    rows = [[f"{year} Unofficial {election.title()} Election Results"], ["State of Montana"],
            ["Source: SOS precinct and county results API"],
            [f"Downloaded at {datetime.now(timezone.utc).isoformat()}"], [], [],
            [title, "Precinct", *candidates.values()]]
    rows.extend([None, name, *[cells[(p, c)] for c in candidates]] for p, name in places.items())
    rows.append([None, "TOTALS", *[expected[c] for c in candidates]])
    return pd.DataFrame(rows)


def api_county_sheet(opener, html, form, control, cache, number, year, election):
    """Use the JSON service called by the site's BuildPrecincts.js as a fallback."""
    if (form.hidden.get("ctl00$hidElectionType", "").lower() != election
            or not form.hidden.get("ctl00$hidElectionDate", "").endswith(f"/{year}")):
        raise ValueError("SOS page election metadata does not match the requested election")
    race_id = control["raceid"]
    query = re.search(rf"BuildPrecincts\('([^']+)',\s*'{race_id}',\s*'([^']+)',\s*'{number}',\s*'([^']*)'\)", html)
    service = re.search(r"var ServiceRoot\s*=\s*'(https://[^']+)'", html)
    if not query or not service:
        raise ValueError("Cannot discover the SOS precinct API request")
    party = query[3].strip() or "0"
    cache_key = race_id + "-" + number + "-" + slug(party)
    payloads, sources = [], []
    for category in ["PREC", "CTY"]:
        url = service[1].rstrip("/") + "/ResultsAjax.svc/GetMapData?" + urlencode({
            "type": query[1], "category": category, "raceID": race_id,
            "osn": query[2], "county": number, "party": party})
        path = cache / f"{cache_key}-{category.lower()}.json"
        meta_path = path.with_suffix(".source.json")
        if not path.exists():
            with opener.open(url, timeout=90) as response:
                raw = response.read()
            data = json.loads(raw)
            if not isinstance(data.get("d"), list) or not data["d"]:
                raise ValueError("SOS API returned no results")
            path.write_bytes(raw)
            meta_path.write_text(json.dumps({"url": url, "downloaded_at": datetime.now(timezone.utc).isoformat()}, indent=2) + "\n")
        payloads.append(json.loads(path.read_bytes())["d"])
        sources.append({"path": str(path.relative_to(cache.parent)), **json.loads(meta_path.read_text())})
    frame = api_table(*payloads, race_id, number, year, election)
    title = str(frame.iloc[6, 0])
    sheet_name = re.sub(r"[\\/*?:\[\]]", " ", race_id[-5:] + control.get("party", "") + title)[:31]
    print(f"  Recovered race {race_id} via SOS precinct API.", flush=True)
    return sheet_name, frame, {"source_type": "api", "race_id": race_id, "sources": sources}


def assemble_county(url, destination, number, year, election):
    """Fallback for broken bulk exports: retain per-race originals and assemble."""
    opener, html, form = export_page(url)
    if not form.precinct_exports:
        raise ValueError("No per-race precinct export controls found on county page")
    if re.search(r"(?:Page\$|Page%24)", html, re.I):
        raise ValueError("County page is paginated; refusing an incomplete race inventory")
    cache = destination.parent / "race-exports"
    cache.mkdir(exist_ok=True)
    sheets, sources = {}, []
    for control in form.precinct_exports:
        try:
            try:
                api_cache = cache / (control["raceid"] + "-" + number + "-"
                                     + slug(control.get("party", "").strip() or "0") + "-prec.json")
                if api_cache.exists():
                    sheet_name, frame, source = api_county_sheet(opener, html, form, control, cache, number, year, election)
                else:
                    sheet_name, frame, source = race_county_sheet(opener, url, form, control, cache, number, year, election)
            except Exception as export_error:
                try:
                    sheet_name, frame, source = api_county_sheet(opener, html, form, control, cache, number, year, election)
                except Exception as api_error:
                    raise ValueError(f"Excel export failed ({export_error}); API fallback failed ({api_error})") from api_error
            if sheet_name in sheets:
                raise ValueError(f"Duplicate per-race export: {sheet_name}")
            sheets[sheet_name] = frame
            sources.append(source)
        except Exception as exc:
            print(f"  Missing race {control['raceid']}: {exc}", file=sys.stderr)
            sources.append({"race_id": control["raceid"], "party": control.get("party", ""),
                            "url": url, "target": control["name"], "error": str(exc)})
    if not sheets:
        raise ValueError("Every per-race precinct export failed")
    temporary = destination.with_suffix(".part.xlsx")
    try:
        with pd.ExcelWriter(temporary, engine="openpyxl") as writer:
            for sheet_name, frame in sheets.items():
                frame.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
        parse_workbook(temporary, year, election, COUNTIES[number])
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)
    return sources


def county_ids(value):
    if value.lower() == "all":
        return list(COUNTIES)
    if value.lower() == "none":
        return []
    try:
        ids = list(dict.fromkeys(f"{int(v):02}" for v in value.split(",")))
        if not ids or any(v not in COUNTIES for v in ids):
            raise ValueError()
        return ids
    except ValueError:
        raise argparse.ArgumentTypeError("Use all, none, or comma-separated county IDs from 1 to 56")


def fetch(args):
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    snapshot = args.destination or ROOT / "sos-data" / str(args.year) / args.election / stamp
    manifest = {"year": args.year, "election": args.election,
                "downloaded_at": datetime.now(timezone.utc).isoformat(),
                "requested_counties": args.counties, "files": [], "failures": [],
                "write_ins": "Not reported by the live SOS site; obtain separately."}
    if args.resume:
        if not args.destination:
            raise ValueError("--resume requires --destination")
        manifest = json.loads((snapshot / "manifest.json").read_text())
        if (manifest["year"], manifest["election"], manifest["requested_counties"]) != (args.year, args.election, args.counties):
            raise ValueError("Resume must use the snapshot's original year, election, and county selection")
        manifest["failures"] = []
    else:
        snapshot.mkdir(parents=True, exist_ok=False)
    completed = {(f["kind"], f.get("county_id")) for f in manifest["files"]
                 if not f.get("incomplete_races") and (snapshot / f["path"]).exists()}
    jobs = [
        ("statewide", None, f"{BASE_URL}/ResultsExport.aspx", "ctl00$MainContent$Statewide"),
        ("legislative", None, f"{BASE_URL}/ResultsExport.aspx", "ctl00$MainContent$Legislative"),
    ]
    jobs.extend(("county", number,
                 f"{BASE_URL}/ResultsSW.aspx?type=CTYALL&cty={number}&map=CTY",
                 "ctl00$NavLinks$lnkbtnSWExport") for number in args.counties)
    try:
        for kind, number, url, target in jobs:
            if (kind, number) in completed:
                continue
            filename = f"county-{number}-{slug(COUNTIES[number])}.xlsx" if number else f"{kind}.xlsx"
            print(f"Downloading {filename}…", flush=True)
            try:
                sources = []
                try:
                    download_export(url, target, snapshot / filename, args.year, args.election,
                                    COUNTIES[number] if number else None)
                except Exception as exc:
                    if not number:
                        raise
                    print(f"  Bulk export failed ({exc}); trying per-race exports.", flush=True)
                    sources = assemble_county(url, snapshot / filename, number, args.year, args.election)
                errors = [s for s in sources if "error" in s]
                manifest["files"] = [f for f in manifest["files"] if (f["kind"], f.get("county_id")) != (kind, number)]
                manifest["files"].append({"kind": kind, "county_id": number,
                                          "path": filename, "url": url,
                                          "assembled_from": sources,
                                          "incomplete_races": errors,
                                          "downloaded_at": datetime.now(timezone.utc).isoformat()})
                manifest["failures"].extend({"kind": kind, "county_id": number, **error} for error in errors)
            except Exception as exc:
                manifest["failures"].append({"kind": kind, "county_id": number, "error": str(exc)})
                print(f"  FAILED: {exc}", file=sys.stderr)
            (snapshot / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    finally:
        (snapshot / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        print(f"Snapshot: {snapshot}")
    return 1 if manifest["failures"] else 0


def import_files(args):
    """Adopt manually downloaded or certified exports without renaming by order."""
    entries = [("statewide", None, args.statewide), ("legislative", None, args.legislative)]
    for value in args.county:
        number, sep, path = value.partition("=")
        if not sep:
            raise ValueError("County imports must be ID=PATH")
        ids = county_ids(number)
        if len(ids) != 1:
            raise ValueError("Each county import needs exactly one county ID")
        entries.append(("county", ids[0], Path(path)))
    keys = [(kind, number) for kind, number, _ in entries]
    if len(set(keys)) != len(keys):
        raise ValueError("Duplicate county imports")
    for kind, number, path in entries:
        parse_workbook(path, args.year, args.election, COUNTIES[number] if number else None)
    args.destination.mkdir(parents=True, exist_ok=False)
    manifest = {"year": args.year, "election": args.election,
                "imported_at": datetime.now(timezone.utc).isoformat(),
                "requested_counties": [n for k, n, _ in entries if k == "county"],
                "files": [], "failures": [],
                "write_ins": "Verify write-in coverage against the original imported source."}
    for kind, number, path in entries:
        filename = f"county-{number}-{slug(COUNTIES[number])}.xlsx" if number else f"{kind}.xlsx"
        shutil.copyfile(path, args.destination / filename)
        manifest["files"].append({"kind": kind, "county_id": number, "path": filename,
                                  "imported_from": str(path.resolve())})
    (args.destination / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Snapshot: {args.destination}")
    return 0


def summarize(frame, group, election):
    records = []
    for key, candidates in frame.groupby(group, sort=True):
        total = int(candidates.votes.sum())
        gop = candidates[candidates.party == "Republican"]
        dem = candidates[candidates.party == "Democrat"]
        records.append({group: key, f"total_{election}_votes": total,
                        f"fraction_{election}_votes_to_gop": int(gop.votes.sum()) / total if total else None,
                        "gop_votes": int(gop.votes.sum()), "gop_candidate": ", ".join(gop.candidate),
                        "dem_votes": int(dem.votes.sum()), "dem_candidate": ", ".join(dem.candidate)})
    columns = [group, f"total_{election}_votes", f"fraction_{election}_votes_to_gop",
               "gop_votes", "gop_candidate", "dem_votes", "dem_candidate"]
    summary = pd.DataFrame(records, columns=columns)
    if election == "primary":
        summary.rename(columns={"gop_votes": "gop_primary_votes", "dem_votes": "dem_primary_votes",
                                "gop_candidate": "gop_candidates", "dem_candidate": "dem_candidates"}, inplace=True)
    return summary


def district_context(summary, year):
    # These inputs describe the 2023–2034 map; never apply them to a later map.
    if not 2024 <= year <= 2032:
        return summary
    context = []
    for chamber, prefix in [("house", "HD"), ("senate", "SD")]:
        path = ROOT / "inputs" / "daves-redistricting" / f"mt-{chamber}-district-statistics.csv"
        if not path.exists():
            return summary
        data = pd.read_csv(path, index_col=False)
        data = data[data.ID.astype(str).str.fullmatch(r"\d+")].copy()
        data["district"] = prefix + "-" + data.ID.astype(str)
        data["daves_score_r_plus"] = (100 * (data.Rep - data.Dem)).round()
        context.append(data[["district", "daves_score_r_plus", "Native"]])
    return summary.merge(pd.concat(context), on="district", how="left", validate="one_to_one")


def parse_snapshot(args):
    snapshot = args.snapshot.resolve()
    manifest = json.loads((snapshot / "manifest.json").read_text())
    year, election = manifest["year"], manifest["election"]
    files = manifest["files"]
    expected = {("statewide", None), ("legislative", None)}
    expected.update(("county", c) for c in manifest.get("requested_counties", []))
    actual = [(item["kind"], item.get("county_id")) for item in files]
    if len(actual) != len(set(actual)):
        raise ValueError("Manifest contains duplicate exports")
    missing = sorted(str(item) for item in expected - set(actual))
    race_gaps = [{"county_id": f.get("county_id"), **gap}
                 for f in files for gap in f.get("incomplete_races", [])]
    if (missing or race_gaps or manifest.get("failures")) and not args.allow_partial:
        raise ValueError(f"Snapshot is incomplete: {missing}; inspect manifest.json. Use --allow-partial for available files.")
    county_rows, precinct_rows, statewide_totals, legislative_totals, inventory = [], [], [], [], []
    county_totals = []
    for item in files:
        kind, number = item["kind"], item.get("county_id")
        if kind not in ("statewide", "legislative", "county"):
            raise ValueError(f"Unknown export kind: {kind}")
        path = (snapshot / item["path"]).resolve()
        if not path.is_relative_to(snapshot):
            raise ValueError("Export path must stay within its snapshot")
        rows, totals, races = parse_workbook(path, year, election, COUNTIES[number] if kind == "county" else None)
        inventory.extend(races)
        if kind == "county":
            precinct_rows.extend(rows)
            county_totals.extend(totals)
        else:
            county_rows.extend(rows)
            (legislative_totals if kind == "legislative" else statewide_totals).extend(totals)
    all_totals = pd.DataFrame(statewide_totals + legislative_totals)
    if all_totals.empty:
        raise ValueError("No statewide or legislative totals found")
    if all_totals.duplicated(["race", "candidate", "party"]).any():
        raise ValueError("Duplicate contest/candidate totals across exports")
    all_counties_present = {number for kind, number in actual if kind == "county"} == set(COUNTIES)
    complete_counties = all_counties_present and not race_gaps
    reconciled = 0
    unreconciled = []
    if county_totals:
        source = pd.DataFrame(county_totals).groupby(["race", "candidate", "party"]).votes.sum()
        expected_counties = pd.DataFrame(county_rows).groupby("race").county.agg(set).to_dict()
        present_counties = pd.DataFrame(county_totals).groupby("race").county.agg(set).to_dict()
        for row in all_totals.itertuples():
            key = (row.race, row.candidate, row.party)
            absent = expected_counties.get(row.race, set()) - present_counties.get(row.race, set())
            if absent:
                unreconciled.append({"race": row.race, "candidate": row.candidate,
                                     "party": row.party, "missing_counties": sorted(absent)})
                if complete_counties and not args.allow_partial:
                    raise ValueError(f"County exports omit {row.race} in {sorted(absent)}")
                continue
            if key not in source or int(source[key]) != row.votes:
                raise ValueError(f"County exports do not reconcile for {key}: expected {row.votes}, found {source.get(key)}")
            reconciled += 1
    cleaned = args.cleaned_dir or ROOT / "cleaned" / str(year) / election
    output = args.output_dir or ROOT / "outputs" / str(year) / election
    # Validate everything before replacing any published CSVs.
    cleaned.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(county_rows, columns=NORMAL_COLUMNS).to_csv(cleaned / "county-results.csv", index=False)
    # Write header-only files for unavailable exports so an earlier run's data
    # cannot remain alongside a newer validation report.
    pd.DataFrame(precinct_rows, columns=NORMAL_COLUMNS)[[c for c in NORMAL_COLUMNS if c != "race_name"]].to_csv(cleaned / "precinct-results.csv", index=False)
    for label, totals in [("statewide", statewide_totals), ("legislative", legislative_totals)]:
        frame = pd.DataFrame(totals, columns=["race", "race_name", "party", "candidate", "votes"])
        group = "district" if label == "legislative" else "race"
        frame[group] = frame["race"] if label == "legislative" else frame["race_name"]
        frame[[group, "party", "candidate", "votes"]].to_csv(
            output / f"{year}-{election}-{label}-vote-counts.csv", index=False)
        summary = summarize(frame, group, election)
        if label == "legislative":
            summary = district_context(summary, year)
        summary.to_csv(
            output / f"{year}-{label}-{election}-by-party-vote.csv", index=False)
    snapshot_reference = str(snapshot.relative_to(ROOT)) if snapshot.is_relative_to(ROOT) else str(snapshot)
    report = {"snapshot": snapshot_reference, "year": year, "election": election,
              "processed_at": datetime.now(timezone.utc).isoformat(),
              "missing_exports": missing, "download_failures": manifest.get("failures", []),
              "county_exports": sum(kind == "county" for kind, _ in actual),
              "precinct_coverage_complete": complete_counties,
              "incomplete_races": race_gaps,
              "candidate_totals_reconciled_across_counties": reconciled,
              "unreconciled_candidate_totals": unreconciled,
              "candidate_totals": len(all_totals), "precinct_rows": len(precinct_rows),
              "unmapped_races": sorted({r["title"] for r in inventory if r["type"] == "unmapped"}),
              "write_ins": manifest.get("write_ins"), "sheets": inventory}
    (cleaned / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Parsed {len(all_totals)} candidate/choice totals and {len(precinct_rows)} precinct rows.")
    print(f"Outputs: {output}\nValidation and normalized data: {cleaned}")
    if report["unmapped_races"]:
        print(f"Review {len(report['unmapped_races'])} preserved, unmapped contest(s) in validation.json.")
    if not complete_counties:
        print(f"Precinct coverage is incomplete; {reconciled} candidate totals could be reconciled across their counties.")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    download = commands.add_parser("fetch", help="Download dated, validated SOS export snapshots")
    download.add_argument("--year", type=int, required=True)
    download.add_argument("--election", choices=["general", "primary"], required=True)
    download.add_argument("--counties", type=county_ids, default=[], help="all, none (default), or IDs such as 1,32,56")
    download.add_argument("--destination", type=Path, help="New snapshot directory; must not exist")
    download.add_argument("--resume", action="store_true", help="Retry missing exports in --destination with the same county selection")
    download.set_defaults(func=fetch)
    imported = commands.add_parser("import-files", help="Create a snapshot from manually downloaded or certified XLSX exports")
    imported.add_argument("--year", type=int, required=True)
    imported.add_argument("--election", choices=["general", "primary"], required=True)
    imported.add_argument("--statewide", type=Path, required=True)
    imported.add_argument("--legislative", type=Path, required=True)
    imported.add_argument("--county", action="append", default=[], metavar="ID=PATH")
    imported.add_argument("--destination", type=Path, required=True, help="New snapshot directory")
    imported.set_defaults(func=import_files)
    parse = commands.add_parser("parse", help="Validate a snapshot and produce CSVs")
    parse.add_argument("--snapshot", type=Path, required=True)
    parse.add_argument("--allow-partial", action="store_true", help="Explicitly process available files in an incomplete snapshot")
    parse.add_argument("--cleaned-dir", type=Path)
    parse.add_argument("--output-dir", type=Path)
    parse.set_defaults(func=parse_snapshot)
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (ValueError, OSError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Interrupted; resume the saved snapshot with --resume.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
