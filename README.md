# Montana Secretary of State interface

System for wrangling election data from the MT Secretary of State's office and exporting it in more convenient formats. Developed for internal use at [Montana Free Press](https://montanafreepress.org).

### Current workflow (2026 onward)

`process/election_results.py` downloads and parses the live [SOS exports](https://electionresults.mt.gov/ResultsExport.aspx). It reads full contest titles inside workbooks instead of hardcoding election-specific numeric IDs or truncated worksheet names. Historical scripts remain available below.

The included November 20, 2026 capture is in `sos-data/2026/general/2026-11-20-live/`. Its generated CSVs are in `cleaned/2026/general/` and `outputs/2026/general/`; `cleaned/2026/general/validation.json` records coverage and reconciliation results.

Install dependencies into a virtual environment:

```sh
python3 -m venv venv
venv/bin/python -m pip install -r requirements.txt
```

Download statewide and legislative exports, plus all 56 counties:

```sh
venv/bin/python process/election_results.py fetch \
  --year 2026 --election general --counties all \
  --destination sos-data/2026/general/my-snapshot
```

The destination must be new. Omitting it creates a UTC timestamped directory automatically. Use `--counties none` (the default) for statewide/legislative totals only, or `--counties 1,32,56` for selected counties. County IDs are SOS's alphabetical IDs, 1–56; they are not license-plate numbers.

The downloader saves a `manifest.json` with source URLs, download times, requested counties, and failures. Every workbook must match the requested election and pass its own row-sum checks before it is accepted. The live URL serves the **current** election: changing `--year` cannot retrieve an archived election. In 2028, change the year and destination once the SOS site actually serves 2028 results. Primary elections use `--election primary`.

If bulk county exports return SOS error pages, the downloader automatically tries the county page's individual race exports and assembles a county workbook. If a race's Excel export also fails, it tries the public JSON service used by the site's precinct-results display, validating precinct sums against a separate county-total request. The original per-race workbooks, JSON responses, and request metadata remain in `race-exports/`; workbooks are reused across counties. If all methods for an individual race fail, successful races are retained, the missing race is recorded, and the command exits with status 1. An assembled county workbook is derived data; its originals are listed under `assembled_from` in the manifest.

Resume an interrupted or incomplete download by repeating the same options with `--resume`:

```sh
venv/bin/python process/election_results.py fetch \
  --year 2026 --election general --counties all \
  --destination sos-data/2026/general/my-snapshot --resume
```

Parse the snapshot:

```sh
venv/bin/python process/election_results.py parse \
  --snapshot sos-data/2026/general/my-snapshot
```

Incomplete snapshots require an explicit `--allow-partial`. This allows missing files or races, but never invalid vote counts or inconsistent sums. Download failures and incomplete precinct coverage remain visible in `validation.json`. Downloads taken while SOS totals are changing may fail reconciliation; capture a fresh snapshot once those totals settle.

Outputs go to `cleaned/<year>/<election>/` and `outputs/<year>/<election>/`, or directories supplied with `--cleaned-dir` and `--output-dir`:

| File | Contents |
| --- | --- |
| `cleaned/…/county-results.csv` | County-level candidate/choice votes from statewide and legislative exports |
| `cleaned/…/precinct-results.csv` | Available precinct votes with election, race, county, precinct, candidate/choice, party, and votes |
| `cleaned/…/validation.json` | Source headers and status, race inventory, unmapped contests, download failures, coverage, and reconciliation results |
| `outputs/…/<year>-<election>-legislative-vote-counts.csv` | Existing `district,party,candidate,votes` format |
| `outputs/…/<year>-<election>-statewide-vote-counts.csv` | Existing `race,party,candidate,votes` format; includes every contest supplied by the statewide workbook |
| `outputs/…/<year>-{legislative,statewide}-<election>-by-party-vote.csv` | Party summaries; legislative summaries retain Dave's Redistricting context for the current district map |

Parsing replaces these generated files for that election. Missing exports produce header-only CSVs, so old precinct data cannot masquerade as a newer capture. All sheets are preserved, including nonpartisan races, retention questions, and ballot issues. Yes/No choices have an empty party. Unrecognized contests retain their source ID and full title and are flagged for review. District keys use `HD-1` / `SD-1` consistently; statewide keys include `us-senate`, `us-house-west`, and `us-house-east`. The statewide export can also contain district or local contests; its filename does not guarantee statewide jurisdiction.

Validation checks election identity, duplicate rows/candidates, nonnegative integer votes, and each candidate's geographic sum against `TOTALS`. Where precinct exports cover every county for a contest, their sums are also checked against the statewide/legislative export. Coverage remains incomplete until all requested races across all 56 counties are present. Party summaries include all votes in their denominator, including third parties and independents. They do not call winners. Live results are unofficial and do not include write-ins; obtain write-ins separately before treating them as final totals.

For manually downloaded or certified workbooks, create a snapshot with explicit county identities:

```sh
venv/bin/python process/election_results.py import-files \
  --year 2026 --election general \
  --statewide /path/to/statewide.xlsx --legislative /path/to/legislative.xlsx \
  --county '1=/path/to/beaverhead.xlsx' --county '32=/path/to/missoula.xlsx' \
  --destination sos-data/2026/general/manual-snapshot
```

Repeat `--county ID=PATH` as needed, or omit it for totals only. Parse the resulting snapshot with the same `parse` command. The import checks workbook contents before copying them; retain the originals' provenance and verify write-in coverage separately.

Run regression and validation tests:

```sh
venv/bin/python -m unittest discover -s tests -v
```

### `/sos-data`

Raw data files in `sos-data` were downloaded from https://sosmt.gov/elections/results/ on on Oct. 30, 2024. As of that date, the Montana SOS didn't have an comprehensive Precinct by Precinct file data file available for the 2022 General Election. Precinct-level results for that election were instead stitched together from unofficial county-by-county vote data files downloaded from [electionresults.mt.gov](https://electionresults.mt.gov/) on 11/23/22.

### `/inputs`

Other data inputs fed into various data pipelines used by MTFP.
- `daves-redistricting` - [Dave's Redistricting](https://davesredistricting.org/) analysis for the state's 2023-2034 legislative districts.

### `/process`

Scripts for data workflow, organized by election year they apply to. Includes some one-off scripts for particular projects done at particular times. Filepaths in these are designed to be run from the repository root, e.g. as `python3 process/2022/parse-2022-precinct-results-by-county-files.py`

### `/cleaned`

Cleaned and (theoretically) standardized flat data, organized by election year.

### `/outputs`

Output files for specific purposes, organized by election year.

### `/utilities`

One-off tool scripts that may be helpful but don't fit into a neat data pipeline at this point.

