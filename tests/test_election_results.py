"""Run with: python -m unittest discover -s tests -v"""

import argparse
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

SCRIPT = Path(__file__).resolve().parents[1] / "process" / "election_results.py"
SPEC = importlib.util.spec_from_file_location("election_results", SCRIPT)
results = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(results)


def table(title="UNITED STATES SENATOR", label="County", votes=(4, 6), total=10,
          choices=("A CANDIDATE\nRepublican",), year=2026):
    rows = [[f"{year} Unofficial General Election Results"], ["State of Montana"],
            ["Precincts 2 of 2 Reporting"], ["Downloaded at test time"], [], [],
            [title, label, *choices]]
    for place, vote in zip(["BEAVERHEAD", "BIG HORN"], votes):
        rows.append([None, place, *([vote] * len(choices))])
    rows.append([None, "TOTALS", *([total] * len(choices))])
    return pd.DataFrame(rows)


def workbook(path, sheets):
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        for name, frame in sheets.items():
            frame.to_excel(writer, sheet_name=name, header=False, index=False)


class ParsingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.path = self.folder / "export.xlsx"

    def parse(self, frame, sheet="99999changed tab name", **kwargs):
        workbook(self.path, {sheet: frame})
        return results.parse_workbook(self.path, 2026, "general", **kwargs)

    def test_full_title_disambiguates_truncated_house_sheet_names(self):
        for number, key in [(1, "us-house-west"), (2, "us-house-east")]:
            title = f"UNITED STATES REPRESENTATIVE {number}{'ST' if number == 1 else 'ND'} CONGRESSIONAL"
            _, totals, _ = self.parse(table(title))
            self.assertEqual(totals[0]["race"], key)

    def test_yes_no_choices_have_no_invented_party(self):
        rows, totals, _ = self.parse(table("CI-133 CONSTITUTIONAL INITIATIVE NO. 133", choices=("Yes", "No")))
        self.assertEqual({r["party"] for r in rows}, {""})
        self.assertEqual({r["candidate"] for r in totals}, {"Yes", "No"})
        self.assertEqual(totals[0]["race"], "ci-133")

    def test_invalid_votes_and_inconsistent_totals_are_rejected(self):
        for votes, total in [((4, 6), 11), ((-1, 11), 10), ((4.5, 5.5), 10), ((None, 10), 10)]:
            with self.subTest(votes=votes, total=total), self.assertRaises(ValueError):
                self.parse(table(votes=votes, total=total))

    def test_wrong_election_cannot_be_relabelled(self):
        with self.assertRaisesRegex(ValueError, "Expected 2026"):
            self.parse(table(year=2024))

    def test_duplicate_rows_rejected(self):
        frame = table()
        frame.iloc[8, 1] = frame.iloc[7, 1]
        with self.assertRaisesRegex(ValueError, "duplicate County"):
            self.parse(frame)

    def test_unknown_contests_are_preserved_and_flagged(self):
        rows, totals, inventory = self.parse(table("SOME LOCAL ISSUE"))
        self.assertEqual(len(rows), 2)
        self.assertEqual(totals[0]["race"], "sos-99999-some-local-issue")
        self.assertEqual(inventory[0]["type"], "unmapped")

    def test_legislative_district_normalizes_without_fixed_string_offsets(self):
        _, totals, _ = self.parse(table("STATE REPRESENTATIVE DISTRICT 007"))
        self.assertEqual(totals[0]["race"], "HD-7")

    def test_fallback_assembles_correct_county_and_reuses_originals(self):
        raw = self.folder / "race.xlsx"
        workbook(raw, {"Beaverhead": table(label="Precinct"), "Big Horn": table(label="Precinct", votes=(1, 2), total=3)})
        content = raw.read_bytes()
        form = results.ExportForm()
        form.feed('<input type="button" name="target" value="Precinct Level" raceid="450000000004069" party="">')
        with patch.object(results, "export_page", return_value=(None, "", form)), patch.object(results, "post_export", return_value=content) as post:
            first = self.folder / "county-01.xlsx"
            second = self.folder / "county-02.xlsx"
            sources = results.assemble_county("https://example.test", first, "01", 2026, "general")
            results.assemble_county("https://example.test", second, "02", 2026, "general")
            self.assertEqual(post.call_count, 1)
            self.assertTrue((self.folder / sources[0]["path"]).exists())
            self.assertEqual(results.parse_workbook(first, 2026, "general", "BEAVERHEAD")[1][0]["votes"], 10)
            self.assertEqual(results.parse_workbook(second, 2026, "general", "BIG HORN")[1][0]["votes"], 3)

    def test_fallback_retains_successful_races_when_another_export_fails(self):
        raw = self.folder / "race.xlsx"
        workbook(raw, {"Beaverhead": table(label="Precinct")})
        form = results.ExportForm()
        for race_id in ["450000000004069", "450000000005102"]:
            form.feed(f'<input type="button" name="target" value="Precinct Level" raceid="{race_id}">')
        with patch.object(results, "export_page", return_value=(None, "", form)), patch.object(results, "post_export", side_effect=[raw.read_bytes(), ValueError("SOS error")]):
            path = self.folder / "county-01.xlsx"
            sources = results.assemble_county("https://example.test", path, "01", 2026, "general")
        self.assertTrue(path.exists())
        self.assertEqual(len(sources), 2)
        self.assertIn("SOS error", sources[1]["error"])

    def test_api_recovery_uses_independent_county_totals(self):
        base = {"RaceID": 450000000005102, "CountyID": "01", "CountyName": "Beaverhead",
                "RaceName": "LOCAL ISSUE", "CandidateID": "9001", "calcCandidate": "Yes", "PartyName": ""}
        precincts = [{**base, "StatePrecinctID": 1, "PrecinctName": "PREC 01", "calcCandidateVotes": 4, "TotalPrecincts": 2},
                     {**base, "StatePrecinctID": 2, "PrecinctName": "PREC 02", "calcCandidateVotes": 6, "TotalPrecincts": 2}]
        totals = [{**base, "calcCandidateVotes": 10, "TotalPrecincts": 16}]
        frame = results.api_table(precincts, totals, "450000000005102", "01", 2026, "general")
        _, parsed, _ = self.parse(frame, county="BEAVERHEAD")
        self.assertEqual(parsed[0]["votes"], 10)
        totals[0]["calcCandidateVotes"] = 11
        with self.assertRaisesRegex(ValueError, "do not match"):
            results.api_table(precincts, totals, "450000000005102", "01", 2026, "general")
        totals[0]["calcCandidateVotes"] = 10
        for row in precincts:
            row["TotalPrecincts"] = 3
        with self.assertRaisesRegex(ValueError, "declared coverage"):
            results.api_table(precincts, totals, "450000000005102", "01", 2026, "general")

    def test_api_recovery_rejects_wrong_county_and_duplicate_records(self):
        base = {"RaceID": 450000000005102, "CountyID": "01", "CountyName": "Beaverhead",
                "RaceName": "LOCAL ISSUE", "CandidateID": "9001", "calcCandidate": "Yes", "PartyName": "",
                "StatePrecinctID": 1, "PrecinctName": "PREC 01", "calcCandidateVotes": 4}
        with self.assertRaisesRegex(ValueError, "different race or county"):
            results.api_table([base], [base], "450000000005102", "02", 2026, "general")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            results.api_table([base, base], [base], "450000000005102", "01", 2026, "general")

    def snapshot(self, county_total=10):
        workbook(self.folder / "statewide.xlsx", {"04069UNITED STATES SENATOR": table()})
        workbook(self.folder / "legislative.xlsx", {"HD 001": table("STATE REPRESENTATIVE DISTRICT 1")})
        files = [{"kind": "statewide", "path": "statewide.xlsx"},
                 {"kind": "legislative", "path": "legislative.xlsx"}]
        for number in ["01", "02"]:
            workbook(self.folder / f"county-{number}.xlsx", {
                "04069UNITED STATES SENATOR": table(label="Precinct", votes=(county_total, 0), total=county_total),
                "HD 001": table("STATE REPRESENTATIVE DISTRICT 1", label="Precinct", votes=(5, 0), total=5)})
            files.append({"kind": "county", "county_id": number, "path": f"county-{number}.xlsx"})
        manifest = {"year": 2026, "election": "general", "files": files, "requested_counties": ["01", "02"], "failures": []}
        (self.folder / "manifest.json").write_text(json.dumps(manifest))
        return argparse.Namespace(snapshot=self.folder, allow_partial=False,
                                  cleaned_dir=self.folder / "cleaned", output_dir=self.folder / "outputs")

    def test_full_county_reconciliation_prevents_publishing_mismatched_snapshot(self):
        args = self.snapshot(county_total=10)
        with patch.object(results, "COUNTIES", {"01": "BEAVERHEAD", "02": "BIG HORN"}):
            with self.assertRaisesRegex(ValueError, "do not reconcile"):
                results.parse_snapshot(args)
        self.assertFalse(args.output_dir.exists())

    def test_complete_snapshot_reconciles_and_writes_expected_schema(self):
        args = self.snapshot(county_total=5)
        with patch.object(results, "COUNTIES", {"01": "BEAVERHEAD", "02": "BIG HORN"}):
            self.assertEqual(results.parse_snapshot(args), 0)
        report = json.loads((args.cleaned_dir / "validation.json").read_text())
        self.assertTrue(report["precinct_coverage_complete"])
        self.assertEqual(report["candidate_totals_reconciled_across_counties"], 2)
        frame = pd.read_csv(args.output_dir / "2026-general-legislative-vote-counts.csv")
        self.assertEqual(list(frame.columns), ["district", "party", "candidate", "votes"])

    def test_missing_export_requires_explicit_partial_option(self):
        args = self.snapshot()
        manifest = json.loads((self.folder / "manifest.json").read_text())
        manifest["files"] = manifest["files"][:1]
        (self.folder / "manifest.json").write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "Snapshot is incomplete"):
            results.parse_snapshot(args)
        self.assertFalse(args.output_dir.exists())

    def test_explicit_partial_run_clears_stale_precinct_output(self):
        args = self.snapshot()
        manifest = json.loads((self.folder / "manifest.json").read_text())
        manifest["files"] = manifest["files"][:1]
        (self.folder / "manifest.json").write_text(json.dumps(manifest))
        args.allow_partial = True
        args.cleaned_dir.mkdir()
        (args.cleaned_dir / "precinct-results.csv").write_text("stale data")
        results.parse_snapshot(args)
        self.assertTrue(pd.read_csv(args.cleaned_dir / "precinct-results.csv").empty)
        self.assertTrue(pd.read_csv(args.output_dir / "2026-general-legislative-vote-counts.csv").empty)


class HistoricalRegressionTests(unittest.TestCase):
    def test_2024_legislative_totals_match_existing_export(self):
        path = results.ROOT / "sos-data/2024/general/2024-12-11-legislative-results.xlsx"
        if not path.exists():
            self.skipTest("Historical workbook unavailable")
        _, totals, _ = results.parse_workbook(path, 2024, "general")
        actual = pd.DataFrame(totals).rename(columns={"race": "district"})
        expected = pd.read_csv(results.ROOT / "outputs/2024/general/2024-general-legislative-vote-counts.csv")
        cols = ["district", "party", "candidate", "votes"]
        pd.testing.assert_frame_equal(actual[cols].sort_values(cols).reset_index(drop=True),
                                      expected[cols].sort_values(cols).reset_index(drop=True), check_dtype=False)


if __name__ == "__main__":
    unittest.main()
