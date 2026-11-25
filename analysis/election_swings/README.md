# Montana election swings and story fact-checking

This standalone Python analysis compares the repository’s **retained 2024 and 2026 general-election snapshots**, without modifying the election processing pipeline or downloading fresh results. It needs only the existing pandas/openpyxl dependencies. No new packages are required.

From the repository root:

```sh
venv/bin/python analysis/election_swings/verify_claims.py
venv/bin/python analysis/election_swings/verify_claims.py --claim SENATE-TESTER-TO-BODNAR
venv/bin/python -m unittest discover -s tests -v
```

Use `python` in place of `venv/bin/python` if your active environment already has `requirements.txt` installed. Scripts locate the repository using their own location, so they can also be invoked from another working directory.

The verification command recomputes **all tables and claims**. It never rewrites the registry, expected values, geographic decisions or source data. `--claim` recomputes tables, prints the selected calculation rows, denominator precinct list and match coverage, and writes a claim-specific JSON file; it preserves the existing complete claim report. To refresh the complete report after reviewing one claim, run without `--claim`.

```sh
venv/bin/python analysis/election_swings/verify_claims.py --output /tmp/montana-election-analysis
venv/bin/python analysis/election_swings/verify_claims.py --registry /path/to/draft-claims.json
venv/bin/python analysis/election_swings/analyze.py  # tables and source audit only
```

`verify_claims.py` returns 1 for FAIL or SOURCE_INCOMPLETE, 2 for a malformed registry or analysis error, and 0 otherwise. A zero exit code **does not clear geographic-review flags**. Examine the explicit status of each claim. Unofficial/partial reporting is an unavoidable caveat on this snapshot; PASS means the arithmetic and source totals agree, not that the election is complete or certified. A claim marked `requires_final_results: true` receives SOURCE_INCOMPLETE for this snapshot. Failed expectations remain FAIL even if another caveat applies; `sample` and caveats remain in the result.

## Where to read results

- [Reporting findings](output/reporting-findings.md): MT-01, Senate candidate patterns, MT-02, additional leads and unresolved geography.
- [Story fact-check](output/story-fact-check.md): every registered calculation, expectation, result, denominator, status and evidence link.
- [Output inventory and CSV conventions](output/README.md): **all generated report and CSV paths**.
- [Source reconciliation](output/source-reconciliation.json): source commit, hashes, historical headers, snapshot/processing dates, reported completeness, limitations and individual candidate/geography comparisons.
- [Crosswalk audit](output/precinct-crosswalk-audit.csv) and [coverage](output/match-coverage.csv): both years’ source identifiers, evidence, exclusions and vote coverage.
- [Geographic investigation](sources/geographic-investigation.md): official sources examined, accepted pairs, changed boundaries and remaining questions.

The 2026 headers report 727 of 728 precincts reporting, with one partial. Write-ins are excluded. Export coverage across all 56 counties does not prove counting is finished. The 2024 retained workbooks also say **unofficial**, even though their headers report all precincts reporting; write-in completeness is not independently established. Refer to the raw headers rather than treating download dates as certification dates.

## Calculations and geographic scope

`core.py` implements validation, aggregation, arithmetic, plurality winners, matching and thresholds. `analyze.py` builds tables and independently reconstructs county candidate totals from the retained 2024 statewide workbook, alongside comparisons with both years’ aggregate CSVs and the 2026 county CSV. All 810 current candidate/geography checks pass. The sources are separate SOS exports, not an independent ballot recount. Uppercasing counties and explicitly mapping `LEWIS & CLARK` to `LEWIS AND CLARK` is recorded in the audit.

Shares and R-minus-D margins are fractions in CSVs. `_change_pp` and `winning_margin_pp` are percentage points. Votes are whole counts. Shares use **all candidate votes** except explicitly named two-party shares. Vote counts are summed before shares are calculated. No intermediate percentages are rounded. Publication display defaults to one decimal with Decimal half-up rounding; the claim JSON retains raw floating-point results and the 50-digit Decimal evaluation of count ratios. Those ratios independently check display rounding. Expected rounded benchmarks can request a separate `expected_rounding`.

Precinct winners use candidate plurality; ties, zero votes, missing candidate records and invalid data have explicit classifications. Malformed CSVs (duplicates, missing identifiers, negative/non-integer votes) fail before producing new analysis. `winner()` also exposes `invalid_data` for direct use. Missing candidates within a reported contest produce `missing_results`; a missing Senate precinct present in another federal contest is retained as missing. There is no authoritative complete absent-precinct inventory for House races, so a wholly absent House precinct cannot be assigned a district from names alone; source reconciliation and the coverage audit expose missing totals. Do not equate precinct presence with finished reporting.

Pondera’s House records are **district portions**. `35_VALIER RURAL` appears in both House races; both are valid portions. Senate results cannot be allocated between those portions. Senate winner counts by congressional district keep this record in `split_house_precinct_unallocated`, ensuring it is not duplicated. The relevant district is established separately in each election from that year’s House contest records.

The provisional sample is the original exact/normalized-name sample, excluding any documented boundary changes. Verification can add a documented rename outside that sample. Thus the provisional and verified samples overlap and are **not additive**. The audit matrix includes unpaired records and unverified proposed pairs; it is not a publication-ready transition matrix. Verified rankings include only documented common geography, positive contest totals and the named minimum in both years. Tied precincts can be ranked by share changes; a flip requires unique winners in both years. The geographically verified sample is narrow and cannot represent every precinct in a district or the state.

The accepted Lake pairs use the county’s map explicitly labeled for 2024–2032 plus its 2026 legislative assignments. Beaverhead precinct 12 has an explicit continuity statement; five other numbered precincts changed. See each row’s method and caveat. No statewide boundary overlay has been performed. Simple renames, splits and mergers elsewhere remain unresolved. One-to-many comparisons are intentionally unsupported: aggregate common territory with independently verified membership before adding a separate analysis; do not pretend aggregation creates an individual-precinct winner transition.

No 2022 precinct comparisons or 2022 Senate race are created. Optional 2022 House context was not needed for this implementation.

## Add a numerical story claim

Edit `claims.json` by copying a similar entry and assigning a unique stable ID. **Do not edit generated story-claims.csv to define a claim.** Each entry includes years, race, geography, candidate/party, sources, calculation, display precision, expectations and caveats. Set `expected_value` to null for a newly computed statistic, or supply the draft’s numerical value. Expectations are never inputs to the calculation.

Supported operations:

- `count`: number of rows satisfying `filters`. `denominator_filters` identifies the eligible universe in the same table; the numerator must be a subset. For a claim about Tester precincts use `senate-tester-precincts` and explicitly filter `provisional_comparable` or `geographically_verified`.
- `sum`: sum `column` over the selected rows. Optionally set `denominator_column` to retain the vote denominator, and `scale: 100` for shares stored as fractions.
- `ratio`: sum `numerator_column` divided by sum `denominator_column`, optionally scaled by 100. This aggregates counts before division.
- `minimum`: minimum of `column` across the selected rows, used for the most negative verified precinct share change. Ties retain the same minimum value.
- `difference`: one selected row’s `after_column` minus `before_column`, optionally scaled by 100. Its evidence labels these as operands, not a vote numerator and denominator.

Each filter has `column`, `op` (default `eq`) and `value`, or a `right_column` for column-to-column comparison. Supported comparisons: `eq`, `ne`, `lt`, `gt`, `le`, `ge`, `in`. Filters are ANDed and never executed as Python expressions. Choose a table/column from the generated CSVs. All table names are filenames without `.csv`.

Example claim for an additional county count:

```json
{
  "id": "MT01-COUNTIES-R-DROP-OVER-5PP",
  "description": "MT-01 county portions with Republican share down more than 5 pp",
  "years": [2024, 2026],
  "race": "us-house-west",
  "geographic_scope": "MT-01 county portions",
  "candidate_or_party": "Republican",
  "table": "county-swings",
  "filters": [
    {"column": "race", "value": "us-house-west"},
    {"column": "republican_share_change_pp", "op": "lt", "value": -5}
  ],
  "denominator_filters": [{"column": "race", "value": "us-house-west"}],
  "operation": "count",
  "calculation": "Count MT-01 county portions where (R26/total26 - R24/total24)*100 < -5",
  "source_files": ["cleaned/2024/general/precinct-results.csv", "cleaned/2026/general/precinct-results.csv"],
  "expected_value": null,
  "display_rounding": 0,
  "caveats": ["Unofficial snapshot; county portions, not necessarily whole counties."]
}
```

For precinct comparisons, include `sample: "provisional"` or `sample: "verified"` and matching sample filters. Provisional claims always remain NEEDS_GEOGRAPHIC_REVIEW even when an expected number matches. Empty verified comparison universes receive NOT_COMPARABLE, not an invented zero transition. Automatic guards also check the selected comparison records’ geography, preventing an omitted sample label from upgrading provisional comparisons.

Use `expected_rounding: 2` to compare publication values at two decimal places, or `absolute_tolerance` for an explicitly approximate benchmark. Avoid silently relaxing precise claims. The supplied approximate MT-02 two-party benchmark is checked within 0.01 pp; its correct two-decimal display is 64.29%.

Rerun the verification command and inspect the specific claim with `--claim ID`. A new calculation that cannot be expressed by existing tables needs a reusable function/table and a meaningful correctness test. The tool does **not** verify arbitrary prose or factual/causal interpretations.

## Trace records and update results

Each generated `evidence/ID.json` identifies selected and denominator CSV row numbers (including the header). Derived rows preserve county, precinct and both years’ source keys and candidate counts. Find the corresponding race/county/precinct/year in `source-records.csv`; its `source_file` and `source_row` identify the original cleaned CSV record. Aggregated claims select county or district rows whose raw candidate numerators and contest denominators remain visible. This permits an independent manual spreadsheet calculation.

After the existing repository pipeline updates cleaned/aggregate results, rerun verification. No network calls are needed. Old expectations remain untouched and may FAIL; inspect whether a draft is stale or a calculation/source is wrong. Geographic reviews fail closed when names disappear. For new or changed precincts, review boundaries before adding pairs to geographic-reviews.json. Tests use fixed, versioned source excerpts plus calculation/invariant tests. Full-snapshot benchmark tests run only when input SHA256s match their recorded snapshot, so legitimate source updates do not automatically invalidate calculation tests.
