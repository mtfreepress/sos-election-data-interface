# Story fact-check

PASS verifies arithmetic in the retained snapshot. It does not certify final results.
The 2026 headers report 727/728 precincts, one partial; write-ins are excluded. 2024 retained headers also say unofficial.
Claims without expected values are recomputed calculations, not comparisons against a draft assertion.
Differences report after and before operands; their numerator/denominator fields are not a vote ratio.

Status totals: {"PASS": 903, "NEEDS_GEOGRAPHIC_REVIEW": 13}

## MT01-R-SHARE-2024: PASS

MT01: R share of all candidate votes, 2024 (%)

Expected: 52.29 | Calculated: 52.294998541577456 | Display: 52.3
Numerator / after operand: 168529 | Denominator / before operand: 322266 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-R-SHARE-2024.json](evidence/MT01-R-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-R-VOTES-2024: PASS

MT01: R votes, 2024

Expected: None | Calculated: 168529 | Display: 168529
Numerator / after operand: 168529 | Denominator / before operand: 322266 (eligible rows or contest votes)

Calculation: `{"column": "republican_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-R-VOTES-2024.json](evidence/MT01-R-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-D-SHARE-2024: PASS

MT01: D share of all candidate votes, 2024 (%)

Expected: 44.62 | Calculated: 44.61624868897122 | Display: 44.6
Numerator / after operand: 143783 | Denominator / before operand: 322266 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-D-SHARE-2024.json](evidence/MT01-D-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-D-VOTES-2024: PASS

MT01: D votes, 2024

Expected: None | Calculated: 143783 | Display: 143783
Numerator / after operand: 143783 | Denominator / before operand: 322266 (eligible rows or contest votes)

Calculation: `{"column": "democratic_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-D-VOTES-2024.json](evidence/MT01-D-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-L-SHARE-2024: PASS

MT01: L share of all candidate votes, 2024 (%)

Expected: None | Calculated: 3.088752769451323 | Display: 3.1
Numerator / after operand: 9954 | Denominator / before operand: 322266 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "libertarian_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-L-SHARE-2024.json](evidence/MT01-L-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-L-VOTES-2024: PASS

MT01: L votes, 2024

Expected: None | Calculated: 9954 | Display: 9954
Numerator / after operand: 9954 | Denominator / before operand: 322266 (eligible rows or contest votes)

Calculation: `{"column": "libertarian_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-L-VOTES-2024.json](evidence/MT01-L-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-I-SHARE-2024: PASS

MT01: I share of all candidate votes, 2024 (%)

Expected: None | Calculated: 0.0 | Display: 0.0
Numerator / after operand: 0 | Denominator / before operand: 322266 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "independent_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-I-SHARE-2024.json](evidence/MT01-I-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-I-VOTES-2024: PASS

MT01: I votes, 2024

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 322266 (eligible rows or contest votes)

Calculation: `{"column": "independent_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-I-VOTES-2024.json](evidence/MT01-I-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-TOTAL-VOTES-2024: PASS

MT01: total candidate votes, 2024

Expected: None | Calculated: 322266 | Display: 322266
Numerator / after operand: 322266 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-TOTAL-VOTES-2024.json](evidence/MT01-TOTAL-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-R-MARGIN-2024: PASS

MT01: Republican-minus-Democratic margin, 2024 (pp)

Expected: 7.68 | Calculated: 7.678749852606232 | Display: 7.7
Numerator / after operand: 24746 | Denominator / before operand: 322266 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "republican_minus_democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-R-MARGIN-2024.json](evidence/MT01-R-MARGIN-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-R-TWO-PARTY-2024: PASS

MT01: Republican two-party share, 2024 (%)

Expected: None | Calculated: 53.9617433848203 | Display: 54.0
Numerator / after operand: 168529 | Denominator / before operand: 312312 (eligible rows or contest votes)

Calculation: `{"denominator_column": "two_party_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-R-TWO-PARTY-2024.json](evidence/MT01-R-TWO-PARTY-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-R-SHARE-2026: PASS

MT01: R share of all candidate votes, 2026 (%)

Expected: 46.64 | Calculated: 46.638302323062156 | Display: 46.6
Numerator / after operand: 124854 | Denominator / before operand: 267707 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-R-SHARE-2026.json](evidence/MT01-R-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-R-VOTES-2026: PASS

MT01: R votes, 2026

Expected: None | Calculated: 124854 | Display: 124854
Numerator / after operand: 124854 | Denominator / before operand: 267707 (eligible rows or contest votes)

Calculation: `{"column": "republican_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-R-VOTES-2026.json](evidence/MT01-R-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-D-SHARE-2026: PASS

MT01: D share of all candidate votes, 2026 (%)

Expected: 50.48 | Calculated: 50.47757436301629 | Display: 50.5
Numerator / after operand: 135132 | Denominator / before operand: 267707 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-D-SHARE-2026.json](evidence/MT01-D-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-D-VOTES-2026: PASS

MT01: D votes, 2026

Expected: None | Calculated: 135132 | Display: 135132
Numerator / after operand: 135132 | Denominator / before operand: 267707 (eligible rows or contest votes)

Calculation: `{"column": "democratic_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-D-VOTES-2026.json](evidence/MT01-D-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-L-SHARE-2026: PASS

MT01: L share of all candidate votes, 2026 (%)

Expected: None | Calculated: 2.8841233139215636 | Display: 2.9
Numerator / after operand: 7721 | Denominator / before operand: 267707 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "libertarian_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-L-SHARE-2026.json](evidence/MT01-L-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-L-VOTES-2026: PASS

MT01: L votes, 2026

Expected: None | Calculated: 7721 | Display: 7721
Numerator / after operand: 7721 | Denominator / before operand: 267707 (eligible rows or contest votes)

Calculation: `{"column": "libertarian_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-L-VOTES-2026.json](evidence/MT01-L-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-I-SHARE-2026: PASS

MT01: I share of all candidate votes, 2026 (%)

Expected: None | Calculated: 0.0 | Display: 0.0
Numerator / after operand: 0 | Denominator / before operand: 267707 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "independent_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-I-SHARE-2026.json](evidence/MT01-I-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-I-VOTES-2026: PASS

MT01: I votes, 2026

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 267707 (eligible rows or contest votes)

Calculation: `{"column": "independent_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-I-VOTES-2026.json](evidence/MT01-I-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-TOTAL-VOTES-2026: PASS

MT01: total candidate votes, 2026

Expected: None | Calculated: 267707 | Display: 267707
Numerator / after operand: 267707 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-TOTAL-VOTES-2026.json](evidence/MT01-TOTAL-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-R-MARGIN-2026: PASS

MT01: Republican-minus-Democratic margin, 2026 (pp)

Expected: -3.84 | Calculated: -3.8392720399541287 | Display: -3.8
Numerator / after operand: -10278 | Denominator / before operand: 267707 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "republican_minus_democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-R-MARGIN-2026.json](evidence/MT01-R-MARGIN-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-R-TWO-PARTY-2026: PASS

MT01: Republican two-party share, 2026 (%)

Expected: None | Calculated: 48.02335510373636 | Display: 48.0
Numerator / after operand: 124854 | Denominator / before operand: 259986 (eligible rows or contest votes)

Calculation: `{"denominator_column": "two_party_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-R-TWO-PARTY-2026.json](evidence/MT01-R-TWO-PARTY-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-R-SHARE-CHANGE: PASS

MT01: 2024–26 change in republican_share (pp)

Expected: None | Calculated: -5.6566962185153 | Display: -5.7
Numerator / after operand: 0.46638302323062153 | Denominator / before operand: 0.5229499854157745 (before value)

Calculation: `{"after_column": "republican_share_2026", "before_column": "republican_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}], "operation": "difference", "scale": 100, "table": "district-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-R-SHARE-CHANGE.json](evidence/MT01-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MARGIN-CHANGE: PASS

MT01: 2024–26 change in republican_margin (pp)

Expected: -11.52 | Calculated: -11.518021892560359 | Display: -11.5
Numerator / after operand: -0.03839272039954129 | Denominator / before operand: 0.07678749852606231 (before value)

Calculation: `{"after_column": "republican_margin_2026", "before_column": "republican_margin_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}], "operation": "difference", "scale": 100, "table": "district-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-MARGIN-CHANGE.json](evidence/MT01-MARGIN-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-TWO-PARTY-CHANGE: PASS

MT01: 2024–26 change in republican_two_party_share (pp)

Expected: None | Calculated: -5.938388281083951 | Display: -5.9
Numerator / after operand: 0.48023355103736354 | Denominator / before operand: 0.539617433848203 (before value)

Calculation: `{"after_column": "republican_two_party_share_2026", "before_column": "republican_two_party_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}], "operation": "difference", "scale": 100, "table": "district-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-TWO-PARTY-CHANGE.json](evidence/MT01-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COUNTIES-DECLINED: PASS

MT01: county portions where republican_share declined

Expected: 15 | Calculated: 15 | Display: 15
Numerator / after operand: 15 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-west"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "republican_share_change_pp", "op": "lt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COUNTIES-DECLINED.json](evidence/MT01-COUNTIES-DECLINED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COUNTIES-INCREASED: PASS

MT01: county portions where republican_share increased

Expected: 1 | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-west"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "republican_share_change_pp", "op": "gt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COUNTIES-INCREASED.json](evidence/MT01-COUNTIES-INCREASED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COUNTIES-UNCHANGED: PASS

MT01: county portions where republican_share unchanged

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-west"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "republican_share_change_pp", "op": "eq", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COUNTIES-UNCHANGED.json](evidence/MT01-COUNTIES-UNCHANGED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COUNTIES-DECLINED-TWO-PARTY: PASS

MT01: county portions where republican_two_party_share declined

Expected: None | Calculated: 15 | Display: 15
Numerator / after operand: 15 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-west"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "republican_two_party_share_change_pp", "op": "lt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COUNTIES-DECLINED-TWO-PARTY.json](evidence/MT01-COUNTIES-DECLINED-TWO-PARTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COUNTIES-INCREASED-TWO-PARTY: PASS

MT01: county portions where republican_two_party_share increased

Expected: None | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-west"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "republican_two_party_share_change_pp", "op": "gt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COUNTIES-INCREASED-TWO-PARTY.json](evidence/MT01-COUNTIES-INCREASED-TWO-PARTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COUNTIES-UNCHANGED-TWO-PARTY: PASS

MT01: county portions where republican_two_party_share unchanged

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-west"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "republican_two_party_share_change_pp", "op": "eq", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COUNTIES-UNCHANGED-TWO-PARTY.json](evidence/MT01-COUNTIES-UNCHANGED-TWO-PARTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-BEAVERHEAD-R-SHARE-CHANGE: PASS

MT01: BEAVERHEAD, republican_share_change_pp

Expected: None | Calculated: -3.9148469405436592 | Display: -3.9
Numerator / after operand: -3.9148469405436592 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "BEAVERHEAD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-BEAVERHEAD-R-SHARE-CHANGE.json](evidence/MT01-BEAVERHEAD-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-BEAVERHEAD-TWO-PARTY-CHANGE: PASS

MT01: BEAVERHEAD, republican_two_party_share_change_pp

Expected: None | Calculated: -3.8049521883767867 | Display: -3.8
Numerator / after operand: -3.8049521883767867 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "BEAVERHEAD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-BEAVERHEAD-TWO-PARTY-CHANGE.json](evidence/MT01-BEAVERHEAD-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-DEER-LODGE-R-SHARE-CHANGE: PASS

MT01: DEER LODGE, republican_share_change_pp

Expected: None | Calculated: -3.8781366205018597 | Display: -3.9
Numerator / after operand: -3.8781366205018597 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "DEER LODGE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-DEER-LODGE-R-SHARE-CHANGE.json](evidence/MT01-DEER-LODGE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-DEER-LODGE-TWO-PARTY-CHANGE: PASS

MT01: DEER LODGE, republican_two_party_share_change_pp

Expected: None | Calculated: -3.9275336637727754 | Display: -3.9
Numerator / after operand: -3.9275336637727754 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "DEER LODGE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-DEER-LODGE-TWO-PARTY-CHANGE.json](evidence/MT01-DEER-LODGE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-FLATHEAD-R-SHARE-CHANGE: PASS

MT01: FLATHEAD, republican_share_change_pp

Expected: -5.07 | Calculated: -5.072407893954689 | Display: -5.1
Numerator / after operand: -5.072407893954689 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "FLATHEAD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-FLATHEAD-R-SHARE-CHANGE.json](evidence/MT01-FLATHEAD-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-FLATHEAD-TWO-PARTY-CHANGE: PASS

MT01: FLATHEAD, republican_two_party_share_change_pp

Expected: None | Calculated: -5.209389603278758 | Display: -5.2
Numerator / after operand: -5.209389603278758 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "FLATHEAD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-FLATHEAD-TWO-PARTY-CHANGE.json](evidence/MT01-FLATHEAD-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-GALLATIN-R-SHARE-CHANGE: PASS

MT01: GALLATIN, republican_share_change_pp

Expected: -7.42 | Calculated: -7.418830355730344 | Display: -7.4
Numerator / after operand: -7.418830355730344 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-GALLATIN-R-SHARE-CHANGE.json](evidence/MT01-GALLATIN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-GALLATIN-TWO-PARTY-CHANGE: PASS

MT01: GALLATIN, republican_two_party_share_change_pp

Expected: None | Calculated: -7.784535506573487 | Display: -7.8
Numerator / after operand: -7.784535506573487 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-GALLATIN-TWO-PARTY-CHANGE.json](evidence/MT01-GALLATIN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-GLACIER-R-SHARE-CHANGE: PASS

MT01: GLACIER, republican_share_change_pp

Expected: None | Calculated: -4.305105107099205 | Display: -4.3
Numerator / after operand: -4.305105107099205 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "GLACIER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-GLACIER-R-SHARE-CHANGE.json](evidence/MT01-GLACIER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-GLACIER-TWO-PARTY-CHANGE: PASS

MT01: GLACIER, republican_two_party_share_change_pp

Expected: None | Calculated: -4.4820501605039365 | Display: -4.5
Numerator / after operand: -4.4820501605039365 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "GLACIER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-GLACIER-TWO-PARTY-CHANGE.json](evidence/MT01-GLACIER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-GRANITE-R-SHARE-CHANGE: PASS

MT01: GRANITE, republican_share_change_pp

Expected: None | Calculated: -4.617132018878745 | Display: -4.6
Numerator / after operand: -4.617132018878745 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "GRANITE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-GRANITE-R-SHARE-CHANGE.json](evidence/MT01-GRANITE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-GRANITE-TWO-PARTY-CHANGE: PASS

MT01: GRANITE, republican_two_party_share_change_pp

Expected: None | Calculated: -5.00725332080888 | Display: -5.0
Numerator / after operand: -5.00725332080888 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "GRANITE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-GRANITE-TWO-PARTY-CHANGE.json](evidence/MT01-GRANITE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-LAKE-R-SHARE-CHANGE: PASS

MT01: LAKE, republican_share_change_pp

Expected: None | Calculated: -2.9661984792989204 | Display: -3.0
Numerator / after operand: -2.9661984792989204 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "LAKE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-LAKE-R-SHARE-CHANGE.json](evidence/MT01-LAKE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-LAKE-TWO-PARTY-CHANGE: PASS

MT01: LAKE, republican_two_party_share_change_pp

Expected: None | Calculated: -3.0609192044764644 | Display: -3.1
Numerator / after operand: -3.0609192044764644 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "LAKE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-LAKE-TWO-PARTY-CHANGE.json](evidence/MT01-LAKE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-LINCOLN-R-SHARE-CHANGE: PASS

MT01: LINCOLN, republican_share_change_pp

Expected: None | Calculated: -1.941170490416777 | Display: -1.9
Numerator / after operand: -1.941170490416777 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "LINCOLN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-LINCOLN-R-SHARE-CHANGE.json](evidence/MT01-LINCOLN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-LINCOLN-TWO-PARTY-CHANGE: PASS

MT01: LINCOLN, republican_two_party_share_change_pp

Expected: None | Calculated: -2.2959277366292774 | Display: -2.3
Numerator / after operand: -2.2959277366292774 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "LINCOLN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-LINCOLN-TWO-PARTY-CHANGE.json](evidence/MT01-LINCOLN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MADISON-R-SHARE-CHANGE: PASS

MT01: MADISON, republican_share_change_pp

Expected: -5.91 | Calculated: -5.905055300284879 | Display: -5.9
Numerator / after operand: -5.905055300284879 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "MADISON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-MADISON-R-SHARE-CHANGE.json](evidence/MT01-MADISON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MADISON-TWO-PARTY-CHANGE: PASS

MT01: MADISON, republican_two_party_share_change_pp

Expected: None | Calculated: -5.993225465963958 | Display: -6.0
Numerator / after operand: -5.993225465963958 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "MADISON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-MADISON-TWO-PARTY-CHANGE.json](evidence/MT01-MADISON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MINERAL-R-SHARE-CHANGE: PASS

MT01: MINERAL, republican_share_change_pp

Expected: None | Calculated: -4.5364628396534545 | Display: -4.5
Numerator / after operand: -4.5364628396534545 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "MINERAL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-MINERAL-R-SHARE-CHANGE.json](evidence/MT01-MINERAL-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MINERAL-TWO-PARTY-CHANGE: PASS

MT01: MINERAL, republican_two_party_share_change_pp

Expected: None | Calculated: -4.30563679924334 | Display: -4.3
Numerator / after operand: -4.30563679924334 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "MINERAL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-MINERAL-TWO-PARTY-CHANGE.json](evidence/MT01-MINERAL-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MISSOULA-R-SHARE-CHANGE: PASS

MT01: MISSOULA, republican_share_change_pp

Expected: -6.47 | Calculated: -6.468261533431013 | Display: -6.5
Numerator / after operand: -6.468261533431013 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-MISSOULA-R-SHARE-CHANGE.json](evidence/MT01-MISSOULA-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MISSOULA-TWO-PARTY-CHANGE: PASS

MT01: MISSOULA, republican_two_party_share_change_pp

Expected: None | Calculated: -6.868401625106801 | Display: -6.9
Numerator / after operand: -6.868401625106801 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-MISSOULA-TWO-PARTY-CHANGE.json](evidence/MT01-MISSOULA-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-PONDERA-R-SHARE-CHANGE: PASS

MT01: PONDERA, republican_share_change_pp

Expected: 2.05 | Calculated: 2.0457749283900872 | Display: 2.0
Numerator / after operand: 2.0457749283900872 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-PONDERA-R-SHARE-CHANGE.json](evidence/MT01-PONDERA-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-PONDERA-TWO-PARTY-CHANGE: PASS

MT01: PONDERA, republican_two_party_share_change_pp

Expected: None | Calculated: 2.0425104552891593 | Display: 2.0
Numerator / after operand: 2.0425104552891593 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-PONDERA-TWO-PARTY-CHANGE.json](evidence/MT01-PONDERA-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-POWELL-R-SHARE-CHANGE: PASS

MT01: POWELL, republican_share_change_pp

Expected: None | Calculated: -4.55031144255218 | Display: -4.6
Numerator / after operand: -4.55031144255218 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "POWELL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-POWELL-R-SHARE-CHANGE.json](evidence/MT01-POWELL-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-POWELL-TWO-PARTY-CHANGE: PASS

MT01: POWELL, republican_two_party_share_change_pp

Expected: None | Calculated: -4.330306182900568 | Display: -4.3
Numerator / after operand: -4.330306182900568 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "POWELL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-POWELL-TWO-PARTY-CHANGE.json](evidence/MT01-POWELL-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-RAVALLI-R-SHARE-CHANGE: PASS

MT01: RAVALLI, republican_share_change_pp

Expected: -4.89 | Calculated: -4.890070938284142 | Display: -4.9
Numerator / after operand: -4.890070938284142 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "RAVALLI"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-RAVALLI-R-SHARE-CHANGE.json](evidence/MT01-RAVALLI-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-RAVALLI-TWO-PARTY-CHANGE: PASS

MT01: RAVALLI, republican_two_party_share_change_pp

Expected: None | Calculated: -4.756175654832839 | Display: -4.8
Numerator / after operand: -4.756175654832839 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "RAVALLI"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-RAVALLI-TWO-PARTY-CHANGE.json](evidence/MT01-RAVALLI-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-SANDERS-R-SHARE-CHANGE: PASS

MT01: SANDERS, republican_share_change_pp

Expected: None | Calculated: -2.5072008195293427 | Display: -2.5
Numerator / after operand: -2.5072008195293427 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "SANDERS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-SANDERS-R-SHARE-CHANGE.json](evidence/MT01-SANDERS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-SANDERS-TWO-PARTY-CHANGE: PASS

MT01: SANDERS, republican_two_party_share_change_pp

Expected: None | Calculated: -2.149857002494693 | Display: -2.1
Numerator / after operand: -2.149857002494693 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "SANDERS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-SANDERS-TWO-PARTY-CHANGE.json](evidence/MT01-SANDERS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-SILVER-BOW-R-SHARE-CHANGE: PASS

MT01: SILVER BOW, republican_share_change_pp

Expected: -5.96 | Calculated: -5.955747933321853 | Display: -6.0
Numerator / after operand: -5.955747933321853 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "SILVER BOW"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-SILVER-BOW-R-SHARE-CHANGE.json](evidence/MT01-SILVER-BOW-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-SILVER-BOW-TWO-PARTY-CHANGE: PASS

MT01: SILVER BOW, republican_two_party_share_change_pp

Expected: None | Calculated: -6.420435661261048 | Display: -6.4
Numerator / after operand: -6.420435661261048 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "SILVER BOW"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-SILVER-BOW-TWO-PARTY-CHANGE.json](evidence/MT01-SILVER-BOW-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-SHARE-2024: PASS

MT02: R share of all candidate votes, 2024 (%)

Expected: 65.99 | Calculated: 65.9899471955579 | Display: 66.0
Numerator / after operand: 181832 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-R-SHARE-2024.json](evidence/MT02-R-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-VOTES-2024: PASS

MT02: R votes, 2024

Expected: None | Calculated: 181832 | Display: 181832
Numerator / after operand: 181832 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"column": "republican_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-R-VOTES-2024.json](evidence/MT02-R-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-D-SHARE-2024: PASS

MT02: D share of all candidate votes, 2024 (%)

Expected: None | Calculated: 34.010052804442104 | Display: 34.0
Numerator / after operand: 93713 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-D-SHARE-2024.json](evidence/MT02-D-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-D-VOTES-2024: PASS

MT02: D votes, 2024

Expected: None | Calculated: 93713 | Display: 93713
Numerator / after operand: 93713 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"column": "democratic_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-D-VOTES-2024.json](evidence/MT02-D-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-L-SHARE-2024: PASS

MT02: L share of all candidate votes, 2024 (%)

Expected: None | Calculated: 0.0 | Display: 0.0
Numerator / after operand: 0 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "libertarian_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-L-SHARE-2024.json](evidence/MT02-L-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-L-VOTES-2024: PASS

MT02: L votes, 2024

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"column": "libertarian_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-L-VOTES-2024.json](evidence/MT02-L-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-I-SHARE-2024: PASS

MT02: I share of all candidate votes, 2024 (%)

Expected: None | Calculated: 0.0 | Display: 0.0
Numerator / after operand: 0 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "independent_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-I-SHARE-2024.json](evidence/MT02-I-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-I-VOTES-2024: PASS

MT02: I votes, 2024

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"column": "independent_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-I-VOTES-2024.json](evidence/MT02-I-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TOTAL-VOTES-2024: PASS

MT02: total candidate votes, 2024

Expected: None | Calculated: 275545 | Display: 275545
Numerator / after operand: 275545 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-TOTAL-VOTES-2024.json](evidence/MT02-TOTAL-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-MARGIN-2024: PASS

MT02: Republican-minus-Democratic margin, 2024 (pp)

Expected: None | Calculated: 31.97989439111579 | Display: 32.0
Numerator / after operand: 88119 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "republican_minus_democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-R-MARGIN-2024.json](evidence/MT02-R-MARGIN-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-TWO-PARTY-2024: PASS

MT02: Republican two-party share, 2024 (%)

Expected: None | Calculated: 65.9899471955579 | Display: 66.0
Numerator / after operand: 181832 | Denominator / before operand: 275545 (eligible rows or contest votes)

Calculation: `{"denominator_column": "two_party_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-R-TWO-PARTY-2024.json](evidence/MT02-R-TWO-PARTY-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-SHARE-2026: PASS

MT02: R share of all candidate votes, 2026 (%)

Expected: 58.1 | Calculated: 58.10259478866344 | Display: 58.1
Numerator / after operand: 128172 | Denominator / before operand: 220596 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-R-SHARE-2026.json](evidence/MT02-R-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-VOTES-2026: PASS

MT02: R votes, 2026

Expected: None | Calculated: 128172 | Display: 128172
Numerator / after operand: 128172 | Denominator / before operand: 220596 (eligible rows or contest votes)

Calculation: `{"column": "republican_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-R-VOTES-2026.json](evidence/MT02-R-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-D-SHARE-2026: PASS

MT02: D share of all candidate votes, 2026 (%)

Expected: None | Calculated: 32.26667754628371 | Display: 32.3
Numerator / after operand: 71179 | Denominator / before operand: 220596 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-D-SHARE-2026.json](evidence/MT02-D-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-D-VOTES-2026: PASS

MT02: D votes, 2026

Expected: None | Calculated: 71179 | Display: 71179
Numerator / after operand: 71179 | Denominator / before operand: 220596 (eligible rows or contest votes)

Calculation: `{"column": "democratic_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-D-VOTES-2026.json](evidence/MT02-D-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-L-SHARE-2026: PASS

MT02: L share of all candidate votes, 2026 (%)

Expected: None | Calculated: 1.8341221055685506 | Display: 1.8
Numerator / after operand: 4046 | Denominator / before operand: 220596 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "libertarian_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-L-SHARE-2026.json](evidence/MT02-L-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-L-VOTES-2026: PASS

MT02: L votes, 2026

Expected: None | Calculated: 4046 | Display: 4046
Numerator / after operand: 4046 | Denominator / before operand: 220596 (eligible rows or contest votes)

Calculation: `{"column": "libertarian_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-L-VOTES-2026.json](evidence/MT02-L-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-I-SHARE-2026: PASS

MT02: I share of all candidate votes, 2026 (%)

Expected: None | Calculated: 7.796605559484306 | Display: 7.8
Numerator / after operand: 17199 | Denominator / before operand: 220596 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "independent_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-I-SHARE-2026.json](evidence/MT02-I-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-I-VOTES-2026: PASS

MT02: I votes, 2026

Expected: 17199 | Calculated: 17199 | Display: 17199
Numerator / after operand: 17199 | Denominator / before operand: 220596 (eligible rows or contest votes)

Calculation: `{"column": "independent_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-I-VOTES-2026.json](evidence/MT02-I-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TOTAL-VOTES-2026: PASS

MT02: total candidate votes, 2026

Expected: None | Calculated: 220596 | Display: 220596
Numerator / after operand: 220596 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TOTAL-VOTES-2026.json](evidence/MT02-TOTAL-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-MARGIN-2026: PASS

MT02: Republican-minus-Democratic margin, 2026 (pp)

Expected: None | Calculated: 25.835917242379736 | Display: 25.8
Numerator / after operand: 56993 | Denominator / before operand: 220596 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "republican_minus_democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-R-MARGIN-2026.json](evidence/MT02-R-MARGIN-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-TWO-PARTY-2026: PASS

MT02: Republican two-party share, 2026 (%)

Expected: 64.3 | Calculated: 64.29463609412544 | Display: 64.3
Numerator / after operand: 128172 | Denominator / before operand: 199351 (eligible rows or contest votes)

Calculation: `{"denominator_column": "two_party_votes", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-R-TWO-PARTY-2026.json](evidence/MT02-R-TWO-PARTY-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion. The supplied approximate 64.30% benchmark is checked within 0.01 percentage point. Exact output rounds to 64.29% at two decimal places.

## MT02-R-SHARE-CHANGE: PASS

MT02: 2024–26 change in republican_share (pp)

Expected: None | Calculated: -7.887352406894454 | Display: -7.9
Numerator / after operand: 0.5810259478866344 | Denominator / before operand: 0.659899471955579 (before value)

Calculation: `{"after_column": "republican_share_2026", "before_column": "republican_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}], "operation": "difference", "scale": 100, "table": "district-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-R-SHARE-CHANGE.json](evidence/MT02-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-MARGIN-CHANGE: PASS

MT02: 2024–26 change in republican_margin (pp)

Expected: None | Calculated: -6.1439771487360515 | Display: -6.1
Numerator / after operand: 0.25835917242379736 | Denominator / before operand: 0.3197989439111579 (before value)

Calculation: `{"after_column": "republican_margin_2026", "before_column": "republican_margin_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}], "operation": "difference", "scale": 100, "table": "district-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-MARGIN-CHANGE.json](evidence/MT02-MARGIN-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TWO-PARTY-CHANGE: PASS

MT02: 2024–26 change in republican_two_party_share (pp)

Expected: None | Calculated: -1.6953111014324618 | Display: -1.7
Numerator / after operand: 0.6429463609412543 | Denominator / before operand: 0.659899471955579 (before value)

Calculation: `{"after_column": "republican_two_party_share_2026", "before_column": "republican_two_party_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}], "operation": "difference", "scale": 100, "table": "district-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TWO-PARTY-CHANGE.json](evidence/MT02-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COUNTIES-DECLINED: PASS

MT02: county portions where republican_share declined

Expected: None | Calculated: 41 | Display: 41
Numerator / after operand: 41 | Denominator / before operand: 41 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-east"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "republican_share_change_pp", "op": "lt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COUNTIES-DECLINED.json](evidence/MT02-COUNTIES-DECLINED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COUNTIES-INCREASED: PASS

MT02: county portions where republican_share increased

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 41 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-east"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "republican_share_change_pp", "op": "gt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COUNTIES-INCREASED.json](evidence/MT02-COUNTIES-INCREASED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COUNTIES-UNCHANGED: PASS

MT02: county portions where republican_share unchanged

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 41 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-east"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "republican_share_change_pp", "op": "eq", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COUNTIES-UNCHANGED.json](evidence/MT02-COUNTIES-UNCHANGED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COUNTIES-DECLINED-TWO-PARTY: PASS

MT02: county portions where republican_two_party_share declined

Expected: None | Calculated: 25 | Display: 25
Numerator / after operand: 25 | Denominator / before operand: 41 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-east"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "republican_two_party_share_change_pp", "op": "lt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COUNTIES-DECLINED-TWO-PARTY.json](evidence/MT02-COUNTIES-DECLINED-TWO-PARTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COUNTIES-INCREASED-TWO-PARTY: PASS

MT02: county portions where republican_two_party_share increased

Expected: None | Calculated: 16 | Display: 16
Numerator / after operand: 16 | Denominator / before operand: 41 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-east"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "republican_two_party_share_change_pp", "op": "gt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COUNTIES-INCREASED-TWO-PARTY.json](evidence/MT02-COUNTIES-INCREASED-TWO-PARTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COUNTIES-UNCHANGED-TWO-PARTY: PASS

MT02: county portions where republican_two_party_share unchanged

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 41 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-house-east"}], "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "republican_two_party_share_change_pp", "op": "eq", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COUNTIES-UNCHANGED-TWO-PARTY.json](evidence/MT02-COUNTIES-UNCHANGED-TWO-PARTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-BIG-HORN-R-SHARE-CHANGE: PASS

MT02: BIG HORN, republican_share_change_pp

Expected: None | Calculated: -3.652579107347831 | Display: -3.7
Numerator / after operand: -3.652579107347831 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "BIG HORN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-BIG-HORN-R-SHARE-CHANGE.json](evidence/MT02-BIG-HORN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-BIG-HORN-TWO-PARTY-CHANGE: PASS

MT02: BIG HORN, republican_two_party_share_change_pp

Expected: None | Calculated: 0.013368663288870763 | Display: 0.0
Numerator / after operand: 0.013368663288870763 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "BIG HORN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-BIG-HORN-TWO-PARTY-CHANGE.json](evidence/MT02-BIG-HORN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-BLAINE-R-SHARE-CHANGE: PASS

MT02: BLAINE, republican_share_change_pp

Expected: None | Calculated: -2.7859753621226444 | Display: -2.8
Numerator / after operand: -2.7859753621226444 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "BLAINE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-BLAINE-R-SHARE-CHANGE.json](evidence/MT02-BLAINE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-BLAINE-TWO-PARTY-CHANGE: PASS

MT02: BLAINE, republican_two_party_share_change_pp

Expected: None | Calculated: 1.3062777425491445 | Display: 1.3
Numerator / after operand: 1.3062777425491445 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "BLAINE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-BLAINE-TWO-PARTY-CHANGE.json](evidence/MT02-BLAINE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-BROADWATER-R-SHARE-CHANGE: PASS

MT02: BROADWATER, republican_share_change_pp

Expected: None | Calculated: -8.436451796103706 | Display: -8.4
Numerator / after operand: -8.436451796103706 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "BROADWATER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-BROADWATER-R-SHARE-CHANGE.json](evidence/MT02-BROADWATER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-BROADWATER-TWO-PARTY-CHANGE: PASS

MT02: BROADWATER, republican_two_party_share_change_pp

Expected: None | Calculated: -0.5152352932479731 | Display: -0.5
Numerator / after operand: -0.5152352932479731 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "BROADWATER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-BROADWATER-TWO-PARTY-CHANGE.json](evidence/MT02-BROADWATER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CARBON-R-SHARE-CHANGE: PASS

MT02: CARBON, republican_share_change_pp

Expected: None | Calculated: -7.978388084835131 | Display: -8.0
Numerator / after operand: -7.978388084835131 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CARBON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CARBON-R-SHARE-CHANGE.json](evidence/MT02-CARBON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CARBON-TWO-PARTY-CHANGE: PASS

MT02: CARBON, republican_two_party_share_change_pp

Expected: None | Calculated: -1.2625020384184005 | Display: -1.3
Numerator / after operand: -1.2625020384184005 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CARBON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CARBON-TWO-PARTY-CHANGE.json](evidence/MT02-CARBON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CARTER-R-SHARE-CHANGE: PASS

MT02: CARTER, republican_share_change_pp

Expected: None | Calculated: -3.880588740748947 | Display: -3.9
Numerator / after operand: -3.880588740748947 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CARTER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CARTER-R-SHARE-CHANGE.json](evidence/MT02-CARTER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CARTER-TWO-PARTY-CHANGE: PASS

MT02: CARTER, republican_two_party_share_change_pp

Expected: None | Calculated: 1.5744787298223928 | Display: 1.6
Numerator / after operand: 1.5744787298223928 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CARTER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CARTER-TWO-PARTY-CHANGE.json](evidence/MT02-CARTER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CASCADE-R-SHARE-CHANGE: PASS

MT02: CASCADE, republican_share_change_pp

Expected: None | Calculated: -9.457211725761816 | Display: -9.5
Numerator / after operand: -9.457211725761816 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CASCADE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CASCADE-R-SHARE-CHANGE.json](evidence/MT02-CASCADE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CASCADE-TWO-PARTY-CHANGE: PASS

MT02: CASCADE, republican_two_party_share_change_pp

Expected: None | Calculated: -3.0299479300972876 | Display: -3.0
Numerator / after operand: -3.0299479300972876 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CASCADE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CASCADE-TWO-PARTY-CHANGE.json](evidence/MT02-CASCADE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CHOUTEAU-R-SHARE-CHANGE: PASS

MT02: CHOUTEAU, republican_share_change_pp

Expected: None | Calculated: -7.067756009400805 | Display: -7.1
Numerator / after operand: -7.067756009400805 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CHOUTEAU"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CHOUTEAU-R-SHARE-CHANGE.json](evidence/MT02-CHOUTEAU-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CHOUTEAU-TWO-PARTY-CHANGE: PASS

MT02: CHOUTEAU, republican_two_party_share_change_pp

Expected: None | Calculated: -1.3308591770226363 | Display: -1.3
Numerator / after operand: -1.3308591770226363 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CHOUTEAU"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CHOUTEAU-TWO-PARTY-CHANGE.json](evidence/MT02-CHOUTEAU-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CUSTER-R-SHARE-CHANGE: PASS

MT02: CUSTER, republican_share_change_pp

Expected: None | Calculated: -7.688120597524639 | Display: -7.7
Numerator / after operand: -7.688120597524639 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CUSTER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CUSTER-R-SHARE-CHANGE.json](evidence/MT02-CUSTER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-CUSTER-TWO-PARTY-CHANGE: PASS

MT02: CUSTER, republican_two_party_share_change_pp

Expected: None | Calculated: -2.327090087687489 | Display: -2.3
Numerator / after operand: -2.327090087687489 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "CUSTER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-CUSTER-TWO-PARTY-CHANGE.json](evidence/MT02-CUSTER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-DANIELS-R-SHARE-CHANGE: PASS

MT02: DANIELS, republican_share_change_pp

Expected: None | Calculated: -2.977667493796532 | Display: -3.0
Numerator / after operand: -2.977667493796532 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "DANIELS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-DANIELS-R-SHARE-CHANGE.json](evidence/MT02-DANIELS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-DANIELS-TWO-PARTY-CHANGE: PASS

MT02: DANIELS, republican_two_party_share_change_pp

Expected: None | Calculated: 1.8057733881564952 | Display: 1.8
Numerator / after operand: 1.8057733881564952 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "DANIELS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-DANIELS-TWO-PARTY-CHANGE.json](evidence/MT02-DANIELS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-DAWSON-R-SHARE-CHANGE: PASS

MT02: DAWSON, republican_share_change_pp

Expected: None | Calculated: -6.936364483171797 | Display: -6.9
Numerator / after operand: -6.936364483171797 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "DAWSON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-DAWSON-R-SHARE-CHANGE.json](evidence/MT02-DAWSON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-DAWSON-TWO-PARTY-CHANGE: PASS

MT02: DAWSON, republican_two_party_share_change_pp

Expected: None | Calculated: -1.8720536207099348 | Display: -1.9
Numerator / after operand: -1.8720536207099348 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "DAWSON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-DAWSON-TWO-PARTY-CHANGE.json](evidence/MT02-DAWSON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-FALLON-R-SHARE-CHANGE: PASS

MT02: FALLON, republican_share_change_pp

Expected: None | Calculated: -4.11540025817404 | Display: -4.1
Numerator / after operand: -4.11540025817404 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "FALLON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-FALLON-R-SHARE-CHANGE.json](evidence/MT02-FALLON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-FALLON-TWO-PARTY-CHANGE: PASS

MT02: FALLON, republican_two_party_share_change_pp

Expected: None | Calculated: 1.2412483906436456 | Display: 1.2
Numerator / after operand: 1.2412483906436456 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "FALLON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-FALLON-TWO-PARTY-CHANGE.json](evidence/MT02-FALLON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-FERGUS-R-SHARE-CHANGE: PASS

MT02: FERGUS, republican_share_change_pp

Expected: None | Calculated: -7.110045924428943 | Display: -7.1
Numerator / after operand: -7.110045924428943 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "FERGUS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-FERGUS-R-SHARE-CHANGE.json](evidence/MT02-FERGUS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-FERGUS-TWO-PARTY-CHANGE: PASS

MT02: FERGUS, republican_two_party_share_change_pp

Expected: None | Calculated: -0.8884391236220646 | Display: -0.9
Numerator / after operand: -0.8884391236220646 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "FERGUS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-FERGUS-TWO-PARTY-CHANGE.json](evidence/MT02-FERGUS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-GARFIELD-R-SHARE-CHANGE: PASS

MT02: GARFIELD, republican_share_change_pp

Expected: None | Calculated: -7.134038800705467 | Display: -7.1
Numerator / after operand: -7.134038800705467 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "GARFIELD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-GARFIELD-R-SHARE-CHANGE.json](evidence/MT02-GARFIELD-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-GARFIELD-TWO-PARTY-CHANGE: PASS

MT02: GARFIELD, republican_two_party_share_change_pp

Expected: None | Calculated: -2.076439058494528 | Display: -2.1
Numerator / after operand: -2.076439058494528 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "GARFIELD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-GARFIELD-TWO-PARTY-CHANGE.json](evidence/MT02-GARFIELD-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-GOLDEN-VALLEY-R-SHARE-CHANGE: PASS

MT02: GOLDEN VALLEY, republican_share_change_pp

Expected: None | Calculated: -4.738414507052047 | Display: -4.7
Numerator / after operand: -4.738414507052047 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "GOLDEN VALLEY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-GOLDEN-VALLEY-R-SHARE-CHANGE.json](evidence/MT02-GOLDEN-VALLEY-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-GOLDEN-VALLEY-TWO-PARTY-CHANGE: PASS

MT02: GOLDEN VALLEY, republican_two_party_share_change_pp

Expected: None | Calculated: 0.16201487591133157 | Display: 0.2
Numerator / after operand: 0.16201487591133157 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "GOLDEN VALLEY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-GOLDEN-VALLEY-TWO-PARTY-CHANGE.json](evidence/MT02-GOLDEN-VALLEY-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-HILL-R-SHARE-CHANGE: PASS

MT02: HILL, republican_share_change_pp

Expected: None | Calculated: -8.048010250035043 | Display: -8.0
Numerator / after operand: -8.048010250035043 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "HILL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-HILL-R-SHARE-CHANGE.json](evidence/MT02-HILL-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-HILL-TWO-PARTY-CHANGE: PASS

MT02: HILL, republican_two_party_share_change_pp

Expected: None | Calculated: -1.6115906670548297 | Display: -1.6
Numerator / after operand: -1.6115906670548297 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "HILL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-HILL-TWO-PARTY-CHANGE.json](evidence/MT02-HILL-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-JEFFERSON-R-SHARE-CHANGE: PASS

MT02: JEFFERSON, republican_share_change_pp

Expected: None | Calculated: -7.316725846673878 | Display: -7.3
Numerator / after operand: -7.316725846673878 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "JEFFERSON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-JEFFERSON-R-SHARE-CHANGE.json](evidence/MT02-JEFFERSON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-JEFFERSON-TWO-PARTY-CHANGE: PASS

MT02: JEFFERSON, republican_two_party_share_change_pp

Expected: None | Calculated: -0.9963173100456024 | Display: -1.0
Numerator / after operand: -0.9963173100456024 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "JEFFERSON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-JEFFERSON-TWO-PARTY-CHANGE.json](evidence/MT02-JEFFERSON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-JUDITH-BASIN-R-SHARE-CHANGE: PASS

MT02: JUDITH BASIN, republican_share_change_pp

Expected: None | Calculated: -5.954239934822459 | Display: -6.0
Numerator / after operand: -5.954239934822459 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "JUDITH BASIN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-JUDITH-BASIN-R-SHARE-CHANGE.json](evidence/MT02-JUDITH-BASIN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-JUDITH-BASIN-TWO-PARTY-CHANGE: PASS

MT02: JUDITH BASIN, republican_two_party_share_change_pp

Expected: None | Calculated: 1.9995454102672339 | Display: 2.0
Numerator / after operand: 1.9995454102672339 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "JUDITH BASIN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-JUDITH-BASIN-TWO-PARTY-CHANGE.json](evidence/MT02-JUDITH-BASIN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-LEWIS-AND-CLARK-R-SHARE-CHANGE: PASS

MT02: LEWIS AND CLARK, republican_share_change_pp

Expected: None | Calculated: -8.416020514446027 | Display: -8.4
Numerator / after operand: -8.416020514446027 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "LEWIS AND CLARK"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-LEWIS-AND-CLARK-R-SHARE-CHANGE.json](evidence/MT02-LEWIS-AND-CLARK-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-LEWIS-AND-CLARK-TWO-PARTY-CHANGE: PASS

MT02: LEWIS AND CLARK, republican_two_party_share_change_pp

Expected: None | Calculated: -2.1533270314681885 | Display: -2.2
Numerator / after operand: -2.1533270314681885 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "LEWIS AND CLARK"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-LEWIS-AND-CLARK-TWO-PARTY-CHANGE.json](evidence/MT02-LEWIS-AND-CLARK-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-LIBERTY-R-SHARE-CHANGE: PASS

MT02: LIBERTY, republican_share_change_pp

Expected: None | Calculated: -6.684770079508473 | Display: -6.7
Numerator / after operand: -6.684770079508473 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "LIBERTY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-LIBERTY-R-SHARE-CHANGE.json](evidence/MT02-LIBERTY-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-LIBERTY-TWO-PARTY-CHANGE: PASS

MT02: LIBERTY, republican_two_party_share_change_pp

Expected: None | Calculated: -1.3280784261773926 | Display: -1.3
Numerator / after operand: -1.3280784261773926 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "LIBERTY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-LIBERTY-TWO-PARTY-CHANGE.json](evidence/MT02-LIBERTY-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-MCCONE-R-SHARE-CHANGE: PASS

MT02: MCCONE, republican_share_change_pp

Expected: None | Calculated: -4.408996509213026 | Display: -4.4
Numerator / after operand: -4.408996509213026 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "MCCONE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-MCCONE-R-SHARE-CHANGE.json](evidence/MT02-MCCONE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-MCCONE-TWO-PARTY-CHANGE: PASS

MT02: MCCONE, republican_two_party_share_change_pp

Expected: None | Calculated: 1.202830188679238 | Display: 1.2
Numerator / after operand: 1.202830188679238 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "MCCONE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-MCCONE-TWO-PARTY-CHANGE.json](evidence/MT02-MCCONE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-MEAGHER-R-SHARE-CHANGE: PASS

MT02: MEAGHER, republican_share_change_pp

Expected: None | Calculated: -6.196155470353071 | Display: -6.2
Numerator / after operand: -6.196155470353071 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "MEAGHER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-MEAGHER-R-SHARE-CHANGE.json](evidence/MT02-MEAGHER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-MEAGHER-TWO-PARTY-CHANGE: PASS

MT02: MEAGHER, republican_two_party_share_change_pp

Expected: None | Calculated: 2.0760865964354336 | Display: 2.1
Numerator / after operand: 2.0760865964354336 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "MEAGHER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-MEAGHER-TWO-PARTY-CHANGE.json](evidence/MT02-MEAGHER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-MUSSELSHELL-R-SHARE-CHANGE: PASS

MT02: MUSSELSHELL, republican_share_change_pp

Expected: None | Calculated: -5.414648926530019 | Display: -5.4
Numerator / after operand: -5.414648926530019 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "MUSSELSHELL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-MUSSELSHELL-R-SHARE-CHANGE.json](evidence/MT02-MUSSELSHELL-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-MUSSELSHELL-TWO-PARTY-CHANGE: PASS

MT02: MUSSELSHELL, republican_two_party_share_change_pp

Expected: None | Calculated: -0.11913354598865888 | Display: -0.1
Numerator / after operand: -0.11913354598865888 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "MUSSELSHELL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-MUSSELSHELL-TWO-PARTY-CHANGE.json](evidence/MT02-MUSSELSHELL-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PARK-R-SHARE-CHANGE: PASS

MT02: PARK, republican_share_change_pp

Expected: None | Calculated: -7.90805401991056 | Display: -7.9
Numerator / after operand: -7.90805401991056 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PARK"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PARK-R-SHARE-CHANGE.json](evidence/MT02-PARK-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PARK-TWO-PARTY-CHANGE: PASS

MT02: PARK, republican_two_party_share_change_pp

Expected: None | Calculated: -2.21740170833995 | Display: -2.2
Numerator / after operand: -2.21740170833995 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PARK"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PARK-TWO-PARTY-CHANGE.json](evidence/MT02-PARK-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PETROLEUM-R-SHARE-CHANGE: PASS

MT02: PETROLEUM, republican_share_change_pp

Expected: None | Calculated: -2.811965811965811 | Display: -2.8
Numerator / after operand: -2.811965811965811 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PETROLEUM"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PETROLEUM-R-SHARE-CHANGE.json](evidence/MT02-PETROLEUM-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PETROLEUM-TWO-PARTY-CHANGE: PASS

MT02: PETROLEUM, republican_two_party_share_change_pp

Expected: None | Calculated: 3.4173486088379668 | Display: 3.4
Numerator / after operand: 3.4173486088379668 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PETROLEUM"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PETROLEUM-TWO-PARTY-CHANGE.json](evidence/MT02-PETROLEUM-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PHILLIPS-R-SHARE-CHANGE: PASS

MT02: PHILLIPS, republican_share_change_pp

Expected: None | Calculated: -4.580313596015184 | Display: -4.6
Numerator / after operand: -4.580313596015184 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PHILLIPS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PHILLIPS-R-SHARE-CHANGE.json](evidence/MT02-PHILLIPS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PHILLIPS-TWO-PARTY-CHANGE: PASS

MT02: PHILLIPS, republican_two_party_share_change_pp

Expected: None | Calculated: 1.2842813828372046 | Display: 1.3
Numerator / after operand: 1.2842813828372046 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PHILLIPS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PHILLIPS-TWO-PARTY-CHANGE.json](evidence/MT02-PHILLIPS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PONDERA-R-SHARE-CHANGE: PASS

MT02: PONDERA, republican_share_change_pp

Expected: None | Calculated: -7.305339057848526 | Display: -7.3
Numerator / after operand: -7.305339057848526 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PONDERA-R-SHARE-CHANGE.json](evidence/MT02-PONDERA-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PONDERA-TWO-PARTY-CHANGE: PASS

MT02: PONDERA, republican_two_party_share_change_pp

Expected: None | Calculated: -0.8673182101904486 | Display: -0.9
Numerator / after operand: -0.8673182101904486 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PONDERA-TWO-PARTY-CHANGE.json](evidence/MT02-PONDERA-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-POWDER-RIVER-R-SHARE-CHANGE: PASS

MT02: POWDER RIVER, republican_share_change_pp

Expected: None | Calculated: -6.36285188108393 | Display: -6.4
Numerator / after operand: -6.36285188108393 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "POWDER RIVER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-POWDER-RIVER-R-SHARE-CHANGE.json](evidence/MT02-POWDER-RIVER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-POWDER-RIVER-TWO-PARTY-CHANGE: PASS

MT02: POWDER RIVER, republican_two_party_share_change_pp

Expected: None | Calculated: -0.005216413103636963 | Display: -0.0
Numerator / after operand: -0.005216413103636963 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "POWDER RIVER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-POWDER-RIVER-TWO-PARTY-CHANGE.json](evidence/MT02-POWDER-RIVER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PRAIRIE-R-SHARE-CHANGE: PASS

MT02: PRAIRIE, republican_share_change_pp

Expected: None | Calculated: -5.546279417696831 | Display: -5.5
Numerator / after operand: -5.546279417696831 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PRAIRIE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PRAIRIE-R-SHARE-CHANGE.json](evidence/MT02-PRAIRIE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PRAIRIE-TWO-PARTY-CHANGE: PASS

MT02: PRAIRIE, republican_two_party_share_change_pp

Expected: None | Calculated: -0.27372984173289483 | Display: -0.3
Numerator / after operand: -0.27372984173289483 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PRAIRIE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PRAIRIE-TWO-PARTY-CHANGE.json](evidence/MT02-PRAIRIE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-RICHLAND-R-SHARE-CHANGE: PASS

MT02: RICHLAND, republican_share_change_pp

Expected: None | Calculated: -7.177359672139194 | Display: -7.2
Numerator / after operand: -7.177359672139194 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "RICHLAND"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-RICHLAND-R-SHARE-CHANGE.json](evidence/MT02-RICHLAND-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-RICHLAND-TWO-PARTY-CHANGE: PASS

MT02: RICHLAND, republican_two_party_share_change_pp

Expected: None | Calculated: -1.5184734508607134 | Display: -1.5
Numerator / after operand: -1.5184734508607134 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "RICHLAND"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-RICHLAND-TWO-PARTY-CHANGE.json](evidence/MT02-RICHLAND-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-ROOSEVELT-R-SHARE-CHANGE: PASS

MT02: ROOSEVELT, republican_share_change_pp

Expected: None | Calculated: -3.4115518970733505 | Display: -3.4
Numerator / after operand: -3.4115518970733505 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "ROOSEVELT"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-ROOSEVELT-R-SHARE-CHANGE.json](evidence/MT02-ROOSEVELT-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-ROOSEVELT-TWO-PARTY-CHANGE: PASS

MT02: ROOSEVELT, republican_two_party_share_change_pp

Expected: None | Calculated: -0.10423279384463857 | Display: -0.1
Numerator / after operand: -0.10423279384463857 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "ROOSEVELT"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-ROOSEVELT-TWO-PARTY-CHANGE.json](evidence/MT02-ROOSEVELT-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-ROSEBUD-R-SHARE-CHANGE: PASS

MT02: ROSEBUD, republican_share_change_pp

Expected: None | Calculated: -2.1992333696860045 | Display: -2.2
Numerator / after operand: -2.1992333696860045 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "ROSEBUD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-ROSEBUD-R-SHARE-CHANGE.json](evidence/MT02-ROSEBUD-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-ROSEBUD-TWO-PARTY-CHANGE: PASS

MT02: ROSEBUD, republican_two_party_share_change_pp

Expected: None | Calculated: 2.8257565274821927 | Display: 2.8
Numerator / after operand: 2.8257565274821927 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "ROSEBUD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-ROSEBUD-TWO-PARTY-CHANGE.json](evidence/MT02-ROSEBUD-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-SHERIDAN-R-SHARE-CHANGE: PASS

MT02: SHERIDAN, republican_share_change_pp

Expected: None | Calculated: -6.419818011723521 | Display: -6.4
Numerator / after operand: -6.419818011723521 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "SHERIDAN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-SHERIDAN-R-SHARE-CHANGE.json](evidence/MT02-SHERIDAN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-SHERIDAN-TWO-PARTY-CHANGE: PASS

MT02: SHERIDAN, republican_two_party_share_change_pp

Expected: None | Calculated: -0.41347905069356594 | Display: -0.4
Numerator / after operand: -0.41347905069356594 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "SHERIDAN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-SHERIDAN-TWO-PARTY-CHANGE.json](evidence/MT02-SHERIDAN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-STILLWATER-R-SHARE-CHANGE: PASS

MT02: STILLWATER, republican_share_change_pp

Expected: None | Calculated: -6.495988231813843 | Display: -6.5
Numerator / after operand: -6.495988231813843 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "STILLWATER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-STILLWATER-R-SHARE-CHANGE.json](evidence/MT02-STILLWATER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-STILLWATER-TWO-PARTY-CHANGE: PASS

MT02: STILLWATER, republican_two_party_share_change_pp

Expected: None | Calculated: -0.14852825689214422 | Display: -0.1
Numerator / after operand: -0.14852825689214422 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "STILLWATER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-STILLWATER-TWO-PARTY-CHANGE.json](evidence/MT02-STILLWATER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-SWEET-GRASS-R-SHARE-CHANGE: PASS

MT02: SWEET GRASS, republican_share_change_pp

Expected: None | Calculated: -7.040626569837638 | Display: -7.0
Numerator / after operand: -7.040626569837638 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "SWEET GRASS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-SWEET-GRASS-R-SHARE-CHANGE.json](evidence/MT02-SWEET-GRASS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-SWEET-GRASS-TWO-PARTY-CHANGE: PASS

MT02: SWEET GRASS, republican_two_party_share_change_pp

Expected: None | Calculated: -1.0485087125345127 | Display: -1.0
Numerator / after operand: -1.0485087125345127 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "SWEET GRASS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-SWEET-GRASS-TWO-PARTY-CHANGE.json](evidence/MT02-SWEET-GRASS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TETON-R-SHARE-CHANGE: PASS

MT02: TETON, republican_share_change_pp

Expected: None | Calculated: -5.384896929386452 | Display: -5.4
Numerator / after operand: -5.384896929386452 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "TETON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TETON-R-SHARE-CHANGE.json](evidence/MT02-TETON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TETON-TWO-PARTY-CHANGE: PASS

MT02: TETON, republican_two_party_share_change_pp

Expected: None | Calculated: 2.147909617521515 | Display: 2.1
Numerator / after operand: 2.147909617521515 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "TETON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TETON-TWO-PARTY-CHANGE.json](evidence/MT02-TETON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TOOLE-R-SHARE-CHANGE: PASS

MT02: TOOLE, republican_share_change_pp

Expected: None | Calculated: -5.445629562069476 | Display: -5.4
Numerator / after operand: -5.445629562069476 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "TOOLE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TOOLE-R-SHARE-CHANGE.json](evidence/MT02-TOOLE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TOOLE-TWO-PARTY-CHANGE: PASS

MT02: TOOLE, republican_two_party_share_change_pp

Expected: None | Calculated: -0.3077149440047 | Display: -0.3
Numerator / after operand: -0.3077149440047 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "TOOLE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TOOLE-TWO-PARTY-CHANGE.json](evidence/MT02-TOOLE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TREASURE-R-SHARE-CHANGE: PASS

MT02: TREASURE, republican_share_change_pp

Expected: None | Calculated: -2.4242424242424288 | Display: -2.4
Numerator / after operand: -2.4242424242424288 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "TREASURE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TREASURE-R-SHARE-CHANGE.json](evidence/MT02-TREASURE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TREASURE-TWO-PARTY-CHANGE: PASS

MT02: TREASURE, republican_two_party_share_change_pp

Expected: None | Calculated: 2.789621882542226 | Display: 2.8
Numerator / after operand: 2.789621882542226 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "TREASURE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TREASURE-TWO-PARTY-CHANGE.json](evidence/MT02-TREASURE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-VALLEY-R-SHARE-CHANGE: PASS

MT02: VALLEY, republican_share_change_pp

Expected: None | Calculated: -5.557593906332037 | Display: -5.6
Numerator / after operand: -5.557593906332037 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "VALLEY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-VALLEY-R-SHARE-CHANGE.json](evidence/MT02-VALLEY-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-VALLEY-TWO-PARTY-CHANGE: PASS

MT02: VALLEY, republican_two_party_share_change_pp

Expected: None | Calculated: 1.122512786801133 | Display: 1.1
Numerator / after operand: 1.122512786801133 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "VALLEY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-VALLEY-TWO-PARTY-CHANGE.json](evidence/MT02-VALLEY-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-WHEATLAND-R-SHARE-CHANGE: PASS

MT02: WHEATLAND, republican_share_change_pp

Expected: None | Calculated: -5.762895702902526 | Display: -5.8
Numerator / after operand: -5.762895702902526 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "WHEATLAND"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-WHEATLAND-R-SHARE-CHANGE.json](evidence/MT02-WHEATLAND-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-WHEATLAND-TWO-PARTY-CHANGE: PASS

MT02: WHEATLAND, republican_two_party_share_change_pp

Expected: None | Calculated: -0.7718073290359784 | Display: -0.8
Numerator / after operand: -0.7718073290359784 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "WHEATLAND"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-WHEATLAND-TWO-PARTY-CHANGE.json](evidence/MT02-WHEATLAND-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-WIBAUX-R-SHARE-CHANGE: PASS

MT02: WIBAUX, republican_share_change_pp

Expected: None | Calculated: -7.291503289555146 | Display: -7.3
Numerator / after operand: -7.291503289555146 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "WIBAUX"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-WIBAUX-R-SHARE-CHANGE.json](evidence/MT02-WIBAUX-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-WIBAUX-TWO-PARTY-CHANGE: PASS

MT02: WIBAUX, republican_two_party_share_change_pp

Expected: None | Calculated: 0.3138538906124255 | Display: 0.3
Numerator / after operand: 0.3138538906124255 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "WIBAUX"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-WIBAUX-TWO-PARTY-CHANGE.json](evidence/MT02-WIBAUX-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-YELLOWSTONE-R-SHARE-CHANGE: PASS

MT02: YELLOWSTONE, republican_share_change_pp

Expected: None | Calculated: -8.611698477187124 | Display: -8.6
Numerator / after operand: -8.611698477187124 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "YELLOWSTONE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-YELLOWSTONE-R-SHARE-CHANGE.json](evidence/MT02-YELLOWSTONE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-YELLOWSTONE-TWO-PARTY-CHANGE: PASS

MT02: YELLOWSTONE, republican_two_party_share_change_pp

Expected: None | Calculated: -2.6493929621203782 | Display: -2.6
Numerator / after operand: -2.6493929621203782 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "YELLOWSTONE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-YELLOWSTONE-TWO-PARTY-CHANGE.json](evidence/MT02-YELLOWSTONE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## SENATE-R-SHARE-2024: PASS

SENATE: R share of all candidate votes, 2024 (%)

Expected: None | Calculated: 52.6431754333385 | Display: 52.6
Numerator / after operand: 319682 | Denominator / before operand: 607262 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-R-SHARE-2024.json](evidence/SENATE-R-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-R-VOTES-2024: PASS

SENATE: R votes, 2024

Expected: None | Calculated: 319682 | Display: 319682
Numerator / after operand: 319682 | Denominator / before operand: 607262 (eligible rows or contest votes)

Calculation: `{"column": "republican_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-R-VOTES-2024.json](evidence/SENATE-R-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-D-SHARE-2024: PASS

SENATE: D share of all candidate votes, 2024 (%)

Expected: None | Calculated: 45.5001300921184 | Display: 45.5
Numerator / after operand: 276305 | Denominator / before operand: 607262 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-D-SHARE-2024.json](evidence/SENATE-D-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-D-VOTES-2024: PASS

SENATE: D votes, 2024

Expected: None | Calculated: 276305 | Display: 276305
Numerator / after operand: 276305 | Denominator / before operand: 607262 (eligible rows or contest votes)

Calculation: `{"column": "democratic_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-D-VOTES-2024.json](evidence/SENATE-D-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-L-SHARE-2024: PASS

SENATE: L share of all candidate votes, 2024 (%)

Expected: None | Calculated: 1.1975061834924627 | Display: 1.2
Numerator / after operand: 7272 | Denominator / before operand: 607262 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "libertarian_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-L-SHARE-2024.json](evidence/SENATE-L-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-L-VOTES-2024: PASS

SENATE: L votes, 2024

Expected: None | Calculated: 7272 | Display: 7272
Numerator / after operand: 7272 | Denominator / before operand: 607262 (eligible rows or contest votes)

Calculation: `{"column": "libertarian_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-L-VOTES-2024.json](evidence/SENATE-L-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-I-SHARE-2024: PASS

SENATE: I share of all candidate votes, 2024 (%)

Expected: None | Calculated: 0.0 | Display: 0.0
Numerator / after operand: 0 | Denominator / before operand: 607262 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "independent_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-I-SHARE-2024.json](evidence/SENATE-I-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-I-VOTES-2024: PASS

SENATE: I votes, 2024

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 607262 (eligible rows or contest votes)

Calculation: `{"column": "independent_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-I-VOTES-2024.json](evidence/SENATE-I-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOTAL-VOTES-2024: PASS

SENATE: total candidate votes, 2024

Expected: None | Calculated: 607262 | Display: 607262
Numerator / after operand: 607262 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-TOTAL-VOTES-2024.json](evidence/SENATE-TOTAL-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-R-MARGIN-2024: PASS

SENATE: Republican-minus-Democratic margin, 2024 (pp)

Expected: None | Calculated: 7.1430453412201 | Display: 7.1
Numerator / after operand: 43377 | Denominator / before operand: 607262 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "republican_minus_democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-R-MARGIN-2024.json](evidence/SENATE-R-MARGIN-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-R-TWO-PARTY-2024: PASS

SENATE: Republican two-party share, 2024 (%)

Expected: None | Calculated: 53.639089443226105 | Display: 53.6
Numerator / after operand: 319682 | Denominator / before operand: 595987 (eligible rows or contest votes)

Calculation: `{"denominator_column": "two_party_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-R-TWO-PARTY-2024.json](evidence/SENATE-R-TWO-PARTY-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-R-SHARE-2026: PASS

SENATE: R share of all candidate votes, 2026 (%)

Expected: None | Calculated: 48.17247771675704 | Display: 48.2
Numerator / after operand: 235693 | Denominator / before operand: 489269 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-R-SHARE-2026.json](evidence/SENATE-R-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-R-VOTES-2026: PASS

SENATE: R votes, 2026

Expected: None | Calculated: 235693 | Display: 235693
Numerator / after operand: 235693 | Denominator / before operand: 489269 (eligible rows or contest votes)

Calculation: `{"column": "republican_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-R-VOTES-2026.json](evidence/SENATE-R-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-D-SHARE-2026: PASS

SENATE: D share of all candidate votes, 2026 (%)

Expected: None | Calculated: 12.259922455745203 | Display: 12.3
Numerator / after operand: 59984 | Denominator / before operand: 489269 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-D-SHARE-2026.json](evidence/SENATE-D-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-D-VOTES-2026: PASS

SENATE: D votes, 2026

Expected: None | Calculated: 59984 | Display: 59984
Numerator / after operand: 59984 | Denominator / before operand: 489269 (eligible rows or contest votes)

Calculation: `{"column": "democratic_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-D-VOTES-2026.json](evidence/SENATE-D-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-L-SHARE-2026: PASS

SENATE: L share of all candidate votes, 2026 (%)

Expected: None | Calculated: 1.8431578538595332 | Display: 1.8
Numerator / after operand: 9018 | Denominator / before operand: 489269 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "libertarian_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-L-SHARE-2026.json](evidence/SENATE-L-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-L-VOTES-2026: PASS

SENATE: L votes, 2026

Expected: None | Calculated: 9018 | Display: 9018
Numerator / after operand: 9018 | Denominator / before operand: 489269 (eligible rows or contest votes)

Calculation: `{"column": "libertarian_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-L-VOTES-2026.json](evidence/SENATE-L-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-I-SHARE-2026: PASS

SENATE: I share of all candidate votes, 2026 (%)

Expected: None | Calculated: 37.72444197363822 | Display: 37.7
Numerator / after operand: 184574 | Denominator / before operand: 489269 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "independent_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-I-SHARE-2026.json](evidence/SENATE-I-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-I-VOTES-2026: PASS

SENATE: I votes, 2026

Expected: None | Calculated: 184574 | Display: 184574
Numerator / after operand: 184574 | Denominator / before operand: 489269 (eligible rows or contest votes)

Calculation: `{"column": "independent_votes", "denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-I-VOTES-2026.json](evidence/SENATE-I-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOTAL-VOTES-2026: PASS

SENATE: total candidate votes, 2026

Expected: None | Calculated: 489269 | Display: 489269
Numerator / after operand: 489269 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "operation": "sum", "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TOTAL-VOTES-2026.json](evidence/SENATE-TOTAL-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-R-MARGIN-2026: PASS

SENATE: Republican-minus-Democratic margin, 2026 (pp)

Expected: None | Calculated: 35.91255526101184 | Display: 35.9
Numerator / after operand: 175709 | Denominator / before operand: 489269 (eligible rows or contest votes)

Calculation: `{"denominator_column": "total_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "republican_minus_democratic_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-R-MARGIN-2026.json](evidence/SENATE-R-MARGIN-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-R-TWO-PARTY-2026: PASS

SENATE: Republican two-party share, 2026 (%)

Expected: None | Calculated: 79.71299762916966 | Display: 79.7
Numerator / after operand: 235693 | Denominator / before operand: 295677 (eligible rows or contest votes)

Calculation: `{"denominator_column": "two_party_votes", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}], "numerator_column": "republican_votes", "operation": "ratio", "scale": 100, "table": "district-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-R-TWO-PARTY-2026.json](evidence/SENATE-R-TWO-PARTY-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-R-SHARE-CHANGE: PASS

SENATE: 2024–26 change in republican_share (pp)

Expected: None | Calculated: -4.470697716581457 | Display: -4.5
Numerator / after operand: 0.4817247771675704 | Denominator / before operand: 0.526431754333385 (before value)

Calculation: `{"after_column": "republican_share_2026", "before_column": "republican_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}], "operation": "difference", "scale": 100, "table": "district-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-R-SHARE-CHANGE.json](evidence/SENATE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MARGIN-CHANGE: PASS

SENATE: 2024–26 change in republican_margin (pp)

Expected: None | Calculated: 28.769509919791737 | Display: 28.8
Numerator / after operand: 0.35912555261011836 | Denominator / before operand: 0.071430453412201 (before value)

Calculation: `{"after_column": "republican_margin_2026", "before_column": "republican_margin_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}], "operation": "difference", "scale": 100, "table": "district-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MARGIN-CHANGE.json](evidence/SENATE-MARGIN-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TWO-PARTY-CHANGE: PASS

SENATE: 2024–26 change in republican_two_party_share (pp)

Expected: None | Calculated: 26.073908185943562 | Display: 26.1
Numerator / after operand: 0.7971299762916967 | Denominator / before operand: 0.5363908944322611 (before value)

Calculation: `{"after_column": "republican_two_party_share_2026", "before_column": "republican_two_party_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}], "operation": "difference", "scale": 100, "table": "district-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TWO-PARTY-CHANGE.json](evidence/SENATE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COUNTIES-DECLINED: PASS

SENATE: county portions where republican_share declined

Expected: 48 | Calculated: 48 | Display: 48
Numerator / after operand: 48 | Denominator / before operand: 56 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-senate"}], "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "republican_share_change_pp", "op": "lt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COUNTIES-DECLINED.json](evidence/SENATE-COUNTIES-DECLINED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COUNTIES-INCREASED: PASS

SENATE: county portions where republican_share increased

Expected: 8 | Calculated: 8 | Display: 8
Numerator / after operand: 8 | Denominator / before operand: 56 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-senate"}], "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "republican_share_change_pp", "op": "gt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COUNTIES-INCREASED.json](evidence/SENATE-COUNTIES-INCREASED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COUNTIES-UNCHANGED: PASS

SENATE: county portions where republican_share unchanged

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 56 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-senate"}], "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "republican_share_change_pp", "op": "eq", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COUNTIES-UNCHANGED.json](evidence/SENATE-COUNTIES-UNCHANGED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COUNTIES-DECLINED-TWO-PARTY: PASS

SENATE: county portions where republican_two_party_share declined

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 56 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-senate"}], "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "republican_two_party_share_change_pp", "op": "lt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COUNTIES-DECLINED-TWO-PARTY.json](evidence/SENATE-COUNTIES-DECLINED-TWO-PARTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COUNTIES-INCREASED-TWO-PARTY: PASS

SENATE: county portions where republican_two_party_share increased

Expected: None | Calculated: 56 | Display: 56
Numerator / after operand: 56 | Denominator / before operand: 56 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-senate"}], "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "republican_two_party_share_change_pp", "op": "gt", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COUNTIES-INCREASED-TWO-PARTY.json](evidence/SENATE-COUNTIES-INCREASED-TWO-PARTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COUNTIES-UNCHANGED-TWO-PARTY: PASS

SENATE: county portions where republican_two_party_share unchanged

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 56 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "race", "op": "eq", "value": "us-senate"}], "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "republican_two_party_share_change_pp", "op": "eq", "value": 0}], "operation": "count", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COUNTIES-UNCHANGED-TWO-PARTY.json](evidence/SENATE-COUNTIES-UNCHANGED-TWO-PARTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BEAVERHEAD-R-SHARE-CHANGE: PASS

SENATE: BEAVERHEAD, republican_share_change_pp

Expected: None | Calculated: -1.5582962483598028 | Display: -1.6
Numerator / after operand: -1.5582962483598028 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "BEAVERHEAD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BEAVERHEAD-R-SHARE-CHANGE.json](evidence/SENATE-BEAVERHEAD-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BEAVERHEAD-TWO-PARTY-CHANGE: PASS

SENATE: BEAVERHEAD, republican_two_party_share_change_pp

Expected: None | Calculated: 23.468804250396 | Display: 23.5
Numerator / after operand: 23.468804250396 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "BEAVERHEAD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BEAVERHEAD-TWO-PARTY-CHANGE.json](evidence/SENATE-BEAVERHEAD-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BEAVERHEAD-R-2024: PASS

BEAVERHEAD: republican_share in 2024 (%)

Expected: None | Calculated: 63.465160075329564 | Display: 63.5
Numerator / after operand: 0.6346516007532956 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "BEAVERHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-BEAVERHEAD-R-2024.json](evidence/SENATE-BEAVERHEAD-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BEAVERHEAD-JON-TESTER-2024: PASS

BEAVERHEAD: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 34.65160075329567 | Display: 34.7
Numerator / after operand: 0.3465160075329567 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "BEAVERHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-BEAVERHEAD-JON-TESTER-2024.json](evidence/SENATE-BEAVERHEAD-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BEAVERHEAD-R-2026: PASS

BEAVERHEAD: republican_share in 2026 (%)

Expected: None | Calculated: 61.90686382696976 | Display: 61.9
Numerator / after operand: 0.6190686382696976 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BEAVERHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BEAVERHEAD-R-2026.json](evidence/SENATE-BEAVERHEAD-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BEAVERHEAD-SETH-BODNAR-2026: PASS

BEAVERHEAD: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 28.18362392407857 | Display: 28.2
Numerator / after operand: 0.2818362392407857 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BEAVERHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BEAVERHEAD-SETH-BODNAR-2026.json](evidence/SENATE-BEAVERHEAD-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BEAVERHEAD-ALANI-BANKHEAD-2026: PASS

BEAVERHEAD: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 8.320459059810197 | Display: 8.3
Numerator / after operand: 0.08320459059810197 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BEAVERHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BEAVERHEAD-ALANI-BANKHEAD-2026.json](evidence/SENATE-BEAVERHEAD-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BIG-HORN-R-SHARE-CHANGE: PASS

SENATE: BIG HORN, republican_share_change_pp

Expected: None | Calculated: 1.6636161116420134 | Display: 1.7
Numerator / after operand: 1.6636161116420134 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "BIG HORN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BIG-HORN-R-SHARE-CHANGE.json](evidence/SENATE-BIG-HORN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BIG-HORN-TWO-PARTY-CHANGE: PASS

SENATE: BIG HORN, republican_two_party_share_change_pp

Expected: None | Calculated: 20.48791597649084 | Display: 20.5
Numerator / after operand: 20.48791597649084 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "BIG HORN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BIG-HORN-TWO-PARTY-CHANGE.json](evidence/SENATE-BIG-HORN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BIG-HORN-R-2024: PASS

BIG HORN: republican_share in 2024 (%)

Expected: None | Calculated: 35.481697731866156 | Display: 35.5
Numerator / after operand: 0.3548169773186616 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "BIG HORN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-BIG-HORN-R-2024.json](evidence/SENATE-BIG-HORN-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BIG-HORN-JON-TESTER-2024: PASS

BIG HORN: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 62.99124185942061 | Display: 63.0
Numerator / after operand: 0.6299124185942061 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "BIG HORN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-BIG-HORN-JON-TESTER-2024.json](evidence/SENATE-BIG-HORN-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BIG-HORN-R-2026: PASS

BIG HORN: republican_share in 2026 (%)

Expected: None | Calculated: 37.14531384350817 | Display: 37.1
Numerator / after operand: 0.3714531384350817 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BIG HORN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BIG-HORN-R-2026.json](evidence/SENATE-BIG-HORN-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BIG-HORN-SETH-BODNAR-2026: PASS

BIG HORN: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 31.785611923187158 | Display: 31.8
Numerator / after operand: 0.31785611923187157 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BIG HORN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BIG-HORN-SETH-BODNAR-2026.json](evidence/SENATE-BIG-HORN-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BIG-HORN-ALANI-BANKHEAD-2026: PASS

BIG HORN: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 28.575523072513615 | Display: 28.6
Numerator / after operand: 0.28575523072513614 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BIG HORN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BIG-HORN-ALANI-BANKHEAD-2026.json](evidence/SENATE-BIG-HORN-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BLAINE-R-SHARE-CHANGE: PASS

SENATE: BLAINE, republican_share_change_pp

Expected: None | Calculated: 4.928564541543773 | Display: 4.9
Numerator / after operand: 4.928564541543773 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "BLAINE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BLAINE-R-SHARE-CHANGE.json](evidence/SENATE-BLAINE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BLAINE-TWO-PARTY-CHANGE: PASS

SENATE: BLAINE, republican_two_party_share_change_pp

Expected: None | Calculated: 25.918647188766027 | Display: 25.9
Numerator / after operand: 25.918647188766027 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "BLAINE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BLAINE-TWO-PARTY-CHANGE.json](evidence/SENATE-BLAINE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BLAINE-R-2024: PASS

BLAINE: republican_share in 2024 (%)

Expected: None | Calculated: 38.9924762839385 | Display: 39.0
Numerator / after operand: 0.38992476283938504 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "BLAINE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-BLAINE-R-2024.json](evidence/SENATE-BLAINE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BLAINE-JON-TESTER-2024: PASS

BLAINE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 59.33922145894668 | Display: 59.3
Numerator / after operand: 0.5933922145894668 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "BLAINE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-BLAINE-JON-TESTER-2024.json](evidence/SENATE-BLAINE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BLAINE-R-2026: PASS

BLAINE: republican_share in 2026 (%)

Expected: None | Calculated: 43.92104082548228 | Display: 43.9
Numerator / after operand: 0.43921040825482277 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BLAINE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BLAINE-R-2026.json](evidence/SENATE-BLAINE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BLAINE-SETH-BODNAR-2026: PASS

BLAINE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 30.82099596231494 | Display: 30.8
Numerator / after operand: 0.3082099596231494 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BLAINE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BLAINE-SETH-BODNAR-2026.json](evidence/SENATE-BLAINE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BLAINE-ALANI-BANKHEAD-2026: PASS

BLAINE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 23.059668012561687 | Display: 23.1
Numerator / after operand: 0.23059668012561688 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BLAINE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BLAINE-ALANI-BANKHEAD-2026.json](evidence/SENATE-BLAINE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BROADWATER-R-SHARE-CHANGE: PASS

SENATE: BROADWATER, republican_share_change_pp

Expected: None | Calculated: -4.626651878150412 | Display: -4.6
Numerator / after operand: -4.626651878150412 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "BROADWATER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BROADWATER-R-SHARE-CHANGE.json](evidence/SENATE-BROADWATER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BROADWATER-TWO-PARTY-CHANGE: PASS

SENATE: BROADWATER, republican_two_party_share_change_pp

Expected: None | Calculated: 17.615042210472666 | Display: 17.6
Numerator / after operand: 17.615042210472666 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "BROADWATER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BROADWATER-TWO-PARTY-CHANGE.json](evidence/SENATE-BROADWATER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BROADWATER-R-2024: PASS

BROADWATER: republican_share in 2024 (%)

Expected: None | Calculated: 72.34613795952086 | Display: 72.3
Numerator / after operand: 0.7234613795952086 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "BROADWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-BROADWATER-R-2024.json](evidence/SENATE-BROADWATER-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BROADWATER-JON-TESTER-2024: PASS

BROADWATER: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 25.1755472945064 | Display: 25.2
Numerator / after operand: 0.251755472945064 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "BROADWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-BROADWATER-JON-TESTER-2024.json](evidence/SENATE-BROADWATER-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BROADWATER-R-2026: PASS

BROADWATER: republican_share in 2026 (%)

Expected: None | Calculated: 67.71948608137045 | Display: 67.7
Numerator / after operand: 0.6771948608137045 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BROADWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BROADWATER-R-2026.json](evidence/SENATE-BROADWATER-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BROADWATER-SETH-BODNAR-2026: PASS

BROADWATER: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 23.5813704496788 | Display: 23.6
Numerator / after operand: 0.235813704496788 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BROADWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BROADWATER-SETH-BODNAR-2026.json](evidence/SENATE-BROADWATER-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BROADWATER-ALANI-BANKHEAD-2026: PASS

BROADWATER: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 6.049250535331906 | Display: 6.0
Numerator / after operand: 0.06049250535331906 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "BROADWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BROADWATER-ALANI-BANKHEAD-2026.json](evidence/SENATE-BROADWATER-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARBON-R-SHARE-CHANGE: PASS

SENATE: CARBON, republican_share_change_pp

Expected: None | Calculated: -5.943581199802783 | Display: -5.9
Numerator / after operand: -5.943581199802783 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CARBON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARBON-R-SHARE-CHANGE.json](evidence/SENATE-CARBON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARBON-TWO-PARTY-CHANGE: PASS

SENATE: CARBON, republican_two_party_share_change_pp

Expected: None | Calculated: 22.858430084401725 | Display: 22.9
Numerator / after operand: 22.858430084401725 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CARBON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARBON-TWO-PARTY-CHANGE.json](evidence/SENATE-CARBON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARBON-R-2024: PASS

CARBON: republican_share in 2024 (%)

Expected: None | Calculated: 60.35462912831618 | Display: 60.4
Numerator / after operand: 0.6035462912831618 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CARBON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CARBON-R-2024.json](evidence/SENATE-CARBON-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARBON-JON-TESTER-2024: PASS

CARBON: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 37.81808337845155 | Display: 37.8
Numerator / after operand: 0.37818083378451545 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CARBON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CARBON-JON-TESTER-2024.json](evidence/SENATE-CARBON-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARBON-R-2026: PASS

CARBON: republican_share in 2026 (%)

Expected: None | Calculated: 54.4110479285134 | Display: 54.4
Numerator / after operand: 0.544110479285134 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CARBON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARBON-R-2026.json](evidence/SENATE-CARBON-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARBON-SETH-BODNAR-2026: PASS

CARBON: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 33.19252640129975 | Display: 33.2
Numerator / after operand: 0.33192526401299755 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CARBON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARBON-SETH-BODNAR-2026.json](evidence/SENATE-CARBON-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARBON-ALANI-BANKHEAD-2026: PASS

CARBON: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 10.105605199025183 | Display: 10.1
Numerator / after operand: 0.10105605199025183 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CARBON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARBON-ALANI-BANKHEAD-2026.json](evidence/SENATE-CARBON-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARTER-R-SHARE-CHANGE: PASS

SENATE: CARTER, republican_share_change_pp

Expected: None | Calculated: -4.18470418470418 | Display: -4.2
Numerator / after operand: -4.18470418470418 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CARTER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARTER-R-SHARE-CHANGE.json](evidence/SENATE-CARTER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARTER-TWO-PARTY-CHANGE: PASS

SENATE: CARTER, republican_two_party_share_change_pp

Expected: None | Calculated: 9.0491963729606 | Display: 9.0
Numerator / after operand: 9.0491963729606 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CARTER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARTER-TWO-PARTY-CHANGE.json](evidence/SENATE-CARTER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARTER-R-2024: PASS

CARTER: republican_share in 2024 (%)

Expected: None | Calculated: 85.71428571428571 | Display: 85.7
Numerator / after operand: 0.8571428571428571 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CARTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CARTER-R-2024.json](evidence/SENATE-CARTER-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARTER-JON-TESTER-2024: PASS

CARTER: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 12.763466042154567 | Display: 12.8
Numerator / after operand: 0.12763466042154567 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CARTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CARTER-JON-TESTER-2024.json](evidence/SENATE-CARTER-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARTER-R-2026: PASS

CARTER: republican_share in 2026 (%)

Expected: None | Calculated: 81.52958152958153 | Display: 81.5
Numerator / after operand: 0.8152958152958153 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CARTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARTER-R-2026.json](evidence/SENATE-CARTER-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARTER-SETH-BODNAR-2026: PASS

CARTER: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 12.121212121212121 | Display: 12.1
Numerator / after operand: 0.12121212121212122 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CARTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARTER-SETH-BODNAR-2026.json](evidence/SENATE-CARTER-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARTER-ALANI-BANKHEAD-2026: PASS

CARTER: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 3.318903318903319 | Display: 3.3
Numerator / after operand: 0.03318903318903319 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CARTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARTER-ALANI-BANKHEAD-2026.json](evidence/SENATE-CARTER-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CASCADE-R-SHARE-CHANGE: PASS

SENATE: CASCADE, republican_share_change_pp

Expected: None | Calculated: -4.181646743461398 | Display: -4.2
Numerator / after operand: -4.181646743461398 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CASCADE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CASCADE-R-SHARE-CHANGE.json](evidence/SENATE-CASCADE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CASCADE-TWO-PARTY-CHANGE: PASS

SENATE: CASCADE, republican_two_party_share_change_pp

Expected: None | Calculated: 23.98924789147616 | Display: 24.0
Numerator / after operand: 23.98924789147616 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CASCADE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CASCADE-TWO-PARTY-CHANGE.json](evidence/SENATE-CASCADE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CASCADE-R-2024: PASS

CASCADE: republican_share in 2024 (%)

Expected: None | Calculated: 52.295588351770206 | Display: 52.3
Numerator / after operand: 0.5229558835177021 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CASCADE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CASCADE-R-2024.json](evidence/SENATE-CASCADE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CASCADE-JON-TESTER-2024: PASS

CASCADE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 45.734878686273994 | Display: 45.7
Numerator / after operand: 0.45734878686273994 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CASCADE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CASCADE-JON-TESTER-2024.json](evidence/SENATE-CASCADE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CASCADE-R-2026: PASS

CASCADE: republican_share in 2026 (%)

Expected: None | Calculated: 48.11394160830881 | Display: 48.1
Numerator / after operand: 0.4811394160830881 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CASCADE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CASCADE-R-2026.json](evidence/SENATE-CASCADE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CASCADE-SETH-BODNAR-2026: PASS

CASCADE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 36.04316790148517 | Display: 36.0
Numerator / after operand: 0.3604316790148517 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CASCADE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CASCADE-SETH-BODNAR-2026.json](evidence/SENATE-CASCADE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CASCADE-ALANI-BANKHEAD-2026: PASS

CASCADE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 14.100612334652729 | Display: 14.1
Numerator / after operand: 0.1410061233465273 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CASCADE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CASCADE-ALANI-BANKHEAD-2026.json](evidence/SENATE-CASCADE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CHOUTEAU-R-SHARE-CHANGE: PASS

SENATE: CHOUTEAU, republican_share_change_pp

Expected: None | Calculated: -0.2098680125911967 | Display: -0.2
Numerator / after operand: -0.2098680125911967 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CHOUTEAU"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CHOUTEAU-R-SHARE-CHANGE.json](evidence/SENATE-CHOUTEAU-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CHOUTEAU-TWO-PARTY-CHANGE: PASS

SENATE: CHOUTEAU, republican_two_party_share_change_pp

Expected: None | Calculated: 26.158668701168043 | Display: 26.2
Numerator / after operand: 26.158668701168043 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CHOUTEAU"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CHOUTEAU-TWO-PARTY-CHANGE.json](evidence/SENATE-CHOUTEAU-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CHOUTEAU-R-2024: PASS

CHOUTEAU: republican_share in 2024 (%)

Expected: None | Calculated: 55.488010807159746 | Display: 55.5
Numerator / after operand: 0.5548801080715975 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CHOUTEAU"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CHOUTEAU-R-2024.json](evidence/SENATE-CHOUTEAU-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CHOUTEAU-JON-TESTER-2024: PASS

CHOUTEAU: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 43.02600472813239 | Display: 43.0
Numerator / after operand: 0.4302600472813239 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CHOUTEAU"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CHOUTEAU-JON-TESTER-2024.json](evidence/SENATE-CHOUTEAU-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CHOUTEAU-R-2026: PASS

CHOUTEAU: republican_share in 2026 (%)

Expected: None | Calculated: 55.27814279456855 | Display: 55.3
Numerator / after operand: 0.5527814279456855 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CHOUTEAU"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CHOUTEAU-R-2026.json](evidence/SENATE-CHOUTEAU-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CHOUTEAU-SETH-BODNAR-2026: PASS

CHOUTEAU: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 30.398598335523435 | Display: 30.4
Numerator / after operand: 0.30398598335523436 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CHOUTEAU"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CHOUTEAU-SETH-BODNAR-2026.json](evidence/SENATE-CHOUTEAU-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CHOUTEAU-ALANI-BANKHEAD-2026: PASS

CHOUTEAU: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 11.738939991239597 | Display: 11.7
Numerator / after operand: 0.11738939991239597 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CHOUTEAU"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CHOUTEAU-ALANI-BANKHEAD-2026.json](evidence/SENATE-CHOUTEAU-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CUSTER-R-SHARE-CHANGE: PASS

SENATE: CUSTER, republican_share_change_pp

Expected: None | Calculated: -1.5735967926689631 | Display: -1.6
Numerator / after operand: -1.5735967926689631 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CUSTER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CUSTER-R-SHARE-CHANGE.json](evidence/SENATE-CUSTER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CUSTER-TWO-PARTY-CHANGE: PASS

SENATE: CUSTER, republican_two_party_share_change_pp

Expected: None | Calculated: 20.119734551158675 | Display: 20.1
Numerator / after operand: 20.119734551158675 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "CUSTER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CUSTER-TWO-PARTY-CHANGE.json](evidence/SENATE-CUSTER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CUSTER-R-2024: PASS

CUSTER: republican_share in 2024 (%)

Expected: None | Calculated: 65.60137457044674 | Display: 65.6
Numerator / after operand: 0.6560137457044674 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CUSTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CUSTER-R-2024.json](evidence/SENATE-CUSTER-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CUSTER-JON-TESTER-2024: PASS

CUSTER: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 31.872852233676973 | Display: 31.9
Numerator / after operand: 0.31872852233676974 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "CUSTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-CUSTER-JON-TESTER-2024.json](evidence/SENATE-CUSTER-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CUSTER-R-2026: PASS

CUSTER: republican_share in 2026 (%)

Expected: None | Calculated: 64.02777777777777 | Display: 64.0
Numerator / after operand: 0.6402777777777777 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CUSTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CUSTER-R-2026.json](evidence/SENATE-CUSTER-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CUSTER-SETH-BODNAR-2026: PASS

CUSTER: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 24.583333333333332 | Display: 24.6
Numerator / after operand: 0.24583333333333332 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CUSTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CUSTER-SETH-BODNAR-2026.json](evidence/SENATE-CUSTER-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CUSTER-ALANI-BANKHEAD-2026: PASS

CUSTER: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 9.212962962962964 | Display: 9.2
Numerator / after operand: 0.09212962962962963 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "CUSTER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CUSTER-ALANI-BANKHEAD-2026.json](evidence/SENATE-CUSTER-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DANIELS-R-SHARE-CHANGE: PASS

SENATE: DANIELS, republican_share_change_pp

Expected: None | Calculated: -1.975787201361645 | Display: -2.0
Numerator / after operand: -1.975787201361645 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "DANIELS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DANIELS-R-SHARE-CHANGE.json](evidence/SENATE-DANIELS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DANIELS-TWO-PARTY-CHANGE: PASS

SENATE: DANIELS, republican_two_party_share_change_pp

Expected: None | Calculated: 15.653130211982235 | Display: 15.7
Numerator / after operand: 15.653130211982235 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "DANIELS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DANIELS-TWO-PARTY-CHANGE.json](evidence/SENATE-DANIELS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DANIELS-R-2024: PASS

DANIELS: republican_share in 2024 (%)

Expected: None | Calculated: 75.36687631027253 | Display: 75.4
Numerator / after operand: 0.7536687631027253 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "DANIELS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-DANIELS-R-2024.json](evidence/SENATE-DANIELS-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DANIELS-JON-TESTER-2024: PASS

DANIELS: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 23.060796645702304 | Display: 23.1
Numerator / after operand: 0.23060796645702306 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "DANIELS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-DANIELS-JON-TESTER-2024.json](evidence/SENATE-DANIELS-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DANIELS-R-2026: PASS

DANIELS: republican_share in 2026 (%)

Expected: None | Calculated: 73.39108910891089 | Display: 73.4
Numerator / after operand: 0.7339108910891089 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "DANIELS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DANIELS-R-2026.json](evidence/SENATE-DANIELS-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DANIELS-SETH-BODNAR-2026: PASS

DANIELS: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 17.450495049504948 | Display: 17.5
Numerator / after operand: 0.1745049504950495 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "DANIELS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DANIELS-SETH-BODNAR-2026.json](evidence/SENATE-DANIELS-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DANIELS-ALANI-BANKHEAD-2026: PASS

DANIELS: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 6.188118811881188 | Display: 6.2
Numerator / after operand: 0.06188118811881188 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "DANIELS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DANIELS-ALANI-BANKHEAD-2026.json](evidence/SENATE-DANIELS-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DAWSON-R-SHARE-CHANGE: PASS

SENATE: DAWSON, republican_share_change_pp

Expected: None | Calculated: -2.0467937552726356 | Display: -2.0
Numerator / after operand: -2.0467937552726356 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "DAWSON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DAWSON-R-SHARE-CHANGE.json](evidence/SENATE-DAWSON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DAWSON-TWO-PARTY-CHANGE: PASS

SENATE: DAWSON, republican_two_party_share_change_pp

Expected: None | Calculated: 16.302059241336465 | Display: 16.3
Numerator / after operand: 16.302059241336465 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "DAWSON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DAWSON-TWO-PARTY-CHANGE.json](evidence/SENATE-DAWSON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DAWSON-R-2024: PASS

DAWSON: republican_share in 2024 (%)

Expected: None | Calculated: 70.25574897915322 | Display: 70.3
Numerator / after operand: 0.7025574897915323 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "DAWSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-DAWSON-R-2024.json](evidence/SENATE-DAWSON-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DAWSON-JON-TESTER-2024: PASS

DAWSON: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 27.057812164195145 | Display: 27.1
Numerator / after operand: 0.27057812164195144 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "DAWSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-DAWSON-JON-TESTER-2024.json](evidence/SENATE-DAWSON-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DAWSON-R-2026: PASS

DAWSON: republican_share in 2026 (%)

Expected: None | Calculated: 68.2089552238806 | Display: 68.2
Numerator / after operand: 0.682089552238806 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "DAWSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DAWSON-R-2026.json](evidence/SENATE-DAWSON-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DAWSON-SETH-BODNAR-2026: PASS

DAWSON: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 20.477611940298505 | Display: 20.5
Numerator / after operand: 0.20477611940298507 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "DAWSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DAWSON-SETH-BODNAR-2026.json](evidence/SENATE-DAWSON-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DAWSON-ALANI-BANKHEAD-2026: PASS

DAWSON: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 8.865671641791046 | Display: 8.9
Numerator / after operand: 0.08865671641791045 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "DAWSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DAWSON-ALANI-BANKHEAD-2026.json](evidence/SENATE-DAWSON-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DEER-LODGE-R-SHARE-CHANGE: PASS

SENATE: DEER LODGE, republican_share_change_pp

Expected: None | Calculated: -0.6990381620986197 | Display: -0.7
Numerator / after operand: -0.6990381620986197 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "DEER LODGE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DEER-LODGE-R-SHARE-CHANGE.json](evidence/SENATE-DEER-LODGE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DEER-LODGE-TWO-PARTY-CHANGE: PASS

SENATE: DEER LODGE, republican_two_party_share_change_pp

Expected: None | Calculated: 31.367938744237932 | Display: 31.4
Numerator / after operand: 31.367938744237932 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "DEER LODGE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DEER-LODGE-TWO-PARTY-CHANGE.json](evidence/SENATE-DEER-LODGE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DEER-LODGE-R-2024: PASS

DEER LODGE: republican_share in 2024 (%)

Expected: None | Calculated: 37.06720977596741 | Display: 37.1
Numerator / after operand: 0.37067209775967414 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "DEER LODGE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-DEER-LODGE-R-2024.json](evidence/SENATE-DEER-LODGE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DEER-LODGE-JON-TESTER-2024: PASS

DEER LODGE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 60.91649694501018 | Display: 60.9
Numerator / after operand: 0.6091649694501018 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "DEER LODGE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-DEER-LODGE-JON-TESTER-2024.json](evidence/SENATE-DEER-LODGE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DEER-LODGE-R-2026: PASS

DEER LODGE: republican_share in 2026 (%)

Expected: None | Calculated: 36.368171613868796 | Display: 36.4
Numerator / after operand: 0.36368171613868794 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "DEER LODGE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DEER-LODGE-R-2026.json](evidence/SENATE-DEER-LODGE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DEER-LODGE-SETH-BODNAR-2026: PASS

DEER LODGE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 45.522574208031926 | Display: 45.5
Numerator / after operand: 0.4552257420803193 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "DEER LODGE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DEER-LODGE-SETH-BODNAR-2026.json](evidence/SENATE-DEER-LODGE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DEER-LODGE-ALANI-BANKHEAD-2026: PASS

DEER LODGE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 16.188575704664505 | Display: 16.2
Numerator / after operand: 0.16188575704664504 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "DEER LODGE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DEER-LODGE-ALANI-BANKHEAD-2026.json](evidence/SENATE-DEER-LODGE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FALLON-R-SHARE-CHANGE: PASS

SENATE: FALLON, republican_share_change_pp

Expected: None | Calculated: -1.3023337616766106 | Display: -1.3
Numerator / after operand: -1.3023337616766106 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "FALLON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FALLON-R-SHARE-CHANGE.json](evidence/SENATE-FALLON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FALLON-TWO-PARTY-CHANGE: PASS

SENATE: FALLON, republican_two_party_share_change_pp

Expected: None | Calculated: 10.86899072871017 | Display: 10.9
Numerator / after operand: 10.86899072871017 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "FALLON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FALLON-TWO-PARTY-CHANGE.json](evidence/SENATE-FALLON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FALLON-R-2024: PASS

FALLON: republican_share in 2024 (%)

Expected: None | Calculated: 80.2675585284281 | Display: 80.3
Numerator / after operand: 0.802675585284281 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "FALLON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-FALLON-R-2024.json](evidence/SENATE-FALLON-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FALLON-JON-TESTER-2024: PASS

FALLON: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 17.123745819397993 | Display: 17.1
Numerator / after operand: 0.17123745819397992 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "FALLON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-FALLON-JON-TESTER-2024.json](evidence/SENATE-FALLON-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FALLON-R-2026: PASS

FALLON: republican_share in 2026 (%)

Expected: None | Calculated: 78.96522476675149 | Display: 79.0
Numerator / after operand: 0.7896522476675149 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "FALLON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FALLON-R-2026.json](evidence/SENATE-FALLON-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FALLON-SETH-BODNAR-2026: PASS

FALLON: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 13.740458015267176 | Display: 13.7
Numerator / after operand: 0.13740458015267176 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "FALLON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FALLON-SETH-BODNAR-2026.json](evidence/SENATE-FALLON-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FALLON-ALANI-BANKHEAD-2026: PASS

FALLON: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 5.682782018659881 | Display: 5.7
Numerator / after operand: 0.056827820186598814 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "FALLON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FALLON-ALANI-BANKHEAD-2026.json](evidence/SENATE-FALLON-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FERGUS-R-SHARE-CHANGE: PASS

SENATE: FERGUS, republican_share_change_pp

Expected: None | Calculated: -7.033198159991782 | Display: -7.0
Numerator / after operand: -7.033198159991782 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "FERGUS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FERGUS-R-SHARE-CHANGE.json](evidence/SENATE-FERGUS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FERGUS-TWO-PARTY-CHANGE: PASS

SENATE: FERGUS, republican_two_party_share_change_pp

Expected: None | Calculated: 16.786211239699846 | Display: 16.8
Numerator / after operand: 16.786211239699846 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "FERGUS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FERGUS-TWO-PARTY-CHANGE.json](evidence/SENATE-FERGUS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FERGUS-R-2024: PASS

FERGUS: republican_share in 2024 (%)

Expected: None | Calculated: 70.22031642762087 | Display: 70.2
Numerator / after operand: 0.7022031642762088 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "FERGUS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-FERGUS-R-2024.json](evidence/SENATE-FERGUS-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FERGUS-JON-TESTER-2024: PASS

FERGUS: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 28.24190448026024 | Display: 28.2
Numerator / after operand: 0.2824190448026024 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "FERGUS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-FERGUS-JON-TESTER-2024.json](evidence/SENATE-FERGUS-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FERGUS-R-2026: PASS

FERGUS: republican_share in 2026 (%)

Expected: None | Calculated: 63.187118267629096 | Display: 63.2
Numerator / after operand: 0.6318711826762909 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "FERGUS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FERGUS-R-2026.json](evidence/SENATE-FERGUS-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FERGUS-SETH-BODNAR-2026: PASS

FERGUS: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 26.0595965204516 | Display: 26.1
Numerator / after operand: 0.260595965204516 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "FERGUS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FERGUS-SETH-BODNAR-2026.json](evidence/SENATE-FERGUS-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FERGUS-ALANI-BANKHEAD-2026: PASS

FERGUS: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 8.532296872108088 | Display: 8.5
Numerator / after operand: 0.08532296872108087 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "FERGUS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FERGUS-ALANI-BANKHEAD-2026.json](evidence/SENATE-FERGUS-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FLATHEAD-R-SHARE-CHANGE: PASS

SENATE: FLATHEAD, republican_share_change_pp

Expected: None | Calculated: -3.274099039820766 | Display: -3.3
Numerator / after operand: -3.274099039820766 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "FLATHEAD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FLATHEAD-R-SHARE-CHANGE.json](evidence/SENATE-FLATHEAD-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FLATHEAD-TWO-PARTY-CHANGE: PASS

SENATE: FLATHEAD, republican_two_party_share_change_pp

Expected: None | Calculated: 21.250578001318875 | Display: 21.3
Numerator / after operand: 21.250578001318875 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "FLATHEAD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FLATHEAD-TWO-PARTY-CHANGE.json](evidence/SENATE-FLATHEAD-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FLATHEAD-R-2024: PASS

FLATHEAD: republican_share in 2024 (%)

Expected: None | Calculated: 60.71889458940544 | Display: 60.7
Numerator / after operand: 0.6071889458940544 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "FLATHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-FLATHEAD-R-2024.json](evidence/SENATE-FLATHEAD-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FLATHEAD-JON-TESTER-2024: PASS

FLATHEAD: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 37.21475559472475 | Display: 37.2
Numerator / after operand: 0.37214755594724747 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "FLATHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-FLATHEAD-JON-TESTER-2024.json](evidence/SENATE-FLATHEAD-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FLATHEAD-R-2026: PASS

FLATHEAD: republican_share in 2026 (%)

Expected: None | Calculated: 57.44479554958467 | Display: 57.4
Numerator / after operand: 0.5744479554958467 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "FLATHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FLATHEAD-R-2026.json](evidence/SENATE-FLATHEAD-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FLATHEAD-SETH-BODNAR-2026: PASS

FLATHEAD: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 29.438589188064107 | Display: 29.4
Numerator / after operand: 0.29438589188064107 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "FLATHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FLATHEAD-SETH-BODNAR-2026.json](evidence/SENATE-FLATHEAD-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FLATHEAD-ALANI-BANKHEAD-2026: PASS

FLATHEAD: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 11.557456148649928 | Display: 11.6
Numerator / after operand: 0.11557456148649928 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "FLATHEAD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FLATHEAD-ALANI-BANKHEAD-2026.json](evidence/SENATE-FLATHEAD-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GALLATIN-R-SHARE-CHANGE: PASS

SENATE: GALLATIN, republican_share_change_pp

Expected: None | Calculated: -7.235623280281212 | Display: -7.2
Numerator / after operand: -7.235623280281212 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GALLATIN-R-SHARE-CHANGE.json](evidence/SENATE-GALLATIN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GALLATIN-TWO-PARTY-CHANGE: PASS

SENATE: GALLATIN, republican_two_party_share_change_pp

Expected: None | Calculated: 27.870405909486745 | Display: 27.9
Numerator / after operand: 27.870405909486745 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GALLATIN-TWO-PARTY-CHANGE.json](evidence/SENATE-GALLATIN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GALLATIN-R-2024: PASS

GALLATIN: republican_share in 2024 (%)

Expected: None | Calculated: 43.28112819785982 | Display: 43.3
Numerator / after operand: 0.43281128197859825 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GALLATIN-R-2024.json](evidence/SENATE-GALLATIN-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GALLATIN-JON-TESTER-2024: PASS

GALLATIN: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 55.40925519098575 | Display: 55.4
Numerator / after operand: 0.5540925519098575 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GALLATIN-JON-TESTER-2024.json](evidence/SENATE-GALLATIN-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GALLATIN-R-2026: PASS

GALLATIN: republican_share in 2026 (%)

Expected: None | Calculated: 36.04550491757861 | Display: 36.0
Numerator / after operand: 0.36045504917578614 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GALLATIN-R-2026.json](evidence/SENATE-GALLATIN-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GALLATIN-SETH-BODNAR-2026: PASS

GALLATIN: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 48.285773652860506 | Display: 48.3
Numerator / after operand: 0.4828577365286051 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GALLATIN-SETH-BODNAR-2026.json](evidence/SENATE-GALLATIN-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GALLATIN-ALANI-BANKHEAD-2026: PASS

GALLATIN: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 14.20903172184513 | Display: 14.2
Numerator / after operand: 0.1420903172184513 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GALLATIN-ALANI-BANKHEAD-2026.json](evidence/SENATE-GALLATIN-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GARFIELD-R-SHARE-CHANGE: PASS

SENATE: GARFIELD, republican_share_change_pp

Expected: None | Calculated: -6.378754415261612 | Display: -6.4
Numerator / after operand: -6.378754415261612 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GARFIELD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GARFIELD-R-SHARE-CHANGE.json](evidence/SENATE-GARFIELD-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GARFIELD-TWO-PARTY-CHANGE: PASS

SENATE: GARFIELD, republican_two_party_share_change_pp

Expected: None | Calculated: 4.274040927501376 | Display: 4.3
Numerator / after operand: 4.274040927501376 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GARFIELD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GARFIELD-TWO-PARTY-CHANGE.json](evidence/SENATE-GARFIELD-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GARFIELD-R-2024: PASS

GARFIELD: republican_share in 2024 (%)

Expected: None | Calculated: 90.45226130653266 | Display: 90.5
Numerator / after operand: 0.9045226130653267 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GARFIELD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GARFIELD-R-2024.json](evidence/SENATE-GARFIELD-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GARFIELD-JON-TESTER-2024: PASS

GARFIELD: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 8.542713567839195 | Display: 8.5
Numerator / after operand: 0.08542713567839195 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GARFIELD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GARFIELD-JON-TESTER-2024.json](evidence/SENATE-GARFIELD-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GARFIELD-R-2026: PASS

GARFIELD: republican_share in 2026 (%)

Expected: None | Calculated: 84.07350689127105 | Display: 84.1
Numerator / after operand: 0.8407350689127105 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GARFIELD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GARFIELD-R-2026.json](evidence/SENATE-GARFIELD-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GARFIELD-SETH-BODNAR-2026: PASS

GARFIELD: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 9.80091883614089 | Display: 9.8
Numerator / after operand: 0.09800918836140889 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GARFIELD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GARFIELD-SETH-BODNAR-2026.json](evidence/SENATE-GARFIELD-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GARFIELD-ALANI-BANKHEAD-2026: PASS

GARFIELD: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 3.828483920367534 | Display: 3.8
Numerator / after operand: 0.03828483920367534 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GARFIELD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GARFIELD-ALANI-BANKHEAD-2026.json](evidence/SENATE-GARFIELD-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GLACIER-R-SHARE-CHANGE: PASS

SENATE: GLACIER, republican_share_change_pp

Expected: None | Calculated: 1.4677911222638007 | Display: 1.5
Numerator / after operand: 1.4677911222638007 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GLACIER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GLACIER-R-SHARE-CHANGE.json](evidence/SENATE-GLACIER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GLACIER-TWO-PARTY-CHANGE: PASS

SENATE: GLACIER, republican_two_party_share_change_pp

Expected: None | Calculated: 23.352936858020062 | Display: 23.4
Numerator / after operand: 23.352936858020062 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GLACIER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GLACIER-TWO-PARTY-CHANGE.json](evidence/SENATE-GLACIER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GLACIER-R-2024: PASS

GLACIER: republican_share in 2024 (%)

Expected: None | Calculated: 27.775613556680952 | Display: 27.8
Numerator / after operand: 0.2777561355668095 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GLACIER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GLACIER-R-2024.json](evidence/SENATE-GLACIER-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GLACIER-JON-TESTER-2024: PASS

GLACIER: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 70.86092715231787 | Display: 70.9
Numerator / after operand: 0.7086092715231788 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GLACIER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GLACIER-JON-TESTER-2024.json](evidence/SENATE-GLACIER-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GLACIER-R-2026: PASS

GLACIER: republican_share in 2026 (%)

Expected: None | Calculated: 29.24340467894475 | Display: 29.2
Numerator / after operand: 0.2924340467894475 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GLACIER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GLACIER-R-2026.json](evidence/SENATE-GLACIER-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GLACIER-SETH-BODNAR-2026: PASS

GLACIER: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 41.612742658038826 | Display: 41.6
Numerator / after operand: 0.41612742658038826 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GLACIER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GLACIER-SETH-BODNAR-2026.json](evidence/SENATE-GLACIER-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GLACIER-ALANI-BANKHEAD-2026: PASS

GLACIER: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 27.526132404181187 | Display: 27.5
Numerator / after operand: 0.27526132404181186 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GLACIER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GLACIER-ALANI-BANKHEAD-2026.json](evidence/SENATE-GLACIER-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GOLDEN-VALLEY-R-SHARE-CHANGE: PASS

SENATE: GOLDEN VALLEY, republican_share_change_pp

Expected: None | Calculated: -5.8961141950832685 | Display: -5.9
Numerator / after operand: -5.8961141950832685 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GOLDEN VALLEY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GOLDEN-VALLEY-R-SHARE-CHANGE.json](evidence/SENATE-GOLDEN-VALLEY-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GOLDEN-VALLEY-TWO-PARTY-CHANGE: PASS

SENATE: GOLDEN VALLEY, republican_two_party_share_change_pp

Expected: None | Calculated: 10.143854714141199 | Display: 10.1
Numerator / after operand: 10.143854714141199 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GOLDEN VALLEY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GOLDEN-VALLEY-TWO-PARTY-CHANGE.json](evidence/SENATE-GOLDEN-VALLEY-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GOLDEN-VALLEY-R-2024: PASS

GOLDEN VALLEY: republican_share in 2024 (%)

Expected: None | Calculated: 81.15384615384616 | Display: 81.2
Numerator / after operand: 0.8115384615384615 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GOLDEN VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GOLDEN-VALLEY-R-2024.json](evidence/SENATE-GOLDEN-VALLEY-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GOLDEN-VALLEY-JON-TESTER-2024: PASS

GOLDEN VALLEY: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 17.5 | Display: 17.5
Numerator / after operand: 0.175 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GOLDEN VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GOLDEN-VALLEY-JON-TESTER-2024.json](evidence/SENATE-GOLDEN-VALLEY-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GOLDEN-VALLEY-R-2026: PASS

GOLDEN VALLEY: republican_share in 2026 (%)

Expected: None | Calculated: 75.25773195876289 | Display: 75.3
Numerator / after operand: 0.7525773195876289 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GOLDEN VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GOLDEN-VALLEY-R-2026.json](evidence/SENATE-GOLDEN-VALLEY-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GOLDEN-VALLEY-SETH-BODNAR-2026: PASS

GOLDEN VALLEY: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 13.917525773195877 | Display: 13.9
Numerator / after operand: 0.13917525773195877 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GOLDEN VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GOLDEN-VALLEY-SETH-BODNAR-2026.json](evidence/SENATE-GOLDEN-VALLEY-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GOLDEN-VALLEY-ALANI-BANKHEAD-2026: PASS

GOLDEN VALLEY: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 6.185567010309279 | Display: 6.2
Numerator / after operand: 0.061855670103092786 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GOLDEN VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GOLDEN-VALLEY-ALANI-BANKHEAD-2026.json](evidence/SENATE-GOLDEN-VALLEY-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GRANITE-R-SHARE-CHANGE: PASS

SENATE: GRANITE, republican_share_change_pp

Expected: None | Calculated: -4.049041355171779 | Display: -4.0
Numerator / after operand: -4.049041355171779 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GRANITE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GRANITE-R-SHARE-CHANGE.json](evidence/SENATE-GRANITE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GRANITE-TWO-PARTY-CHANGE: PASS

SENATE: GRANITE, republican_two_party_share_change_pp

Expected: None | Calculated: 22.96751927100179 | Display: 23.0
Numerator / after operand: 22.96751927100179 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "GRANITE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GRANITE-TWO-PARTY-CHANGE.json](evidence/SENATE-GRANITE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GRANITE-R-2024: PASS

GRANITE: republican_share in 2024 (%)

Expected: None | Calculated: 63.02059496567506 | Display: 63.0
Numerator / after operand: 0.6302059496567506 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GRANITE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GRANITE-R-2024.json](evidence/SENATE-GRANITE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GRANITE-JON-TESTER-2024: PASS

GRANITE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 35.60640732265446 | Display: 35.6
Numerator / after operand: 0.3560640732265446 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "GRANITE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-GRANITE-JON-TESTER-2024.json](evidence/SENATE-GRANITE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GRANITE-R-2026: PASS

GRANITE: republican_share in 2026 (%)

Expected: None | Calculated: 58.97155361050328 | Display: 59.0
Numerator / after operand: 0.5897155361050328 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GRANITE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GRANITE-R-2026.json](evidence/SENATE-GRANITE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GRANITE-SETH-BODNAR-2026: PASS

GRANITE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 29.48577680525164 | Display: 29.5
Numerator / after operand: 0.2948577680525164 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GRANITE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GRANITE-SETH-BODNAR-2026.json](evidence/SENATE-GRANITE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GRANITE-ALANI-BANKHEAD-2026: PASS

GRANITE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 8.916849015317286 | Display: 8.9
Numerator / after operand: 0.08916849015317287 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "GRANITE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GRANITE-ALANI-BANKHEAD-2026.json](evidence/SENATE-GRANITE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-HILL-R-SHARE-CHANGE: PASS

SENATE: HILL, republican_share_change_pp

Expected: None | Calculated: -1.8876260178916304 | Display: -1.9
Numerator / after operand: -1.8876260178916304 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "HILL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-HILL-R-SHARE-CHANGE.json](evidence/SENATE-HILL-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-HILL-TWO-PARTY-CHANGE: PASS

SENATE: HILL, republican_two_party_share_change_pp

Expected: None | Calculated: 23.517990849311367 | Display: 23.5
Numerator / after operand: 23.517990849311367 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "HILL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-HILL-TWO-PARTY-CHANGE.json](evidence/SENATE-HILL-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-HILL-R-2024: PASS

HILL: republican_share in 2024 (%)

Expected: None | Calculated: 47.08723653395784 | Display: 47.1
Numerator / after operand: 0.47087236533957844 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "HILL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-HILL-R-2024.json](evidence/SENATE-HILL-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-HILL-JON-TESTER-2024: PASS

HILL: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 50.322014051522245 | Display: 50.3
Numerator / after operand: 0.5032201405152225 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "HILL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-HILL-JON-TESTER-2024.json](evidence/SENATE-HILL-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-HILL-R-2026: PASS

HILL: republican_share in 2026 (%)

Expected: None | Calculated: 45.199610516066215 | Display: 45.2
Numerator / after operand: 0.45199610516066213 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "HILL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-HILL-R-2026.json](evidence/SENATE-HILL-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-HILL-SETH-BODNAR-2026: PASS

HILL: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 32.852969814995134 | Display: 32.9
Numerator / after operand: 0.3285296981499513 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "HILL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-HILL-SETH-BODNAR-2026.json](evidence/SENATE-HILL-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-HILL-ALANI-BANKHEAD-2026: PASS

HILL: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 17.702044790652387 | Display: 17.7
Numerator / after operand: 0.17702044790652385 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "HILL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-HILL-ALANI-BANKHEAD-2026.json](evidence/SENATE-HILL-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JEFFERSON-R-SHARE-CHANGE: PASS

SENATE: JEFFERSON, republican_share_change_pp

Expected: None | Calculated: -4.193183716872529 | Display: -4.2
Numerator / after operand: -4.193183716872529 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "JEFFERSON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JEFFERSON-R-SHARE-CHANGE.json](evidence/SENATE-JEFFERSON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JEFFERSON-TWO-PARTY-CHANGE: PASS

SENATE: JEFFERSON, republican_two_party_share_change_pp

Expected: None | Calculated: 24.748130368593923 | Display: 24.7
Numerator / after operand: 24.748130368593923 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "JEFFERSON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JEFFERSON-TWO-PARTY-CHANGE.json](evidence/SENATE-JEFFERSON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JEFFERSON-R-2024: PASS

JEFFERSON: republican_share in 2024 (%)

Expected: None | Calculated: 61.15168203040824 | Display: 61.2
Numerator / after operand: 0.6115168203040824 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "JEFFERSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-JEFFERSON-R-2024.json](evidence/SENATE-JEFFERSON-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JEFFERSON-JON-TESTER-2024: PASS

JEFFERSON: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 37.10044295462708 | Display: 37.1
Numerator / after operand: 0.3710044295462708 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "JEFFERSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-JEFFERSON-JON-TESTER-2024.json](evidence/SENATE-JEFFERSON-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JEFFERSON-R-2026: PASS

JEFFERSON: republican_share in 2026 (%)

Expected: None | Calculated: 56.95849831353571 | Display: 57.0
Numerator / after operand: 0.5695849831353571 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "JEFFERSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JEFFERSON-R-2026.json](evidence/SENATE-JEFFERSON-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JEFFERSON-SETH-BODNAR-2026: PASS

JEFFERSON: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 32.52676345505206 | Display: 32.5
Numerator / after operand: 0.3252676345505206 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "JEFFERSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JEFFERSON-SETH-BODNAR-2026.json](evidence/SENATE-JEFFERSON-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JEFFERSON-ALANI-BANKHEAD-2026: PASS

JEFFERSON: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 8.52031089602581 | Display: 8.5
Numerator / after operand: 0.08520310896025811 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "JEFFERSON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JEFFERSON-ALANI-BANKHEAD-2026.json](evidence/SENATE-JEFFERSON-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JUDITH-BASIN-R-SHARE-CHANGE: PASS

SENATE: JUDITH BASIN, republican_share_change_pp

Expected: None | Calculated: -7.661461491813215 | Display: -7.7
Numerator / after operand: -7.661461491813215 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "JUDITH BASIN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JUDITH-BASIN-R-SHARE-CHANGE.json](evidence/SENATE-JUDITH-BASIN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JUDITH-BASIN-TWO-PARTY-CHANGE: PASS

SENATE: JUDITH BASIN, republican_two_party_share_change_pp

Expected: None | Calculated: 18.433549958427164 | Display: 18.4
Numerator / after operand: 18.433549958427164 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "JUDITH BASIN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JUDITH-BASIN-TWO-PARTY-CHANGE.json](evidence/SENATE-JUDITH-BASIN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JUDITH-BASIN-R-2024: PASS

JUDITH BASIN: republican_share in 2024 (%)

Expected: None | Calculated: 72.86764705882352 | Display: 72.9
Numerator / after operand: 0.7286764705882353 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "JUDITH BASIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-JUDITH-BASIN-R-2024.json](evidence/SENATE-JUDITH-BASIN-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JUDITH-BASIN-JON-TESTER-2024: PASS

JUDITH BASIN: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 25.882352941176475 | Display: 25.9
Numerator / after operand: 0.25882352941176473 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "JUDITH BASIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-JUDITH-BASIN-JON-TESTER-2024.json](evidence/SENATE-JUDITH-BASIN-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JUDITH-BASIN-R-2026: PASS

JUDITH BASIN: republican_share in 2026 (%)

Expected: None | Calculated: 65.20618556701031 | Display: 65.2
Numerator / after operand: 0.6520618556701031 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "JUDITH BASIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JUDITH-BASIN-R-2026.json](evidence/SENATE-JUDITH-BASIN-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JUDITH-BASIN-SETH-BODNAR-2026: PASS

JUDITH BASIN: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 26.11683848797251 | Display: 26.1
Numerator / after operand: 0.2611683848797251 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "JUDITH BASIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JUDITH-BASIN-SETH-BODNAR-2026.json](evidence/SENATE-JUDITH-BASIN-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JUDITH-BASIN-ALANI-BANKHEAD-2026: PASS

JUDITH BASIN: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 5.498281786941581 | Display: 5.5
Numerator / after operand: 0.054982817869415807 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "JUDITH BASIN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JUDITH-BASIN-ALANI-BANKHEAD-2026.json](evidence/SENATE-JUDITH-BASIN-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LAKE-R-SHARE-CHANGE: PASS

SENATE: LAKE, republican_share_change_pp

Expected: None | Calculated: -1.5855759482364506 | Display: -1.6
Numerator / after operand: -1.5855759482364506 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "LAKE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LAKE-R-SHARE-CHANGE.json](evidence/SENATE-LAKE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LAKE-TWO-PARTY-CHANGE: PASS

SENATE: LAKE, republican_two_party_share_change_pp

Expected: None | Calculated: 25.621954894808784 | Display: 25.6
Numerator / after operand: 25.621954894808784 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "LAKE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LAKE-TWO-PARTY-CHANGE.json](evidence/SENATE-LAKE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LAKE-R-2024: PASS

LAKE: republican_share in 2024 (%)

Expected: None | Calculated: 52.26269640440181 | Display: 52.3
Numerator / after operand: 0.5226269640440181 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "LAKE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-LAKE-R-2024.json](evidence/SENATE-LAKE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LAKE-JON-TESTER-2024: PASS

LAKE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 45.88948390513741 | Display: 45.9
Numerator / after operand: 0.45889483905137407 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "LAKE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-LAKE-JON-TESTER-2024.json](evidence/SENATE-LAKE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LAKE-R-2026: PASS

LAKE: republican_share in 2026 (%)

Expected: None | Calculated: 50.67712045616536 | Display: 50.7
Numerator / after operand: 0.5067712045616536 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LAKE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LAKE-R-2026.json](evidence/SENATE-LAKE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LAKE-SETH-BODNAR-2026: PASS

LAKE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 34.354953670705626 | Display: 34.4
Numerator / after operand: 0.3435495367070563 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LAKE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LAKE-SETH-BODNAR-2026.json](evidence/SENATE-LAKE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LAKE-ALANI-BANKHEAD-2026: PASS

LAKE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 13.578047042052743 | Display: 13.6
Numerator / after operand: 0.13578047042052743 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LAKE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LAKE-ALANI-BANKHEAD-2026.json](evidence/SENATE-LAKE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LEWIS-AND-CLARK-R-SHARE-CHANGE: PASS

SENATE: LEWIS AND CLARK, republican_share_change_pp

Expected: None | Calculated: -5.149280605622875 | Display: -5.1
Numerator / after operand: -5.149280605622875 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "LEWIS AND CLARK"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LEWIS-AND-CLARK-R-SHARE-CHANGE.json](evidence/SENATE-LEWIS-AND-CLARK-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LEWIS-AND-CLARK-TWO-PARTY-CHANGE: PASS

SENATE: LEWIS AND CLARK, republican_two_party_share_change_pp

Expected: None | Calculated: 33.95214664911295 | Display: 34.0
Numerator / after operand: 33.95214664911295 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "LEWIS AND CLARK"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LEWIS-AND-CLARK-TWO-PARTY-CHANGE.json](evidence/SENATE-LEWIS-AND-CLARK-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LEWIS-AND-CLARK-R-2024: PASS

LEWIS AND CLARK: republican_share in 2024 (%)

Expected: None | Calculated: 45.68874000330274 | Display: 45.7
Numerator / after operand: 0.4568874000330274 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "LEWIS AND CLARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-LEWIS-AND-CLARK-R-2024.json](evidence/SENATE-LEWIS-AND-CLARK-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LEWIS-AND-CLARK-JON-TESTER-2024: PASS

LEWIS AND CLARK: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 52.31310009672321 | Display: 52.3
Numerator / after operand: 0.5231310009672321 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "LEWIS AND CLARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-LEWIS-AND-CLARK-JON-TESTER-2024.json](evidence/SENATE-LEWIS-AND-CLARK-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LEWIS-AND-CLARK-R-2026: PASS

LEWIS AND CLARK: republican_share in 2026 (%)

Expected: None | Calculated: 40.53945939767986 | Display: 40.5
Numerator / after operand: 0.40539459397679867 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LEWIS AND CLARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LEWIS-AND-CLARK-R-2026.json](evidence/SENATE-LEWIS-AND-CLARK-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LEWIS-AND-CLARK-SETH-BODNAR-2026: PASS

LEWIS AND CLARK: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 48.00845762615006 | Display: 48.0
Numerator / after operand: 0.48008457626150064 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LEWIS AND CLARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LEWIS-AND-CLARK-SETH-BODNAR-2026.json](evidence/SENATE-LEWIS-AND-CLARK-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LEWIS-AND-CLARK-ALANI-BANKHEAD-2026: PASS

LEWIS AND CLARK: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 9.774844276815818 | Display: 9.8
Numerator / after operand: 0.09774844276815818 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LEWIS AND CLARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LEWIS-AND-CLARK-ALANI-BANKHEAD-2026.json](evidence/SENATE-LEWIS-AND-CLARK-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LIBERTY-R-SHARE-CHANGE: PASS

SENATE: LIBERTY, republican_share_change_pp

Expected: None | Calculated: -5.162378993629824 | Display: -5.2
Numerator / after operand: -5.162378993629824 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "LIBERTY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LIBERTY-R-SHARE-CHANGE.json](evidence/SENATE-LIBERTY-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LIBERTY-TWO-PARTY-CHANGE: PASS

SENATE: LIBERTY, republican_two_party_share_change_pp

Expected: None | Calculated: 18.129957897399763 | Display: 18.1
Numerator / after operand: 18.129957897399763 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "LIBERTY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LIBERTY-TWO-PARTY-CHANGE.json](evidence/SENATE-LIBERTY-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LIBERTY-R-2024: PASS

LIBERTY: republican_share in 2024 (%)

Expected: None | Calculated: 68.16367265469061 | Display: 68.2
Numerator / after operand: 0.6816367265469062 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "LIBERTY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-LIBERTY-R-2024.json](evidence/SENATE-LIBERTY-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LIBERTY-JON-TESTER-2024: PASS

LIBERTY: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 30.63872255489022 | Display: 30.6
Numerator / after operand: 0.3063872255489022 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "LIBERTY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-LIBERTY-JON-TESTER-2024.json](evidence/SENATE-LIBERTY-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LIBERTY-R-2026: PASS

LIBERTY: republican_share in 2026 (%)

Expected: None | Calculated: 63.0012936610608 | Display: 63.0
Numerator / after operand: 0.630012936610608 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LIBERTY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LIBERTY-R-2026.json](evidence/SENATE-LIBERTY-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LIBERTY-SETH-BODNAR-2026: PASS

LIBERTY: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 25.35575679172057 | Display: 25.4
Numerator / after operand: 0.2535575679172057 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LIBERTY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LIBERTY-SETH-BODNAR-2026.json](evidence/SENATE-LIBERTY-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LIBERTY-ALANI-BANKHEAD-2026: PASS

LIBERTY: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 9.314359637774903 | Display: 9.3
Numerator / after operand: 0.09314359637774904 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LIBERTY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LIBERTY-ALANI-BANKHEAD-2026.json](evidence/SENATE-LIBERTY-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LINCOLN-R-SHARE-CHANGE: PASS

SENATE: LINCOLN, republican_share_change_pp

Expected: None | Calculated: -0.5222803929901487 | Display: -0.5
Numerator / after operand: -0.5222803929901487 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "LINCOLN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LINCOLN-R-SHARE-CHANGE.json](evidence/SENATE-LINCOLN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LINCOLN-TWO-PARTY-CHANGE: PASS

SENATE: LINCOLN, republican_two_party_share_change_pp

Expected: None | Calculated: 13.828732818035538 | Display: 13.8
Numerator / after operand: 13.828732818035538 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "LINCOLN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LINCOLN-TWO-PARTY-CHANGE.json](evidence/SENATE-LINCOLN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LINCOLN-R-2024: PASS

LINCOLN: republican_share in 2024 (%)

Expected: None | Calculated: 70.14975886284796 | Display: 70.1
Numerator / after operand: 0.7014975886284796 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "LINCOLN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-LINCOLN-R-2024.json](evidence/SENATE-LINCOLN-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LINCOLN-JON-TESTER-2024: PASS

LINCOLN: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 27.811151535662916 | Display: 27.8
Numerator / after operand: 0.27811151535662915 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "LINCOLN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-LINCOLN-JON-TESTER-2024.json](evidence/SENATE-LINCOLN-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LINCOLN-R-2026: PASS

LINCOLN: republican_share in 2026 (%)

Expected: None | Calculated: 69.6274784698578 | Display: 69.6
Numerator / after operand: 0.6962747846985781 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LINCOLN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LINCOLN-R-2026.json](evidence/SENATE-LINCOLN-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LINCOLN-SETH-BODNAR-2026: PASS

LINCOLN: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 16.853595033046265 | Display: 16.9
Numerator / after operand: 0.16853595033046265 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LINCOLN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LINCOLN-SETH-BODNAR-2026.json](evidence/SENATE-LINCOLN-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LINCOLN-ALANI-BANKHEAD-2026: PASS

LINCOLN: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 11.866613258561987 | Display: 11.9
Numerator / after operand: 0.11866613258561987 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "LINCOLN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LINCOLN-ALANI-BANKHEAD-2026.json](evidence/SENATE-LINCOLN-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MADISON-R-SHARE-CHANGE: PASS

SENATE: MADISON, republican_share_change_pp

Expected: None | Calculated: -6.138501741194391 | Display: -6.1
Numerator / after operand: -6.138501741194391 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MADISON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MADISON-R-SHARE-CHANGE.json](evidence/SENATE-MADISON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MADISON-TWO-PARTY-CHANGE: PASS

SENATE: MADISON, republican_two_party_share_change_pp

Expected: None | Calculated: 17.469818597640206 | Display: 17.5
Numerator / after operand: 17.469818597640206 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MADISON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MADISON-TWO-PARTY-CHANGE.json](evidence/SENATE-MADISON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MADISON-R-2024: PASS

MADISON: republican_share in 2024 (%)

Expected: None | Calculated: 67.36260362296592 | Display: 67.4
Numerator / after operand: 0.6736260362296592 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MADISON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MADISON-R-2024.json](evidence/SENATE-MADISON-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MADISON-JON-TESTER-2024: PASS

MADISON: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 31.08688977586736 | Display: 31.1
Numerator / after operand: 0.3108688977586736 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MADISON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MADISON-JON-TESTER-2024.json](evidence/SENATE-MADISON-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MADISON-R-2026: PASS

MADISON: republican_share in 2026 (%)

Expected: None | Calculated: 61.22410188177153 | Display: 61.2
Numerator / after operand: 0.6122410188177153 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MADISON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MADISON-R-2026.json](evidence/SENATE-MADISON-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MADISON-SETH-BODNAR-2026: PASS

MADISON: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 26.85801178483178 | Display: 26.9
Numerator / after operand: 0.2685801178483178 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MADISON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MADISON-SETH-BODNAR-2026.json](evidence/SENATE-MADISON-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MADISON-ALANI-BANKHEAD-2026: PASS

MADISON: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 10.05512260026611 | Display: 10.1
Numerator / after operand: 0.10055122600266109 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MADISON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MADISON-ALANI-BANKHEAD-2026.json](evidence/SENATE-MADISON-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MCCONE-R-SHARE-CHANGE: PASS

SENATE: MCCONE, republican_share_change_pp

Expected: None | Calculated: -4.392989348039588 | Display: -4.4
Numerator / after operand: -4.392989348039588 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MCCONE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MCCONE-R-SHARE-CHANGE.json](evidence/SENATE-MCCONE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MCCONE-TWO-PARTY-CHANGE: PASS

SENATE: MCCONE, republican_two_party_share_change_pp

Expected: None | Calculated: 10.317247453013357 | Display: 10.3
Numerator / after operand: 10.317247453013357 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MCCONE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MCCONE-TWO-PARTY-CHANGE.json](evidence/SENATE-MCCONE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MCCONE-R-2024: PASS

MCCONE: republican_share in 2024 (%)

Expected: None | Calculated: 82.02764976958525 | Display: 82.0
Numerator / after operand: 0.8202764976958525 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MCCONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MCCONE-R-2024.json](evidence/SENATE-MCCONE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MCCONE-JON-TESTER-2024: PASS

MCCONE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 15.944700460829491 | Display: 15.9
Numerator / after operand: 0.15944700460829492 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MCCONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MCCONE-JON-TESTER-2024.json](evidence/SENATE-MCCONE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MCCONE-R-2026: PASS

MCCONE: republican_share in 2026 (%)

Expected: None | Calculated: 77.63466042154566 | Display: 77.6
Numerator / after operand: 0.7763466042154566 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MCCONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MCCONE-R-2026.json](evidence/SENATE-MCCONE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MCCONE-SETH-BODNAR-2026: PASS

MCCONE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 15.456674473067917 | Display: 15.5
Numerator / after operand: 0.15456674473067916 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MCCONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MCCONE-SETH-BODNAR-2026.json](evidence/SENATE-MCCONE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MCCONE-ALANI-BANKHEAD-2026: PASS

MCCONE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 4.918032786885246 | Display: 4.9
Numerator / after operand: 0.04918032786885246 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MCCONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MCCONE-ALANI-BANKHEAD-2026.json](evidence/SENATE-MCCONE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MEAGHER-R-SHARE-CHANGE: PASS

SENATE: MEAGHER, republican_share_change_pp

Expected: None | Calculated: -4.620922179697462 | Display: -4.6
Numerator / after operand: -4.620922179697462 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MEAGHER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MEAGHER-R-SHARE-CHANGE.json](evidence/SENATE-MEAGHER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MEAGHER-TWO-PARTY-CHANGE: PASS

SENATE: MEAGHER, republican_two_party_share_change_pp

Expected: None | Calculated: 19.347009304158156 | Display: 19.3
Numerator / after operand: 19.347009304158156 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MEAGHER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MEAGHER-TWO-PARTY-CHANGE.json](evidence/SENATE-MEAGHER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MEAGHER-R-2024: PASS

MEAGHER: republican_share in 2024 (%)

Expected: None | Calculated: 71.61016949152543 | Display: 71.6
Numerator / after operand: 0.7161016949152542 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MEAGHER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MEAGHER-R-2024.json](evidence/SENATE-MEAGHER-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MEAGHER-JON-TESTER-2024: PASS

MEAGHER: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 26.1864406779661 | Display: 26.2
Numerator / after operand: 0.261864406779661 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MEAGHER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MEAGHER-JON-TESTER-2024.json](evidence/SENATE-MEAGHER-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MEAGHER-R-2026: PASS

MEAGHER: republican_share in 2026 (%)

Expected: None | Calculated: 66.98924731182797 | Display: 67.0
Numerator / after operand: 0.6698924731182796 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MEAGHER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MEAGHER-R-2026.json](evidence/SENATE-MEAGHER-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MEAGHER-SETH-BODNAR-2026: PASS

MEAGHER: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 24.731182795698924 | Display: 24.7
Numerator / after operand: 0.24731182795698925 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MEAGHER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MEAGHER-SETH-BODNAR-2026.json](evidence/SENATE-MEAGHER-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MEAGHER-ALANI-BANKHEAD-2026: PASS

MEAGHER: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 5.376344086021505 | Display: 5.4
Numerator / after operand: 0.053763440860215055 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MEAGHER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MEAGHER-ALANI-BANKHEAD-2026.json](evidence/SENATE-MEAGHER-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MINERAL-R-SHARE-CHANGE: PASS

SENATE: MINERAL, republican_share_change_pp

Expected: None | Calculated: -3.0233509901559596 | Display: -3.0
Numerator / after operand: -3.0233509901559596 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MINERAL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MINERAL-R-SHARE-CHANGE.json](evidence/SENATE-MINERAL-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MINERAL-TWO-PARTY-CHANGE: PASS

SENATE: MINERAL, republican_two_party_share_change_pp

Expected: None | Calculated: 20.375327237227246 | Display: 20.4
Numerator / after operand: 20.375327237227246 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MINERAL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MINERAL-TWO-PARTY-CHANGE.json](evidence/SENATE-MINERAL-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MINERAL-R-2024: PASS

MINERAL: republican_share in 2024 (%)

Expected: None | Calculated: 64.26816426816427 | Display: 64.3
Numerator / after operand: 0.6426816426816426 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MINERAL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MINERAL-R-2024.json](evidence/SENATE-MINERAL-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MINERAL-JON-TESTER-2024: PASS

MINERAL: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 33.34503334503334 | Display: 33.3
Numerator / after operand: 0.3334503334503334 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MINERAL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MINERAL-JON-TESTER-2024.json](evidence/SENATE-MINERAL-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MINERAL-R-2026: PASS

MINERAL: republican_share in 2026 (%)

Expected: None | Calculated: 61.2448132780083 | Display: 61.2
Numerator / after operand: 0.612448132780083 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MINERAL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MINERAL-R-2026.json](evidence/SENATE-MINERAL-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MINERAL-SETH-BODNAR-2026: PASS

MINERAL: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 26.182572614107887 | Display: 26.2
Numerator / after operand: 0.26182572614107885 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MINERAL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MINERAL-SETH-BODNAR-2026.json](evidence/SENATE-MINERAL-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MINERAL-ALANI-BANKHEAD-2026: PASS

MINERAL: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 9.792531120331951 | Display: 9.8
Numerator / after operand: 0.0979253112033195 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MINERAL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MINERAL-ALANI-BANKHEAD-2026.json](evidence/SENATE-MINERAL-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MISSOULA-R-SHARE-CHANGE: PASS

SENATE: MISSOULA, republican_share_change_pp

Expected: None | Calculated: -5.454535518284359 | Display: -5.5
Numerator / after operand: -5.454535518284359 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MISSOULA-R-SHARE-CHANGE.json](evidence/SENATE-MISSOULA-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MISSOULA-TWO-PARTY-CHANGE: PASS

SENATE: MISSOULA, republican_two_party_share_change_pp

Expected: None | Calculated: 34.835859431844604 | Display: 34.8
Numerator / after operand: 34.835859431844604 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MISSOULA-TWO-PARTY-CHANGE.json](evidence/SENATE-MISSOULA-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MISSOULA-R-2024: PASS

MISSOULA: republican_share in 2024 (%)

Expected: None | Calculated: 32.35975576514202 | Display: 32.4
Numerator / after operand: 0.3235975576514202 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MISSOULA-R-2024.json](evidence/SENATE-MISSOULA-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MISSOULA-JON-TESTER-2024: PASS

MISSOULA: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 66.00474295371531 | Display: 66.0
Numerator / after operand: 0.6600474295371531 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MISSOULA-JON-TESTER-2024.json](evidence/SENATE-MISSOULA-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MISSOULA-R-2026: PASS

MISSOULA: republican_share in 2026 (%)

Expected: None | Calculated: 26.90522024685766 | Display: 26.9
Numerator / after operand: 0.2690522024685766 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MISSOULA-R-2026.json](evidence/SENATE-MISSOULA-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MISSOULA-SETH-BODNAR-2026: PASS

MISSOULA: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 59.11642428458192 | Display: 59.1
Numerator / after operand: 0.5911642428458191 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MISSOULA-SETH-BODNAR-2026.json](evidence/SENATE-MISSOULA-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MISSOULA-ALANI-BANKHEAD-2026: PASS

MISSOULA: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 12.816862675315852 | Display: 12.8
Numerator / after operand: 0.12816862675315852 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MISSOULA-ALANI-BANKHEAD-2026.json](evidence/SENATE-MISSOULA-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MUSSELSHELL-R-SHARE-CHANGE: PASS

SENATE: MUSSELSHELL, republican_share_change_pp

Expected: None | Calculated: -4.936749347752367 | Display: -4.9
Numerator / after operand: -4.936749347752367 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MUSSELSHELL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MUSSELSHELL-R-SHARE-CHANGE.json](evidence/SENATE-MUSSELSHELL-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MUSSELSHELL-TWO-PARTY-CHANGE: PASS

SENATE: MUSSELSHELL, republican_two_party_share_change_pp

Expected: None | Calculated: 11.060018421111039 | Display: 11.1
Numerator / after operand: 11.060018421111039 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "MUSSELSHELL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MUSSELSHELL-TWO-PARTY-CHANGE.json](evidence/SENATE-MUSSELSHELL-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MUSSELSHELL-R-2024: PASS

MUSSELSHELL: republican_share in 2024 (%)

Expected: None | Calculated: 80.13311148086522 | Display: 80.1
Numerator / after operand: 0.8013311148086523 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MUSSELSHELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MUSSELSHELL-R-2024.json](evidence/SENATE-MUSSELSHELL-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MUSSELSHELL-JON-TESTER-2024: PASS

MUSSELSHELL: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 17.8369384359401 | Display: 17.8
Numerator / after operand: 0.178369384359401 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "MUSSELSHELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-MUSSELSHELL-JON-TESTER-2024.json](evidence/SENATE-MUSSELSHELL-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MUSSELSHELL-R-2026: PASS

MUSSELSHELL: republican_share in 2026 (%)

Expected: None | Calculated: 75.19636213311286 | Display: 75.2
Numerator / after operand: 0.7519636213311286 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MUSSELSHELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MUSSELSHELL-R-2026.json](evidence/SENATE-MUSSELSHELL-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MUSSELSHELL-SETH-BODNAR-2026: PASS

MUSSELSHELL: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 16.329061595700704 | Display: 16.3
Numerator / after operand: 0.16329061595700703 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MUSSELSHELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MUSSELSHELL-SETH-BODNAR-2026.json](evidence/SENATE-MUSSELSHELL-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MUSSELSHELL-ALANI-BANKHEAD-2026: PASS

MUSSELSHELL: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 5.787515502273667 | Display: 5.8
Numerator / after operand: 0.05787515502273667 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "MUSSELSHELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MUSSELSHELL-ALANI-BANKHEAD-2026.json](evidence/SENATE-MUSSELSHELL-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PARK-R-SHARE-CHANGE: PASS

SENATE: PARK, republican_share_change_pp

Expected: None | Calculated: -5.368247924999137 | Display: -5.4
Numerator / after operand: -5.368247924999137 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PARK"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PARK-R-SHARE-CHANGE.json](evidence/SENATE-PARK-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PARK-TWO-PARTY-CHANGE: PASS

SENATE: PARK, republican_two_party_share_change_pp

Expected: None | Calculated: 29.018804698469353 | Display: 29.0
Numerator / after operand: 29.018804698469353 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PARK"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PARK-TWO-PARTY-CHANGE.json](evidence/SENATE-PARK-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PARK-R-2024: PASS

PARK: republican_share in 2024 (%)

Expected: None | Calculated: 47.51184834123222 | Display: 47.5
Numerator / after operand: 0.47511848341232227 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PARK-R-2024.json](evidence/SENATE-PARK-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PARK-JON-TESTER-2024: PASS

PARK: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 50.85477318889641 | Display: 50.9
Numerator / after operand: 0.5085477318889641 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PARK-JON-TESTER-2024.json](evidence/SENATE-PARK-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PARK-R-2026: PASS

PARK: republican_share in 2026 (%)

Expected: None | Calculated: 42.14360041623309 | Display: 42.1
Numerator / after operand: 0.4214360041623309 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PARK-R-2026.json](evidence/SENATE-PARK-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PARK-SETH-BODNAR-2026: PASS

PARK: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 44.172736732570236 | Display: 44.2
Numerator / after operand: 0.4417273673257024 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PARK-SETH-BODNAR-2026.json](evidence/SENATE-PARK-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PARK-ALANI-BANKHEAD-2026: PASS

PARK: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 12.362122788761706 | Display: 12.4
Numerator / after operand: 0.12362122788761706 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PARK"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PARK-ALANI-BANKHEAD-2026.json](evidence/SENATE-PARK-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PETROLEUM-R-SHARE-CHANGE: PASS

SENATE: PETROLEUM, republican_share_change_pp

Expected: None | Calculated: -3.936585365853651 | Display: -3.9
Numerator / after operand: -3.936585365853651 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PETROLEUM"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PETROLEUM-R-SHARE-CHANGE.json](evidence/SENATE-PETROLEUM-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PETROLEUM-TWO-PARTY-CHANGE: PASS

SENATE: PETROLEUM, republican_two_party_share_change_pp

Expected: None | Calculated: 13.461655415678408 | Display: 13.5
Numerator / after operand: 13.461655415678408 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PETROLEUM"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PETROLEUM-TWO-PARTY-CHANGE.json](evidence/SENATE-PETROLEUM-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PETROLEUM-R-2024: PASS

PETROLEUM: republican_share in 2024 (%)

Expected: None | Calculated: 83.53658536585365 | Display: 83.5
Numerator / after operand: 0.8353658536585366 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PETROLEUM"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PETROLEUM-R-2024.json](evidence/SENATE-PETROLEUM-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PETROLEUM-JON-TESTER-2024: PASS

PETROLEUM: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 15.24390243902439 | Display: 15.2
Numerator / after operand: 0.1524390243902439 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PETROLEUM"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PETROLEUM-JON-TESTER-2024.json](evidence/SENATE-PETROLEUM-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PETROLEUM-R-2026: PASS

PETROLEUM: republican_share in 2026 (%)

Expected: None | Calculated: 79.60000000000001 | Display: 79.6
Numerator / after operand: 0.796 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PETROLEUM"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PETROLEUM-R-2026.json](evidence/SENATE-PETROLEUM-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PETROLEUM-SETH-BODNAR-2026: PASS

PETROLEUM: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 14.399999999999999 | Display: 14.4
Numerator / after operand: 0.144 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PETROLEUM"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PETROLEUM-SETH-BODNAR-2026.json](evidence/SENATE-PETROLEUM-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PETROLEUM-ALANI-BANKHEAD-2026: PASS

PETROLEUM: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 1.6 | Display: 1.6
Numerator / after operand: 0.016 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PETROLEUM"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PETROLEUM-ALANI-BANKHEAD-2026.json](evidence/SENATE-PETROLEUM-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PHILLIPS-R-SHARE-CHANGE: PASS

SENATE: PHILLIPS, republican_share_change_pp

Expected: None | Calculated: -3.2163474507688083 | Display: -3.2
Numerator / after operand: -3.2163474507688083 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PHILLIPS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PHILLIPS-R-SHARE-CHANGE.json](evidence/SENATE-PHILLIPS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PHILLIPS-TWO-PARTY-CHANGE: PASS

SENATE: PHILLIPS, republican_two_party_share_change_pp

Expected: None | Calculated: 14.467147656551195 | Display: 14.5
Numerator / after operand: 14.467147656551195 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PHILLIPS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PHILLIPS-TWO-PARTY-CHANGE.json](evidence/SENATE-PHILLIPS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PHILLIPS-R-2024: PASS

PHILLIPS: republican_share in 2024 (%)

Expected: None | Calculated: 76.27272727272727 | Display: 76.3
Numerator / after operand: 0.7627272727272727 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PHILLIPS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PHILLIPS-R-2024.json](evidence/SENATE-PHILLIPS-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PHILLIPS-JON-TESTER-2024: PASS

PHILLIPS: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 22.272727272727273 | Display: 22.3
Numerator / after operand: 0.22272727272727272 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PHILLIPS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PHILLIPS-JON-TESTER-2024.json](evidence/SENATE-PHILLIPS-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PHILLIPS-R-2026: PASS

PHILLIPS: republican_share in 2026 (%)

Expected: None | Calculated: 73.05637982195846 | Display: 73.1
Numerator / after operand: 0.7305637982195846 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PHILLIPS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PHILLIPS-R-2026.json](evidence/SENATE-PHILLIPS-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PHILLIPS-SETH-BODNAR-2026: PASS

PHILLIPS: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 18.45697329376855 | Display: 18.5
Numerator / after operand: 0.18456973293768547 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PHILLIPS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PHILLIPS-SETH-BODNAR-2026.json](evidence/SENATE-PHILLIPS-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PHILLIPS-ALANI-BANKHEAD-2026: PASS

PHILLIPS: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 6.468842729970327 | Display: 6.5
Numerator / after operand: 0.06468842729970327 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PHILLIPS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PHILLIPS-ALANI-BANKHEAD-2026.json](evidence/SENATE-PHILLIPS-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PONDERA-R-SHARE-CHANGE: PASS

SENATE: PONDERA, republican_share_change_pp

Expected: None | Calculated: -2.3008637445742885 | Display: -2.3
Numerator / after operand: -2.3008637445742885 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PONDERA-R-SHARE-CHANGE.json](evidence/SENATE-PONDERA-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PONDERA-TWO-PARTY-CHANGE: PASS

SENATE: PONDERA, republican_two_party_share_change_pp

Expected: None | Calculated: 21.65710633452569 | Display: 21.7
Numerator / after operand: 21.65710633452569 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PONDERA-TWO-PARTY-CHANGE.json](evidence/SENATE-PONDERA-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PONDERA-R-2024: PASS

PONDERA: republican_share in 2024 (%)

Expected: None | Calculated: 62.94487090020935 | Display: 62.9
Numerator / after operand: 0.6294487090020935 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PONDERA-R-2024.json](evidence/SENATE-PONDERA-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PONDERA-JON-TESTER-2024: PASS

PONDERA: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 35.48499651081647 | Display: 35.5
Numerator / after operand: 0.3548499651081647 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PONDERA-JON-TESTER-2024.json](evidence/SENATE-PONDERA-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PONDERA-R-2026: PASS

PONDERA: republican_share in 2026 (%)

Expected: None | Calculated: 60.64400715563506 | Display: 60.6
Numerator / after operand: 0.6064400715563506 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PONDERA-R-2026.json](evidence/SENATE-PONDERA-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PONDERA-SETH-BODNAR-2026: PASS

PONDERA: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 26.610017889087658 | Display: 26.6
Numerator / after operand: 0.26610017889087656 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PONDERA-SETH-BODNAR-2026.json](evidence/SENATE-PONDERA-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PONDERA-ALANI-BANKHEAD-2026: PASS

PONDERA: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 10.196779964221825 | Display: 10.2
Numerator / after operand: 0.10196779964221825 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PONDERA-ALANI-BANKHEAD-2026.json](evidence/SENATE-PONDERA-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWDER-RIVER-R-SHARE-CHANGE: PASS

SENATE: POWDER RIVER, republican_share_change_pp

Expected: None | Calculated: -4.395131258098406 | Display: -4.4
Numerator / after operand: -4.395131258098406 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "POWDER RIVER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWDER-RIVER-R-SHARE-CHANGE.json](evidence/SENATE-POWDER-RIVER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWDER-RIVER-TWO-PARTY-CHANGE: PASS

SENATE: POWDER RIVER, republican_two_party_share_change_pp

Expected: None | Calculated: 12.725220712096274 | Display: 12.7
Numerator / after operand: 12.725220712096274 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "POWDER RIVER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWDER-RIVER-TWO-PARTY-CHANGE.json](evidence/SENATE-POWDER-RIVER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWDER-RIVER-R-2024: PASS

POWDER RIVER: republican_share in 2024 (%)

Expected: None | Calculated: 79.81981981981981 | Display: 79.8
Numerator / after operand: 0.7981981981981981 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "POWDER RIVER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-POWDER-RIVER-R-2024.json](evidence/SENATE-POWDER-RIVER-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWDER-RIVER-JON-TESTER-2024: PASS

POWDER RIVER: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 18.46846846846847 | Display: 18.5
Numerator / after operand: 0.18468468468468469 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "POWDER RIVER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-POWDER-RIVER-JON-TESTER-2024.json](evidence/SENATE-POWDER-RIVER-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWDER-RIVER-R-2026: PASS

POWDER RIVER: republican_share in 2026 (%)

Expected: None | Calculated: 75.42468856172141 | Display: 75.4
Numerator / after operand: 0.7542468856172141 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "POWDER RIVER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWDER-RIVER-R-2026.json](evidence/SENATE-POWDER-RIVER-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWDER-RIVER-SETH-BODNAR-2026: PASS

POWDER RIVER: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 17.10079275198188 | Display: 17.1
Numerator / after operand: 0.1710079275198188 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "POWDER RIVER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWDER-RIVER-SETH-BODNAR-2026.json](evidence/SENATE-POWDER-RIVER-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWDER-RIVER-ALANI-BANKHEAD-2026: PASS

POWDER RIVER: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 4.8697621744054365 | Display: 4.9
Numerator / after operand: 0.04869762174405436 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "POWDER RIVER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWDER-RIVER-ALANI-BANKHEAD-2026.json](evidence/SENATE-POWDER-RIVER-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWELL-R-SHARE-CHANGE: PASS

SENATE: POWELL, republican_share_change_pp

Expected: None | Calculated: 0.8243585245355289 | Display: 0.8
Numerator / after operand: 0.8243585245355289 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "POWELL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWELL-R-SHARE-CHANGE.json](evidence/SENATE-POWELL-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWELL-TWO-PARTY-CHANGE: PASS

SENATE: POWELL, republican_two_party_share_change_pp

Expected: None | Calculated: 22.821287921669697 | Display: 22.8
Numerator / after operand: 22.821287921669697 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "POWELL"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWELL-TWO-PARTY-CHANGE.json](evidence/SENATE-POWELL-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWELL-R-2024: PASS

POWELL: republican_share in 2024 (%)

Expected: None | Calculated: 65.43471675249924 | Display: 65.4
Numerator / after operand: 0.6543471675249924 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "POWELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-POWELL-R-2024.json](evidence/SENATE-POWELL-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWELL-JON-TESTER-2024: PASS

POWELL: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 32.26295062102393 | Display: 32.3
Numerator / after operand: 0.32262950621023934 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "POWELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-POWELL-JON-TESTER-2024.json](evidence/SENATE-POWELL-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWELL-R-2026: PASS

POWELL: republican_share in 2026 (%)

Expected: None | Calculated: 66.25907527703477 | Display: 66.3
Numerator / after operand: 0.6625907527703477 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "POWELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWELL-R-2026.json](evidence/SENATE-POWELL-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWELL-SETH-BODNAR-2026: PASS

POWELL: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 24.11157814291173 | Display: 24.1
Numerator / after operand: 0.2411157814291173 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "POWELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWELL-SETH-BODNAR-2026.json](evidence/SENATE-POWELL-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWELL-ALANI-BANKHEAD-2026: PASS

POWELL: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 7.527703477264043 | Display: 7.5
Numerator / after operand: 0.07527703477264043 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "POWELL"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWELL-ALANI-BANKHEAD-2026.json](evidence/SENATE-POWELL-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PRAIRIE-R-SHARE-CHANGE: PASS

SENATE: PRAIRIE, republican_share_change_pp

Expected: None | Calculated: -1.3187843084750295 | Display: -1.3
Numerator / after operand: -1.3187843084750295 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PRAIRIE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PRAIRIE-R-SHARE-CHANGE.json](evidence/SENATE-PRAIRIE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PRAIRIE-TWO-PARTY-CHANGE: PASS

SENATE: PRAIRIE, republican_two_party_share_change_pp

Expected: None | Calculated: 17.671595362178326 | Display: 17.7
Numerator / after operand: 17.671595362178326 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "PRAIRIE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PRAIRIE-TWO-PARTY-CHANGE.json](evidence/SENATE-PRAIRIE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PRAIRIE-R-2024: PASS

PRAIRIE: republican_share in 2024 (%)

Expected: None | Calculated: 70.56277056277057 | Display: 70.6
Numerator / after operand: 0.7056277056277056 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PRAIRIE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PRAIRIE-R-2024.json](evidence/SENATE-PRAIRIE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PRAIRIE-JON-TESTER-2024: PASS

PRAIRIE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 25.97402597402597 | Display: 26.0
Numerator / after operand: 0.2597402597402597 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "PRAIRIE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-PRAIRIE-JON-TESTER-2024.json](evidence/SENATE-PRAIRIE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PRAIRIE-R-2026: PASS

PRAIRIE: republican_share in 2026 (%)

Expected: None | Calculated: 69.24398625429554 | Display: 69.2
Numerator / after operand: 0.6924398625429553 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PRAIRIE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PRAIRIE-R-2026.json](evidence/SENATE-PRAIRIE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PRAIRIE-SETH-BODNAR-2026: PASS

PRAIRIE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 20.103092783505154 | Display: 20.1
Numerator / after operand: 0.20103092783505155 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PRAIRIE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PRAIRIE-SETH-BODNAR-2026.json](evidence/SENATE-PRAIRIE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PRAIRIE-ALANI-BANKHEAD-2026: PASS

PRAIRIE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 7.0446735395189 | Display: 7.0
Numerator / after operand: 0.070446735395189 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "PRAIRIE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PRAIRIE-ALANI-BANKHEAD-2026.json](evidence/SENATE-PRAIRIE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RAVALLI-R-SHARE-CHANGE: PASS

SENATE: RAVALLI, republican_share_change_pp

Expected: None | Calculated: -4.107952829324935 | Display: -4.1
Numerator / after operand: -4.107952829324935 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "RAVALLI"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RAVALLI-R-SHARE-CHANGE.json](evidence/SENATE-RAVALLI-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RAVALLI-TWO-PARTY-CHANGE: PASS

SENATE: RAVALLI, republican_two_party_share_change_pp

Expected: None | Calculated: 22.627999435924206 | Display: 22.6
Numerator / after operand: 22.627999435924206 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "RAVALLI"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RAVALLI-TWO-PARTY-CHANGE.json](evidence/SENATE-RAVALLI-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RAVALLI-R-2024: PASS

RAVALLI: republican_share in 2024 (%)

Expected: None | Calculated: 63.62032815256099 | Display: 63.6
Numerator / after operand: 0.6362032815256099 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "RAVALLI"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-RAVALLI-R-2024.json](evidence/SENATE-RAVALLI-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RAVALLI-JON-TESTER-2024: PASS

RAVALLI: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 34.77551835457783 | Display: 34.8
Numerator / after operand: 0.3477551835457783 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "RAVALLI"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-RAVALLI-JON-TESTER-2024.json](evidence/SENATE-RAVALLI-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RAVALLI-R-2026: PASS

RAVALLI: republican_share in 2026 (%)

Expected: None | Calculated: 59.51237532323606 | Display: 59.5
Numerator / after operand: 0.5951237532323606 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "RAVALLI"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RAVALLI-R-2026.json](evidence/SENATE-RAVALLI-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RAVALLI-SETH-BODNAR-2026: PASS

RAVALLI: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 30.168698436153186 | Display: 30.2
Numerator / after operand: 0.30168698436153185 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "RAVALLI"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RAVALLI-SETH-BODNAR-2026.json](evidence/SENATE-RAVALLI-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RAVALLI-ALANI-BANKHEAD-2026: PASS

RAVALLI: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 8.66888314247014 | Display: 8.7
Numerator / after operand: 0.08668883142470139 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "RAVALLI"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RAVALLI-ALANI-BANKHEAD-2026.json](evidence/SENATE-RAVALLI-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RICHLAND-R-SHARE-CHANGE: PASS

SENATE: RICHLAND, republican_share_change_pp

Expected: None | Calculated: -0.870158275464461 | Display: -0.9
Numerator / after operand: -0.870158275464461 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "RICHLAND"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RICHLAND-R-SHARE-CHANGE.json](evidence/SENATE-RICHLAND-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RICHLAND-TWO-PARTY-CHANGE: PASS

SENATE: RICHLAND, republican_two_party_share_change_pp

Expected: None | Calculated: 13.60232517084402 | Display: 13.6
Numerator / after operand: 13.60232517084402 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "RICHLAND"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RICHLAND-TWO-PARTY-CHANGE.json](evidence/SENATE-RICHLAND-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RICHLAND-R-2024: PASS

RICHLAND: republican_share in 2024 (%)

Expected: None | Calculated: 73.84905660377359 | Display: 73.8
Numerator / after operand: 0.7384905660377359 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "RICHLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-RICHLAND-R-2024.json](evidence/SENATE-RICHLAND-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RICHLAND-JON-TESTER-2024: PASS

RICHLAND: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 23.358490566037734 | Display: 23.4
Numerator / after operand: 0.23358490566037735 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "RICHLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-RICHLAND-JON-TESTER-2024.json](evidence/SENATE-RICHLAND-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RICHLAND-R-2026: PASS

RICHLAND: republican_share in 2026 (%)

Expected: None | Calculated: 72.97889832830913 | Display: 73.0
Numerator / after operand: 0.7297889832830913 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "RICHLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RICHLAND-R-2026.json](evidence/SENATE-RICHLAND-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RICHLAND-SETH-BODNAR-2026: PASS

RICHLAND: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 15.648122773362566 | Display: 15.6
Numerator / after operand: 0.15648122773362566 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "RICHLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RICHLAND-SETH-BODNAR-2026.json](evidence/SENATE-RICHLAND-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RICHLAND-ALANI-BANKHEAD-2026: PASS

RICHLAND: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 8.495478213209099 | Display: 8.5
Numerator / after operand: 0.08495478213209098 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "RICHLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RICHLAND-ALANI-BANKHEAD-2026.json](evidence/SENATE-RICHLAND-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROOSEVELT-R-SHARE-CHANGE: PASS

SENATE: ROOSEVELT, republican_share_change_pp

Expected: None | Calculated: 2.413542906119903 | Display: 2.4
Numerator / after operand: 2.413542906119903 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "ROOSEVELT"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROOSEVELT-R-SHARE-CHANGE.json](evidence/SENATE-ROOSEVELT-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROOSEVELT-TWO-PARTY-CHANGE: PASS

SENATE: ROOSEVELT, republican_two_party_share_change_pp

Expected: None | Calculated: 19.99282373238967 | Display: 20.0
Numerator / after operand: 19.99282373238967 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "ROOSEVELT"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROOSEVELT-TWO-PARTY-CHANGE.json](evidence/SENATE-ROOSEVELT-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROOSEVELT-R-2024: PASS

ROOSEVELT: republican_share in 2024 (%)

Expected: None | Calculated: 41.33400707427994 | Display: 41.3
Numerator / after operand: 0.4133400707427994 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "ROOSEVELT"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-ROOSEVELT-R-2024.json](evidence/SENATE-ROOSEVELT-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROOSEVELT-JON-TESTER-2024: PASS

ROOSEVELT: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 56.82162708438605 | Display: 56.8
Numerator / after operand: 0.5682162708438605 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "ROOSEVELT"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-ROOSEVELT-JON-TESTER-2024.json](evidence/SENATE-ROOSEVELT-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROOSEVELT-R-2026: PASS

ROOSEVELT: republican_share in 2026 (%)

Expected: None | Calculated: 43.74754998039984 | Display: 43.7
Numerator / after operand: 0.4374754998039984 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "ROOSEVELT"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROOSEVELT-R-2026.json](evidence/SENATE-ROOSEVELT-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROOSEVELT-SETH-BODNAR-2026: PASS

ROOSEVELT: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 27.597020776166207 | Display: 27.6
Numerator / after operand: 0.2759702077616621 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "ROOSEVELT"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROOSEVELT-SETH-BODNAR-2026.json](evidence/SENATE-ROOSEVELT-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROOSEVELT-ALANI-BANKHEAD-2026: PASS

ROOSEVELT: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 26.695413563308506 | Display: 26.7
Numerator / after operand: 0.26695413563308507 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "ROOSEVELT"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROOSEVELT-ALANI-BANKHEAD-2026.json](evidence/SENATE-ROOSEVELT-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROSEBUD-R-SHARE-CHANGE: PASS

SENATE: ROSEBUD, republican_share_change_pp

Expected: None | Calculated: -0.6741016948369705 | Display: -0.7
Numerator / after operand: -0.6741016948369705 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "ROSEBUD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROSEBUD-R-SHARE-CHANGE.json](evidence/SENATE-ROSEBUD-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROSEBUD-TWO-PARTY-CHANGE: PASS

SENATE: ROSEBUD, republican_two_party_share_change_pp

Expected: None | Calculated: 21.108893851139253 | Display: 21.1
Numerator / after operand: 21.108893851139253 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "ROSEBUD"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROSEBUD-TWO-PARTY-CHANGE.json](evidence/SENATE-ROSEBUD-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROSEBUD-R-2024: PASS

ROSEBUD: republican_share in 2024 (%)

Expected: None | Calculated: 59.29108485499462 | Display: 59.3
Numerator / after operand: 0.5929108485499462 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "ROSEBUD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-ROSEBUD-R-2024.json](evidence/SENATE-ROSEBUD-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROSEBUD-JON-TESTER-2024: PASS

ROSEBUD: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 38.53383458646616 | Display: 38.5
Numerator / after operand: 0.38533834586466165 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "ROSEBUD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-ROSEBUD-JON-TESTER-2024.json](evidence/SENATE-ROSEBUD-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROSEBUD-R-2026: PASS

ROSEBUD: republican_share in 2026 (%)

Expected: None | Calculated: 58.61698316015765 | Display: 58.6
Numerator / after operand: 0.5861698316015765 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "ROSEBUD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROSEBUD-R-2026.json](evidence/SENATE-ROSEBUD-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROSEBUD-SETH-BODNAR-2026: PASS

ROSEBUD: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 25.546399140093158 | Display: 25.5
Numerator / after operand: 0.25546399140093157 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "ROSEBUD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROSEBUD-SETH-BODNAR-2026.json](evidence/SENATE-ROSEBUD-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROSEBUD-ALANI-BANKHEAD-2026: PASS

ROSEBUD: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 13.113579362235757 | Display: 13.1
Numerator / after operand: 0.13113579362235758 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "ROSEBUD"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROSEBUD-ALANI-BANKHEAD-2026.json](evidence/SENATE-ROSEBUD-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SANDERS-R-SHARE-CHANGE: PASS

SENATE: SANDERS, republican_share_change_pp

Expected: None | Calculated: -0.8488009388556539 | Display: -0.8
Numerator / after operand: -0.8488009388556539 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "SANDERS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SANDERS-R-SHARE-CHANGE.json](evidence/SENATE-SANDERS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SANDERS-TWO-PARTY-CHANGE: PASS

SENATE: SANDERS, republican_two_party_share_change_pp

Expected: None | Calculated: 16.375655429625414 | Display: 16.4
Numerator / after operand: 16.375655429625414 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "SANDERS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SANDERS-TWO-PARTY-CHANGE.json](evidence/SENATE-SANDERS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SANDERS-R-2024: PASS

SANDERS: republican_share in 2024 (%)

Expected: None | Calculated: 69.86183074265976 | Display: 69.9
Numerator / after operand: 0.6986183074265976 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "SANDERS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SANDERS-R-2024.json](evidence/SENATE-SANDERS-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SANDERS-JON-TESTER-2024: PASS

SANDERS: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 27.646188008882312 | Display: 27.6
Numerator / after operand: 0.2764618800888231 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "SANDERS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SANDERS-JON-TESTER-2024.json](evidence/SENATE-SANDERS-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SANDERS-R-2026: PASS

SANDERS: republican_share in 2026 (%)

Expected: None | Calculated: 69.0130298038041 | Display: 69.0
Numerator / after operand: 0.690130298038041 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SANDERS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SANDERS-R-2026.json](evidence/SENATE-SANDERS-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SANDERS-SETH-BODNAR-2026: PASS

SANDERS: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 19.904148569716938 | Display: 19.9
Numerator / after operand: 0.1990414856971694 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SANDERS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SANDERS-SETH-BODNAR-2026.json](evidence/SENATE-SANDERS-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SANDERS-ALANI-BANKHEAD-2026: PASS

SANDERS: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 9.390444810543658 | Display: 9.4
Numerator / after operand: 0.09390444810543658 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SANDERS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SANDERS-ALANI-BANKHEAD-2026.json](evidence/SENATE-SANDERS-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHERIDAN-R-SHARE-CHANGE: PASS

SENATE: SHERIDAN, republican_share_change_pp

Expected: None | Calculated: 0.14384196998116217 | Display: 0.1
Numerator / after operand: 0.14384196998116217 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "SHERIDAN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SHERIDAN-R-SHARE-CHANGE.json](evidence/SENATE-SHERIDAN-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHERIDAN-TWO-PARTY-CHANGE: PASS

SENATE: SHERIDAN, republican_two_party_share_change_pp

Expected: None | Calculated: 21.714856002832917 | Display: 21.7
Numerator / after operand: 21.714856002832917 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "SHERIDAN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SHERIDAN-TWO-PARTY-CHANGE.json](evidence/SENATE-SHERIDAN-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHERIDAN-R-2024: PASS

SHERIDAN: republican_share in 2024 (%)

Expected: None | Calculated: 61.096468107538215 | Display: 61.1
Numerator / after operand: 0.6109646810753822 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "SHERIDAN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SHERIDAN-R-2024.json](evidence/SENATE-SHERIDAN-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHERIDAN-JON-TESTER-2024: PASS

SHERIDAN: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 36.10964681075382 | Display: 36.1
Numerator / after operand: 0.3610964681075382 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "SHERIDAN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SHERIDAN-JON-TESTER-2024.json](evidence/SENATE-SHERIDAN-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHERIDAN-R-2026: PASS

SHERIDAN: republican_share in 2026 (%)

Expected: None | Calculated: 61.240310077519375 | Display: 61.2
Numerator / after operand: 0.6124031007751938 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SHERIDAN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SHERIDAN-R-2026.json](evidence/SENATE-SHERIDAN-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHERIDAN-SETH-BODNAR-2026: PASS

SHERIDAN: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 25.129198966408268 | Display: 25.1
Numerator / after operand: 0.25129198966408267 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SHERIDAN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SHERIDAN-SETH-BODNAR-2026.json](evidence/SENATE-SHERIDAN-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHERIDAN-ALANI-BANKHEAD-2026: PASS

SHERIDAN: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 11.175710594315245 | Display: 11.2
Numerator / after operand: 0.11175710594315245 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SHERIDAN"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SHERIDAN-ALANI-BANKHEAD-2026.json](evidence/SENATE-SHERIDAN-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SILVER-BOW-R-SHARE-CHANGE: PASS

SENATE: SILVER BOW, republican_share_change_pp

Expected: None | Calculated: -1.6410790902149253 | Display: -1.6
Numerator / after operand: -1.6410790902149253 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "SILVER BOW"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SILVER-BOW-R-SHARE-CHANGE.json](evidence/SENATE-SILVER-BOW-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SILVER-BOW-TWO-PARTY-CHANGE: PASS

SENATE: SILVER BOW, republican_two_party_share_change_pp

Expected: None | Calculated: 31.20912102887902 | Display: 31.2
Numerator / after operand: 31.20912102887902 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "SILVER BOW"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SILVER-BOW-TWO-PARTY-CHANGE.json](evidence/SENATE-SILVER-BOW-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SILVER-BOW-R-2024: PASS

SILVER BOW: republican_share in 2024 (%)

Expected: None | Calculated: 33.83646432837442 | Display: 33.8
Numerator / after operand: 0.33836464328374416 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "SILVER BOW"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SILVER-BOW-R-2024.json](evidence/SENATE-SILVER-BOW-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SILVER-BOW-JON-TESTER-2024: PASS

SILVER BOW: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 64.3609512433489 | Display: 64.4
Numerator / after operand: 0.643609512433489 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "SILVER BOW"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SILVER-BOW-JON-TESTER-2024.json](evidence/SENATE-SILVER-BOW-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SILVER-BOW-R-2026: PASS

SILVER BOW: republican_share in 2026 (%)

Expected: None | Calculated: 32.19538523815949 | Display: 32.2
Numerator / after operand: 0.3219538523815949 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SILVER BOW"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SILVER-BOW-R-2026.json](evidence/SENATE-SILVER-BOW-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SILVER-BOW-SETH-BODNAR-2026: PASS

SILVER BOW: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 48.731615166644175 | Display: 48.7
Numerator / after operand: 0.48731615166644177 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SILVER BOW"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SILVER-BOW-SETH-BODNAR-2026.json](evidence/SENATE-SILVER-BOW-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SILVER-BOW-ALANI-BANKHEAD-2026: PASS

SILVER BOW: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 16.833085953312644 | Display: 16.8
Numerator / after operand: 0.16833085953312643 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SILVER BOW"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SILVER-BOW-ALANI-BANKHEAD-2026.json](evidence/SENATE-SILVER-BOW-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-STILLWATER-R-SHARE-CHANGE: PASS

SENATE: STILLWATER, republican_share_change_pp

Expected: None | Calculated: -6.273672208758296 | Display: -6.3
Numerator / after operand: -6.273672208758296 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "STILLWATER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-STILLWATER-R-SHARE-CHANGE.json](evidence/SENATE-STILLWATER-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-STILLWATER-TWO-PARTY-CHANGE: PASS

SENATE: STILLWATER, republican_two_party_share_change_pp

Expected: None | Calculated: 15.567737231065792 | Display: 15.6
Numerator / after operand: 15.567737231065792 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "STILLWATER"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-STILLWATER-TWO-PARTY-CHANGE.json](evidence/SENATE-STILLWATER-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-STILLWATER-R-2024: PASS

STILLWATER: republican_share in 2024 (%)

Expected: None | Calculated: 75.40458530006742 | Display: 75.4
Numerator / after operand: 0.7540458530006743 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "STILLWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-STILLWATER-R-2024.json](evidence/SENATE-STILLWATER-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-STILLWATER-JON-TESTER-2024: PASS

STILLWATER: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 22.791638570465274 | Display: 22.8
Numerator / after operand: 0.22791638570465272 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "STILLWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-STILLWATER-JON-TESTER-2024.json](evidence/SENATE-STILLWATER-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-STILLWATER-R-2026: PASS

STILLWATER: republican_share in 2026 (%)

Expected: None | Calculated: 69.13091309130913 | Display: 69.1
Numerator / after operand: 0.6913091309130913 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "STILLWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-STILLWATER-R-2026.json](evidence/SENATE-STILLWATER-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-STILLWATER-SETH-BODNAR-2026: PASS

STILLWATER: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 22.37623762376238 | Display: 22.4
Numerator / after operand: 0.22376237623762377 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "STILLWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-STILLWATER-SETH-BODNAR-2026.json](evidence/SENATE-STILLWATER-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-STILLWATER-ALANI-BANKHEAD-2026: PASS

STILLWATER: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 5.720572057205721 | Display: 5.7
Numerator / after operand: 0.05720572057205721 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "STILLWATER"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-STILLWATER-ALANI-BANKHEAD-2026.json](evidence/SENATE-STILLWATER-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SWEET-GRASS-R-SHARE-CHANGE: PASS

SENATE: SWEET GRASS, republican_share_change_pp

Expected: None | Calculated: -7.215712325438151 | Display: -7.2
Numerator / after operand: -7.215712325438151 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "SWEET GRASS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SWEET-GRASS-R-SHARE-CHANGE.json](evidence/SENATE-SWEET-GRASS-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SWEET-GRASS-TWO-PARTY-CHANGE: PASS

SENATE: SWEET GRASS, republican_two_party_share_change_pp

Expected: None | Calculated: 17.825895939245594 | Display: 17.8
Numerator / after operand: 17.825895939245594 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "SWEET GRASS"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SWEET-GRASS-TWO-PARTY-CHANGE.json](evidence/SENATE-SWEET-GRASS-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SWEET-GRASS-R-2024: PASS

SWEET GRASS: republican_share in 2024 (%)

Expected: None | Calculated: 70.14987510407992 | Display: 70.1
Numerator / after operand: 0.7014987510407993 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "SWEET GRASS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SWEET-GRASS-R-2024.json](evidence/SENATE-SWEET-GRASS-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SWEET-GRASS-JON-TESTER-2024: PASS

SWEET GRASS: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 27.685262281432138 | Display: 27.7
Numerator / after operand: 0.2768526228143214 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "SWEET GRASS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SWEET-GRASS-JON-TESTER-2024.json](evidence/SENATE-SWEET-GRASS-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SWEET-GRASS-R-2026: PASS

SWEET GRASS: republican_share in 2026 (%)

Expected: None | Calculated: 62.93416277864178 | Display: 62.9
Numerator / after operand: 0.6293416277864178 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SWEET GRASS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SWEET-GRASS-R-2026.json](evidence/SENATE-SWEET-GRASS-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SWEET-GRASS-SETH-BODNAR-2026: PASS

SWEET GRASS: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 27.16433385173665 | Display: 27.2
Numerator / after operand: 0.2716433385173665 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SWEET GRASS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SWEET-GRASS-SETH-BODNAR-2026.json](evidence/SENATE-SWEET-GRASS-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SWEET-GRASS-ALANI-BANKHEAD-2026: PASS

SWEET GRASS: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 7.36132711249352 | Display: 7.4
Numerator / after operand: 0.0736132711249352 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "SWEET GRASS"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SWEET-GRASS-ALANI-BANKHEAD-2026.json](evidence/SENATE-SWEET-GRASS-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TETON-R-SHARE-CHANGE: PASS

SENATE: TETON, republican_share_change_pp

Expected: None | Calculated: -2.4008436905181285 | Display: -2.4
Numerator / after operand: -2.4008436905181285 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "TETON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TETON-R-SHARE-CHANGE.json](evidence/SENATE-TETON-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TETON-TWO-PARTY-CHANGE: PASS

SENATE: TETON, republican_two_party_share_change_pp

Expected: None | Calculated: 21.369792618940764 | Display: 21.4
Numerator / after operand: 21.369792618940764 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "TETON"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TETON-TWO-PARTY-CHANGE.json](evidence/SENATE-TETON-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TETON-R-2024: PASS

TETON: republican_share in 2024 (%)

Expected: None | Calculated: 64.420410427066 | Display: 64.4
Numerator / after operand: 0.64420410427066 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "TETON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-TETON-R-2024.json](evidence/SENATE-TETON-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TETON-JON-TESTER-2024: PASS

TETON: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 33.72157515252357 | Display: 33.7
Numerator / after operand: 0.3372157515252357 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "TETON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-TETON-JON-TESTER-2024.json](evidence/SENATE-TETON-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TETON-R-2026: PASS

TETON: republican_share in 2026 (%)

Expected: None | Calculated: 62.01956673654787 | Display: 62.0
Numerator / after operand: 0.6201956673654787 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "TETON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TETON-R-2026.json](evidence/SENATE-TETON-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TETON-SETH-BODNAR-2026: PASS

TETON: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 26.41509433962264 | Display: 26.4
Numerator / after operand: 0.2641509433962264 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "TETON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TETON-SETH-BODNAR-2026.json](evidence/SENATE-TETON-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TETON-ALANI-BANKHEAD-2026: PASS

TETON: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 9.25925925925926 | Display: 9.3
Numerator / after operand: 0.09259259259259259 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "TETON"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TETON-ALANI-BANKHEAD-2026.json](evidence/SENATE-TETON-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOOLE-R-SHARE-CHANGE: PASS

SENATE: TOOLE, republican_share_change_pp

Expected: None | Calculated: -1.4419031311154629 | Display: -1.4
Numerator / after operand: -1.4419031311154629 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "TOOLE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TOOLE-R-SHARE-CHANGE.json](evidence/SENATE-TOOLE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOOLE-TWO-PARTY-CHANGE: PASS

SENATE: TOOLE, republican_two_party_share_change_pp

Expected: None | Calculated: 16.27585241691394 | Display: 16.3
Numerator / after operand: 16.27585241691394 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "TOOLE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TOOLE-TWO-PARTY-CHANGE.json](evidence/SENATE-TOOLE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOOLE-R-2024: PASS

TOOLE: republican_share in 2024 (%)

Expected: None | Calculated: 70.25440313111547 | Display: 70.3
Numerator / after operand: 0.7025440313111546 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "TOOLE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-TOOLE-R-2024.json](evidence/SENATE-TOOLE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOOLE-JON-TESTER-2024: PASS

TOOLE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 27.299412915851274 | Display: 27.3
Numerator / after operand: 0.27299412915851273 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "TOOLE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-TOOLE-JON-TESTER-2024.json](evidence/SENATE-TOOLE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOOLE-R-2026: PASS

TOOLE: republican_share in 2026 (%)

Expected: None | Calculated: 68.8125 | Display: 68.8
Numerator / after operand: 0.688125 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "TOOLE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TOOLE-R-2026.json](evidence/SENATE-TOOLE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOOLE-SETH-BODNAR-2026: PASS

TOOLE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 19.875 | Display: 19.9
Numerator / after operand: 0.19875 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "TOOLE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TOOLE-SETH-BODNAR-2026.json](evidence/SENATE-TOOLE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOOLE-ALANI-BANKHEAD-2026: PASS

TOOLE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 9.125 | Display: 9.1
Numerator / after operand: 0.09125 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "TOOLE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TOOLE-ALANI-BANKHEAD-2026.json](evidence/SENATE-TOOLE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TREASURE-R-SHARE-CHANGE: PASS

SENATE: TREASURE, republican_share_change_pp

Expected: None | Calculated: 3.7795831861533014 | Display: 3.8
Numerator / after operand: 3.7795831861533014 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "TREASURE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TREASURE-R-SHARE-CHANGE.json](evidence/SENATE-TREASURE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TREASURE-TWO-PARTY-CHANGE: PASS

SENATE: TREASURE, republican_two_party_share_change_pp

Expected: None | Calculated: 18.429853898961458 | Display: 18.4
Numerator / after operand: 18.429853898961458 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "TREASURE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TREASURE-TWO-PARTY-CHANGE.json](evidence/SENATE-TREASURE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TREASURE-R-2024: PASS

TREASURE: republican_share in 2024 (%)

Expected: None | Calculated: 75.16778523489933 | Display: 75.2
Numerator / after operand: 0.7516778523489933 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "TREASURE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-TREASURE-R-2024.json](evidence/SENATE-TREASURE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TREASURE-JON-TESTER-2024: PASS

TREASURE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 22.595078299776286 | Display: 22.6
Numerator / after operand: 0.22595078299776286 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "TREASURE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-TREASURE-JON-TESTER-2024.json](evidence/SENATE-TREASURE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TREASURE-R-2026: PASS

TREASURE: republican_share in 2026 (%)

Expected: None | Calculated: 78.94736842105263 | Display: 78.9
Numerator / after operand: 0.7894736842105263 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "TREASURE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TREASURE-R-2026.json](evidence/SENATE-TREASURE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TREASURE-SETH-BODNAR-2026: PASS

TREASURE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 14.681440443213297 | Display: 14.7
Numerator / after operand: 0.14681440443213298 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "TREASURE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TREASURE-SETH-BODNAR-2026.json](evidence/SENATE-TREASURE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TREASURE-ALANI-BANKHEAD-2026: PASS

TREASURE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 3.8781163434903045 | Display: 3.9
Numerator / after operand: 0.038781163434903045 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "TREASURE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TREASURE-ALANI-BANKHEAD-2026.json](evidence/SENATE-TREASURE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-VALLEY-R-SHARE-CHANGE: PASS

SENATE: VALLEY, republican_share_change_pp

Expected: None | Calculated: -2.794274182303025 | Display: -2.8
Numerator / after operand: -2.794274182303025 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "VALLEY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-VALLEY-R-SHARE-CHANGE.json](evidence/SENATE-VALLEY-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-VALLEY-TWO-PARTY-CHANGE: PASS

SENATE: VALLEY, republican_two_party_share_change_pp

Expected: None | Calculated: 21.792403236256398 | Display: 21.8
Numerator / after operand: 21.792403236256398 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "VALLEY"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-VALLEY-TWO-PARTY-CHANGE.json](evidence/SENATE-VALLEY-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-VALLEY-R-2024: PASS

VALLEY: republican_share in 2024 (%)

Expected: None | Calculated: 65.28218910334718 | Display: 65.3
Numerator / after operand: 0.6528218910334718 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-VALLEY-R-2024.json](evidence/SENATE-VALLEY-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-VALLEY-JON-TESTER-2024: PASS

VALLEY: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 31.932567798680672 | Display: 31.9
Numerator / after operand: 0.3193256779868067 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-VALLEY-JON-TESTER-2024.json](evidence/SENATE-VALLEY-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-VALLEY-R-2026: PASS

VALLEY: republican_share in 2026 (%)

Expected: None | Calculated: 62.48791492104415 | Display: 62.5
Numerator / after operand: 0.6248791492104415 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-VALLEY-R-2026.json](evidence/SENATE-VALLEY-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-VALLEY-SETH-BODNAR-2026: PASS

VALLEY: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 27.231711247180147 | Display: 27.2
Numerator / after operand: 0.27231711247180146 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-VALLEY-SETH-BODNAR-2026.json](evidence/SENATE-VALLEY-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-VALLEY-ALANI-BANKHEAD-2026: PASS

VALLEY: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 7.7666774089590715 | Display: 7.8
Numerator / after operand: 0.07766677408959072 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "VALLEY"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-VALLEY-ALANI-BANKHEAD-2026.json](evidence/SENATE-VALLEY-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WHEATLAND-R-SHARE-CHANGE: PASS

SENATE: WHEATLAND, republican_share_change_pp

Expected: None | Calculated: -4.5193498501677976 | Display: -4.5
Numerator / after operand: -4.5193498501677976 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "WHEATLAND"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WHEATLAND-R-SHARE-CHANGE.json](evidence/SENATE-WHEATLAND-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WHEATLAND-TWO-PARTY-CHANGE: PASS

SENATE: WHEATLAND, republican_two_party_share_change_pp

Expected: None | Calculated: 17.01685709745916 | Display: 17.0
Numerator / after operand: 17.01685709745916 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "WHEATLAND"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WHEATLAND-TWO-PARTY-CHANGE.json](evidence/SENATE-WHEATLAND-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WHEATLAND-R-2024: PASS

WHEATLAND: republican_share in 2024 (%)

Expected: None | Calculated: 72.92817679558011 | Display: 72.9
Numerator / after operand: 0.7292817679558011 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "WHEATLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-WHEATLAND-R-2024.json](evidence/SENATE-WHEATLAND-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WHEATLAND-JON-TESTER-2024: PASS

WHEATLAND: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 25.59852670349908 | Display: 25.6
Numerator / after operand: 0.2559852670349908 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "WHEATLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-WHEATLAND-JON-TESTER-2024.json](evidence/SENATE-WHEATLAND-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WHEATLAND-R-2026: PASS

WHEATLAND: republican_share in 2026 (%)

Expected: None | Calculated: 68.40882694541232 | Display: 68.4
Numerator / after operand: 0.6840882694541232 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "WHEATLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WHEATLAND-R-2026.json](evidence/SENATE-WHEATLAND-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WHEATLAND-SETH-BODNAR-2026: PASS

WHEATLAND: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 23.228803716608596 | Display: 23.2
Numerator / after operand: 0.23228803716608595 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "WHEATLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WHEATLAND-SETH-BODNAR-2026.json](evidence/SENATE-WHEATLAND-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WHEATLAND-ALANI-BANKHEAD-2026: PASS

WHEATLAND: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 6.736353077816492 | Display: 6.7
Numerator / after operand: 0.06736353077816493 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "WHEATLAND"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WHEATLAND-ALANI-BANKHEAD-2026.json](evidence/SENATE-WHEATLAND-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WIBAUX-R-SHARE-CHANGE: PASS

SENATE: WIBAUX, republican_share_change_pp

Expected: None | Calculated: 1.769215332129248 | Display: 1.8
Numerator / after operand: 1.769215332129248 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "WIBAUX"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WIBAUX-R-SHARE-CHANGE.json](evidence/SENATE-WIBAUX-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WIBAUX-TWO-PARTY-CHANGE: PASS

SENATE: WIBAUX, republican_two_party_share_change_pp

Expected: None | Calculated: 15.435971366076762 | Display: 15.4
Numerator / after operand: 15.435971366076762 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "WIBAUX"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WIBAUX-TWO-PARTY-CHANGE.json](evidence/SENATE-WIBAUX-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WIBAUX-R-2024: PASS

WIBAUX: republican_share in 2024 (%)

Expected: None | Calculated: 75.27272727272727 | Display: 75.3
Numerator / after operand: 0.7527272727272727 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "WIBAUX"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-WIBAUX-R-2024.json](evidence/SENATE-WIBAUX-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WIBAUX-JON-TESTER-2024: PASS

WIBAUX: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 22.0 | Display: 22.0
Numerator / after operand: 0.22 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "WIBAUX"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-WIBAUX-JON-TESTER-2024.json](evidence/SENATE-WIBAUX-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WIBAUX-R-2026: PASS

WIBAUX: republican_share in 2026 (%)

Expected: None | Calculated: 77.04194260485652 | Display: 77.0
Numerator / after operand: 0.7704194260485652 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "WIBAUX"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WIBAUX-R-2026.json](evidence/SENATE-WIBAUX-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WIBAUX-SETH-BODNAR-2026: PASS

WIBAUX: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 13.46578366445916 | Display: 13.5
Numerator / after operand: 0.1346578366445916 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "WIBAUX"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WIBAUX-SETH-BODNAR-2026.json](evidence/SENATE-WIBAUX-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WIBAUX-ALANI-BANKHEAD-2026: PASS

WIBAUX: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 5.960264900662252 | Display: 6.0
Numerator / after operand: 0.059602649006622516 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "WIBAUX"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WIBAUX-ALANI-BANKHEAD-2026.json](evidence/SENATE-WIBAUX-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-YELLOWSTONE-R-SHARE-CHANGE: PASS

SENATE: YELLOWSTONE, republican_share_change_pp

Expected: None | Calculated: -5.797491757880713 | Display: -5.8
Numerator / after operand: -5.797491757880713 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "YELLOWSTONE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-YELLOWSTONE-R-SHARE-CHANGE.json](evidence/SENATE-YELLOWSTONE-R-SHARE-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-YELLOWSTONE-TWO-PARTY-CHANGE: PASS

SENATE: YELLOWSTONE, republican_two_party_share_change_pp

Expected: None | Calculated: 21.099067128315397 | Display: 21.1
Numerator / after operand: 21.099067128315397 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_two_party_share_change_pp", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "county", "op": "eq", "value": "YELLOWSTONE"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-YELLOWSTONE-TWO-PARTY-CHANGE.json](evidence/SENATE-YELLOWSTONE-TWO-PARTY-CHANGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-YELLOWSTONE-R-2024: PASS

YELLOWSTONE: republican_share in 2024 (%)

Expected: None | Calculated: 57.09824967981948 | Display: 57.1
Numerator / after operand: 0.5709824967981948 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "YELLOWSTONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-YELLOWSTONE-R-2024.json](evidence/SENATE-YELLOWSTONE-R-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-YELLOWSTONE-JON-TESTER-2024: PASS

YELLOWSTONE: share__JON TESTER in 2024 (%)

Expected: None | Calculated: 40.852594986887844 | Display: 40.9
Numerator / after operand: 0.40852594986887847 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__JON TESTER", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2024}, {"column": "county", "op": "eq", "value": "YELLOWSTONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-YELLOWSTONE-JON-TESTER-2024.json](evidence/SENATE-YELLOWSTONE-JON-TESTER-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-YELLOWSTONE-R-2026: PASS

YELLOWSTONE: republican_share in 2026 (%)

Expected: None | Calculated: 51.30075792193877 | Display: 51.3
Numerator / after operand: 0.5130075792193877 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "republican_share", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "YELLOWSTONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-YELLOWSTONE-R-2026.json](evidence/SENATE-YELLOWSTONE-R-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-YELLOWSTONE-SETH-BODNAR-2026: PASS

YELLOWSTONE: share__SETH BODNAR in 2026 (%)

Expected: None | Calculated: 32.92312055843563 | Display: 32.9
Numerator / after operand: 0.32923120558435626 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__SETH BODNAR", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "YELLOWSTONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-YELLOWSTONE-SETH-BODNAR-2026.json](evidence/SENATE-YELLOWSTONE-SETH-BODNAR-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-YELLOWSTONE-ALANI-BANKHEAD-2026: PASS

YELLOWSTONE: share__ALANI BANKHEAD in 2026 (%)

Expected: None | Calculated: 13.316420591525771 | Display: 13.3
Numerator / after operand: 0.1331642059152577 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "share__ALANI BANKHEAD", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "year", "op": "eq", "value": 2026}, {"column": "county", "op": "eq", "value": "YELLOWSTONE"}], "operation": "sum", "scale": 100, "table": "county-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-YELLOWSTONE-ALANI-BANKHEAD-2026.json](evidence/SENATE-YELLOWSTONE-ALANI-BANKHEAD-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## MT02-JOHN-B-DRISCOLL-WINS-2024: PASS

2024 us-house-east: JOHN B DRISCOLL precinct wins/status count

Expected: None | Calculated: 51 | Display: 51
Numerator / after operand: 51 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "JOHN B DRISCOLL"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-JOHN-B-DRISCOLL-WINS-2024.json](evidence/MT02-JOHN-B-DRISCOLL-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-JOHN-B-DRISCOLL-MAJORITIES-2024: PASS

2024 JOHN B DRISCOLL: precincts with strictly more than 50%

Expected: None | Calculated: 51.0 | Display: 51
Numerator / after operand: 51.0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "JOHN B DRISCOLL"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-JOHN-B-DRISCOLL-MAJORITIES-2024.json](evidence/MT02-JOHN-B-DRISCOLL-MAJORITIES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TROY-DOWNING-WINS-2024: PASS

2024 us-house-east: TROY DOWNING precinct wins/status count

Expected: None | Calculated: 332 | Display: 332
Numerator / after operand: 332 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "TROY DOWNING"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-TROY-DOWNING-WINS-2024.json](evidence/MT02-TROY-DOWNING-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TROY-DOWNING-MAJORITIES-2024: PASS

2024 TROY DOWNING: precincts with strictly more than 50%

Expected: None | Calculated: 332.0 | Display: 332
Numerator / after operand: 332.0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "TROY DOWNING"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-TROY-DOWNING-MAJORITIES-2024.json](evidence/MT02-TROY-DOWNING-MAJORITIES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-Democrat-WINS-2024: PASS

2024 us-house-east: Democrat precinct wins/status count

Expected: None | Calculated: 51 | Display: 51
Numerator / after operand: 51 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Democrat"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-Democrat-WINS-2024.json](evidence/MT02-Democrat-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-Republican-WINS-2024: PASS

2024 us-house-east: Republican precinct wins/status count

Expected: None | Calculated: 332 | Display: 332
Numerator / after operand: 332 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-Republican-WINS-2024.json](evidence/MT02-Republican-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-non-Republican-WINS-2024: PASS

2024 us-house-east: non-Republican precinct wins/status count

Expected: None | Calculated: 51 | Display: 51
Numerator / after operand: 51 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "republican_category"}, {"column": "name", "op": "eq", "value": "non-Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-non-Republican-WINS-2024.json](evidence/MT02-non-Republican-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-tie-WINS-2024: PASS

2024 us-house-east: tie precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "tie"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-tie-WINS-2024.json](evidence/MT02-tie-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-no_votes-WINS-2024: PASS

2024 us-house-east: no_votes precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "no_votes"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-no_votes-WINS-2024.json](evidence/MT02-no_votes-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-missing_results-WINS-2024: PASS

2024 us-house-east: missing_results precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "missing_results"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-missing_results-WINS-2024.json](evidence/MT02-missing_results-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-invalid_data-WINS-2024: PASS

2024 us-house-east: invalid_data precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "invalid_data"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-invalid_data-WINS-2024.json](evidence/MT02-invalid_data-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-RYAN-K-ZINKE-WINS-2024: PASS

2024 us-house-west: RYAN K ZINKE precinct wins/status count

Expected: None | Calculated: 220 | Display: 220
Numerator / after operand: 220 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "RYAN K ZINKE"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-RYAN-K-ZINKE-WINS-2024.json](evidence/MT01-RYAN-K-ZINKE-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-RYAN-K-ZINKE-MAJORITIES-2024: PASS

2024 RYAN K ZINKE: precincts with strictly more than 50%

Expected: None | Calculated: 213.0 | Display: 213
Numerator / after operand: 213.0 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "RYAN K ZINKE"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-RYAN-K-ZINKE-MAJORITIES-2024.json](evidence/MT01-RYAN-K-ZINKE-MAJORITIES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-DENNIS-HAYES-WINS-2024: PASS

2024 us-house-west: DENNIS HAYES precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "DENNIS HAYES"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-DENNIS-HAYES-WINS-2024.json](evidence/MT01-DENNIS-HAYES-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-DENNIS-HAYES-MAJORITIES-2024: PASS

2024 DENNIS HAYES: precincts with strictly more than 50%

Expected: None | Calculated: 0.0 | Display: 0
Numerator / after operand: 0.0 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "DENNIS HAYES"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-DENNIS-HAYES-MAJORITIES-2024.json](evidence/MT01-DENNIS-HAYES-MAJORITIES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MONICA-TRANEL-WINS-2024: PASS

2024 us-house-west: MONICA TRANEL precinct wins/status count

Expected: None | Calculated: 124 | Display: 124
Numerator / after operand: 124 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "MONICA TRANEL"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-MONICA-TRANEL-WINS-2024.json](evidence/MT01-MONICA-TRANEL-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MONICA-TRANEL-MAJORITIES-2024: PASS

2024 MONICA TRANEL: precincts with strictly more than 50%

Expected: None | Calculated: 120.0 | Display: 120
Numerator / after operand: 120.0 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "MONICA TRANEL"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-MONICA-TRANEL-MAJORITIES-2024.json](evidence/MT01-MONICA-TRANEL-MAJORITIES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-Democrat-WINS-2024: PASS

2024 us-house-west: Democrat precinct wins/status count

Expected: None | Calculated: 124 | Display: 124
Numerator / after operand: 124 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Democrat"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-Democrat-WINS-2024.json](evidence/MT01-Democrat-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-Libertarian-WINS-2024: PASS

2024 us-house-west: Libertarian precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Libertarian"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-Libertarian-WINS-2024.json](evidence/MT01-Libertarian-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-Republican-WINS-2024: PASS

2024 us-house-west: Republican precinct wins/status count

Expected: None | Calculated: 220 | Display: 220
Numerator / after operand: 220 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-Republican-WINS-2024.json](evidence/MT01-Republican-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-non-Republican-WINS-2024: PASS

2024 us-house-west: non-Republican precinct wins/status count

Expected: None | Calculated: 124 | Display: 124
Numerator / after operand: 124 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "republican_category"}, {"column": "name", "op": "eq", "value": "non-Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-non-Republican-WINS-2024.json](evidence/MT01-non-Republican-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-tie-WINS-2024: PASS

2024 us-house-west: tie precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "tie"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-tie-WINS-2024.json](evidence/MT01-tie-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-no_votes-WINS-2024: PASS

2024 us-house-west: no_votes precinct wins/status count

Expected: None | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "no_votes"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-no_votes-WINS-2024.json](evidence/MT01-no_votes-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-missing_results-WINS-2024: PASS

2024 us-house-west: missing_results precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "missing_results"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-missing_results-WINS-2024.json](evidence/MT01-missing_results-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-invalid_data-WINS-2024: PASS

2024 us-house-west: invalid_data precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "invalid_data"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-invalid_data-WINS-2024.json](evidence/MT01-invalid_data-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## SENATE-TESTER-WINS-2024: PASS

2024 us-senate: JON TESTER precinct wins/status count

Expected: 228 | Calculated: 228 | Display: 228
Numerator / after operand: 228 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "JON TESTER"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-TESTER-WINS-2024.json](evidence/SENATE-TESTER-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TESTER-MAJORITIES-2024: PASS

2024 JON TESTER: precincts with strictly more than 50%

Expected: None | Calculated: 213.0 | Display: 213
Numerator / after operand: 213.0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "JON TESTER"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-TESTER-MAJORITIES-2024.json](evidence/SENATE-TESTER-MAJORITIES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHEEHY-WINS-2024: PASS

2024 us-senate: TIM SHEEHY precinct wins/status count

Expected: 497 | Calculated: 497 | Display: 497
Numerator / after operand: 497 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "TIM SHEEHY"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SHEEHY-WINS-2024.json](evidence/SENATE-SHEEHY-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHEEHY-MAJORITIES-2024: PASS

2024 TIM SHEEHY: precincts with strictly more than 50%

Expected: None | Calculated: 489.0 | Display: 489
Numerator / after operand: 489.0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "TIM SHEEHY"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SHEEHY-MAJORITIES-2024.json](evidence/SENATE-SHEEHY-MAJORITIES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SID-DAOUD-WINS-2024: PASS

2024 us-senate: SID DAOUD precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "SID DAOUD"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SID-DAOUD-WINS-2024.json](evidence/SENATE-SID-DAOUD-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SID-DAOUD-MAJORITIES-2024: PASS

2024 SID DAOUD: precincts with strictly more than 50%

Expected: None | Calculated: 0.0 | Display: 0
Numerator / after operand: 0.0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "SID DAOUD"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-SID-DAOUD-MAJORITIES-2024.json](evidence/SENATE-SID-DAOUD-MAJORITIES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROBERT-BARB-WINS-2024: PASS

2024 us-senate: ROBERT BARB precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "ROBERT BARB"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-ROBERT-BARB-WINS-2024.json](evidence/SENATE-ROBERT-BARB-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROBERT-BARB-MAJORITIES-2024: PASS

2024 ROBERT BARB: precincts with strictly more than 50%

Expected: None | Calculated: 0.0 | Display: 0
Numerator / after operand: 0.0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "ROBERT BARB"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-ROBERT-BARB-MAJORITIES-2024.json](evidence/SENATE-ROBERT-BARB-MAJORITIES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-Democrat-WINS-2024: PASS

2024 us-senate: Democrat precinct wins/status count

Expected: None | Calculated: 228 | Display: 228
Numerator / after operand: 228 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Democrat"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-Democrat-WINS-2024.json](evidence/SENATE-Democrat-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-Green-WINS-2024: PASS

2024 us-senate: Green precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Green"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-Green-WINS-2024.json](evidence/SENATE-Green-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-Libertarian-WINS-2024: PASS

2024 us-senate: Libertarian precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Libertarian"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-Libertarian-WINS-2024.json](evidence/SENATE-Libertarian-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-Republican-WINS-2024: PASS

2024 us-senate: Republican precinct wins/status count

Expected: None | Calculated: 497 | Display: 497
Numerator / after operand: 497 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-Republican-WINS-2024.json](evidence/SENATE-Republican-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-non-Republican-WINS-2024: PASS

2024 us-senate: non-Republican precinct wins/status count

Expected: None | Calculated: 228 | Display: 228
Numerator / after operand: 228 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "republican_category"}, {"column": "name", "op": "eq", "value": "non-Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-non-Republican-WINS-2024.json](evidence/SENATE-non-Republican-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-tie-WINS-2024: PASS

2024 us-senate: tie precinct wins/status count

Expected: None | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "tie"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-tie-WINS-2024.json](evidence/SENATE-tie-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-no_votes-WINS-2024: PASS

2024 us-senate: no_votes precinct wins/status count

Expected: None | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "no_votes"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-no_votes-WINS-2024.json](evidence/SENATE-no_votes-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-missing_results-WINS-2024: PASS

2024 us-senate: missing_results precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "missing_results"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-missing_results-WINS-2024.json](evidence/SENATE-missing_results-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-invalid_data-WINS-2024: PASS

2024 us-senate: invalid_data precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "invalid_data"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-invalid_data-WINS-2024.json](evidence/SENATE-invalid_data-WINS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## MT02-TROY-DOWNING-WINS-2026: PASS

2026 us-house-east: TROY DOWNING precinct wins/status count

Expected: None | Calculated: 321 | Display: 321
Numerator / after operand: 321 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "TROY DOWNING"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TROY-DOWNING-WINS-2026.json](evidence/MT02-TROY-DOWNING-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-TROY-DOWNING-MAJORITIES-2026: PASS

2026 TROY DOWNING: precincts with strictly more than 50%

Expected: None | Calculated: 298.0 | Display: 298
Numerator / after operand: 298.0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "TROY DOWNING"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-TROY-DOWNING-MAJORITIES-2026.json](evidence/MT02-TROY-DOWNING-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PATRICK-MCCRACKEN-WINS-2026: PASS

2026 us-house-east: PATRICK MCCRACKEN precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "PATRICK MCCRACKEN"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PATRICK-MCCRACKEN-WINS-2026.json](evidence/MT02-PATRICK-MCCRACKEN-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PATRICK-MCCRACKEN-MAJORITIES-2026: PASS

2026 PATRICK MCCRACKEN: precincts with strictly more than 50%

Expected: None | Calculated: 0.0 | Display: 0
Numerator / after operand: 0.0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "PATRICK MCCRACKEN"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PATRICK-MCCRACKEN-MAJORITIES-2026.json](evidence/MT02-PATRICK-MCCRACKEN-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-BRIAN-J-MILLER-WINS-2026: PASS

2026 us-house-east: BRIAN J MILLER precinct wins/status count

Expected: None | Calculated: 61 | Display: 61
Numerator / after operand: 61 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "BRIAN J MILLER"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-BRIAN-J-MILLER-WINS-2026.json](evidence/MT02-BRIAN-J-MILLER-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-BRIAN-J-MILLER-MAJORITIES-2026: PASS

2026 BRIAN J MILLER: precincts with strictly more than 50%

Expected: None | Calculated: 46.0 | Display: 46
Numerator / after operand: 46.0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "BRIAN J MILLER"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-BRIAN-J-MILLER-MAJORITIES-2026.json](evidence/MT02-BRIAN-J-MILLER-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-MICHAEL-D-EISENHAUER-WINS-2026: PASS

2026 us-house-east: MICHAEL D EISENHAUER precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "MICHAEL D EISENHAUER"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-MICHAEL-D-EISENHAUER-WINS-2026.json](evidence/MT02-MICHAEL-D-EISENHAUER-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-MICHAEL-D-EISENHAUER-MAJORITIES-2026: PASS

2026 MICHAEL D EISENHAUER: precincts with strictly more than 50%

Expected: None | Calculated: 0.0 | Display: 0
Numerator / after operand: 0.0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "MICHAEL D EISENHAUER"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-MICHAEL-D-EISENHAUER-MAJORITIES-2026.json](evidence/MT02-MICHAEL-D-EISENHAUER-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-Democrat-WINS-2026: PASS

2026 us-house-east: Democrat precinct wins/status count

Expected: None | Calculated: 61 | Display: 61
Numerator / after operand: 61 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Democrat"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-Democrat-WINS-2026.json](evidence/MT02-Democrat-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-Independent-WINS-2026: PASS

2026 us-house-east: Independent precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Independent"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-Independent-WINS-2026.json](evidence/MT02-Independent-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-Libertarian-WINS-2026: PASS

2026 us-house-east: Libertarian precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Libertarian"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-Libertarian-WINS-2026.json](evidence/MT02-Libertarian-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-Republican-WINS-2026: PASS

2026 us-house-east: Republican precinct wins/status count

Expected: None | Calculated: 321 | Display: 321
Numerator / after operand: 321 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-Republican-WINS-2026.json](evidence/MT02-Republican-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-non-Republican-WINS-2026: PASS

2026 us-house-east: non-Republican precinct wins/status count

Expected: None | Calculated: 61 | Display: 61
Numerator / after operand: 61 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "republican_category"}, {"column": "name", "op": "eq", "value": "non-Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-non-Republican-WINS-2026.json](evidence/MT02-non-Republican-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-tie-WINS-2026: PASS

2026 us-house-east: tie precinct wins/status count

Expected: None | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "tie"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-tie-WINS-2026.json](evidence/MT02-tie-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-no_votes-WINS-2026: PASS

2026 us-house-east: no_votes precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "no_votes"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-no_votes-WINS-2026.json](evidence/MT02-no_votes-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-missing_results-WINS-2026: PASS

2026 us-house-east: missing_results precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "missing_results"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-missing_results-WINS-2026.json](evidence/MT02-missing_results-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-invalid_data-WINS-2026: PASS

2026 us-house-east: invalid_data precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "invalid_data"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-invalid_data-WINS-2026.json](evidence/MT02-invalid_data-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-AARON-FLINT-WINS-2026: PASS

2026 us-house-west: AARON FLINT precinct wins/status count

Expected: None | Calculated: 198 | Display: 198
Numerator / after operand: 198 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "AARON FLINT"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-AARON-FLINT-WINS-2026.json](evidence/MT01-AARON-FLINT-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-AARON-FLINT-MAJORITIES-2026: PASS

2026 AARON FLINT: precincts with strictly more than 50%

Expected: None | Calculated: 186.0 | Display: 186
Numerator / after operand: 186.0 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "AARON FLINT"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-AARON-FLINT-MAJORITIES-2026.json](evidence/MT01-AARON-FLINT-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-SAM-FORSTAG-WINS-2026: PASS

2026 us-house-west: SAM FORSTAG precinct wins/status count

Expected: None | Calculated: 147 | Display: 147
Numerator / after operand: 147 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "SAM FORSTAG"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-SAM-FORSTAG-WINS-2026.json](evidence/MT01-SAM-FORSTAG-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-SAM-FORSTAG-MAJORITIES-2026: PASS

2026 SAM FORSTAG: precincts with strictly more than 50%

Expected: None | Calculated: 141.0 | Display: 141
Numerator / after operand: 141.0 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "SAM FORSTAG"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-SAM-FORSTAG-MAJORITIES-2026.json](evidence/MT01-SAM-FORSTAG-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-NICK-SHEEDY-WINS-2026: PASS

2026 us-house-west: NICK SHEEDY precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "NICK SHEEDY"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-NICK-SHEEDY-WINS-2026.json](evidence/MT01-NICK-SHEEDY-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-NICK-SHEEDY-MAJORITIES-2026: PASS

2026 NICK SHEEDY: precincts with strictly more than 50%

Expected: None | Calculated: 0.0 | Display: 0
Numerator / after operand: 0.0 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "NICK SHEEDY"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-NICK-SHEEDY-MAJORITIES-2026.json](evidence/MT01-NICK-SHEEDY-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-Democrat-WINS-2026: PASS

2026 us-house-west: Democrat precinct wins/status count

Expected: None | Calculated: 147 | Display: 147
Numerator / after operand: 147 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Democrat"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-Democrat-WINS-2026.json](evidence/MT01-Democrat-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-Libertarian-WINS-2026: PASS

2026 us-house-west: Libertarian precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Libertarian"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-Libertarian-WINS-2026.json](evidence/MT01-Libertarian-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-Republican-WINS-2026: PASS

2026 us-house-west: Republican precinct wins/status count

Expected: None | Calculated: 198 | Display: 198
Numerator / after operand: 198 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-Republican-WINS-2026.json](evidence/MT01-Republican-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-non-Republican-WINS-2026: PASS

2026 us-house-west: non-Republican precinct wins/status count

Expected: None | Calculated: 147 | Display: 147
Numerator / after operand: 147 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "republican_category"}, {"column": "name", "op": "eq", "value": "non-Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-non-Republican-WINS-2026.json](evidence/MT01-non-Republican-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-tie-WINS-2026: PASS

2026 us-house-west: tie precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "tie"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-tie-WINS-2026.json](evidence/MT01-tie-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-no_votes-WINS-2026: PASS

2026 us-house-west: no_votes precinct wins/status count

Expected: None | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "no_votes"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-no_votes-WINS-2026.json](evidence/MT01-no_votes-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-missing_results-WINS-2026: PASS

2026 us-house-west: missing_results precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "missing_results"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-missing_results-WINS-2026.json](evidence/MT01-missing_results-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-invalid_data-WINS-2026: PASS

2026 us-house-west: invalid_data precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "invalid_data"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-invalid_data-WINS-2026.json](evidence/MT01-invalid_data-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## SENATE-ALME-WINS-2026: PASS

2026 us-senate: KURT ALME precinct wins/status count

Expected: 532 | Calculated: 532 | Display: 532
Numerator / after operand: 532 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "KURT ALME"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ALME-WINS-2026.json](evidence/SENATE-ALME-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ALME-MAJORITIES-2026: PASS

2026 KURT ALME: precincts with strictly more than 50%

Expected: None | Calculated: 442.0 | Display: 442
Numerator / after operand: 442.0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "KURT ALME"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ALME-MAJORITIES-2026.json](evidence/SENATE-ALME-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-KYLE-AUSTIN-WINS-2026: PASS

2026 us-senate: KYLE AUSTIN precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "KYLE AUSTIN"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-KYLE-AUSTIN-WINS-2026.json](evidence/SENATE-KYLE-AUSTIN-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-KYLE-AUSTIN-MAJORITIES-2026: PASS

2026 KYLE AUSTIN: precincts with strictly more than 50%

Expected: None | Calculated: 0.0 | Display: 0
Numerator / after operand: 0.0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "KYLE AUSTIN"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-KYLE-AUSTIN-MAJORITIES-2026.json](evidence/SENATE-KYLE-AUSTIN-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-2026: PASS

2026 us-senate: ALANI BANKHEAD precinct wins/status count

Expected: 15 | Calculated: 15 | Display: 15
Numerator / after operand: 15 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "ALANI BANKHEAD"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-2026.json](evidence/SENATE-BANKHEAD-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-MAJORITIES-2026: PASS

2026 ALANI BANKHEAD: precincts with strictly more than 50%

Expected: None | Calculated: 2.0 | Display: 2
Numerator / after operand: 2.0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "ALANI BANKHEAD"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-MAJORITIES-2026.json](evidence/SENATE-BANKHEAD-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-WINS-2026: PASS

2026 us-senate: SETH BODNAR precinct wins/status count

Expected: 180 | Calculated: 180 | Display: 180
Numerator / after operand: 180 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "SETH BODNAR"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-WINS-2026.json](evidence/SENATE-BODNAR-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-MAJORITIES-2026: PASS

2026 SETH BODNAR: precincts with strictly more than 50%

Expected: None | Calculated: 103.0 | Display: 103
Numerator / after operand: 103.0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "majority_precincts", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "candidate"}, {"column": "name", "op": "eq", "value": "SETH BODNAR"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-MAJORITIES-2026.json](evidence/SENATE-BODNAR-MAJORITIES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-Democrat-WINS-2026: PASS

2026 us-senate: Democrat precinct wins/status count

Expected: None | Calculated: 15 | Display: 15
Numerator / after operand: 15 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Democrat"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-Democrat-WINS-2026.json](evidence/SENATE-Democrat-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-Independent-WINS-2026: PASS

2026 us-senate: Independent precinct wins/status count

Expected: None | Calculated: 180 | Display: 180
Numerator / after operand: 180 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Independent"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-Independent-WINS-2026.json](evidence/SENATE-Independent-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-Libertarian-WINS-2026: PASS

2026 us-senate: Libertarian precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Libertarian"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-Libertarian-WINS-2026.json](evidence/SENATE-Libertarian-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-Republican-WINS-2026: PASS

2026 us-senate: Republican precinct wins/status count

Expected: None | Calculated: 532 | Display: 532
Numerator / after operand: 532 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "party"}, {"column": "name", "op": "eq", "value": "Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-Republican-WINS-2026.json](evidence/SENATE-Republican-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-non-Republican-WINS-2026: PASS

2026 us-senate: non-Republican precinct wins/status count

Expected: None | Calculated: 195 | Display: 195
Numerator / after operand: 195 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "republican_category"}, {"column": "name", "op": "eq", "value": "non-Republican"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-non-Republican-WINS-2026.json](evidence/SENATE-non-Republican-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-tie-WINS-2026: PASS

2026 us-senate: tie precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "tie"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-tie-WINS-2026.json](evidence/SENATE-tie-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-no_votes-WINS-2026: PASS

2026 us-senate: no_votes precinct wins/status count

Expected: None | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "no_votes"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-no_votes-WINS-2026.json](evidence/SENATE-no_votes-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-missing_results-WINS-2026: PASS

2026 us-senate: missing_results precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "missing_results"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-missing_results-WINS-2026.json](evidence/SENATE-missing_results-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-invalid_data-WINS-2026: PASS

2026 us-senate: invalid_data precinct wins/status count

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"column": "wins", "denominator_column": "precinct_count", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "scope", "op": "eq", "value": "contest"}, {"column": "kind", "op": "eq", "value": "status"}, {"column": "name", "op": "eq", "value": "invalid_data"}], "operation": "sum", "table": "winner-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-invalid_data-WINS-2026.json](evidence/SENATE-invalid_data-WINS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-R-PLURALITY-BELOW-50-2024: PASS

Republican plurality wins with share strictly below 50%

Expected: None | Calculated: 8 | Display: 8
Numerator / after operand: 8 | Denominator / before operand: 727 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}], "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "republican_plurality_below_50", "op": "eq", "value": true}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/SENATE-R-PLURALITY-BELOW-50-2024.json](evidence/SENATE-R-PLURALITY-BELOW-50-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## MT01-R-PLURALITY-BELOW-50-2024: PASS

Republican plurality wins with share strictly below 50%

Expected: None | Calculated: 7 | Display: 7
Numerator / after operand: 7 | Denominator / before operand: 345 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}], "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "republican_plurality_below_50", "op": "eq", "value": true}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-R-PLURALITY-BELOW-50-2024.json](evidence/MT01-R-PLURALITY-BELOW-50-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-PLURALITY-BELOW-50-2024: PASS

Republican plurality wins with share strictly below 50%

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}], "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "republican_plurality_below_50", "op": "eq", "value": true}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-R-PLURALITY-BELOW-50-2024.json](evidence/MT02-R-PLURALITY-BELOW-50-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## SENATE-R-PLURALITY-BELOW-50-2026: PASS

Republican plurality wins with share strictly below 50%

Expected: None | Calculated: 89 | Display: 89
Numerator / after operand: 89 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}], "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-senate"}, {"column": "republican_plurality_below_50", "op": "eq", "value": true}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-R-PLURALITY-BELOW-50-2026.json](evidence/SENATE-R-PLURALITY-BELOW-50-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## MT01-R-PLURALITY-BELOW-50-2026: PASS

Republican plurality wins with share strictly below 50%

Expected: None | Calculated: 12 | Display: 12
Numerator / after operand: 12 | Denominator / before operand: 346 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}], "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "republican_plurality_below_50", "op": "eq", "value": true}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-R-PLURALITY-BELOW-50-2026.json](evidence/MT01-R-PLURALITY-BELOW-50-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-R-PLURALITY-BELOW-50-2026: PASS

Republican plurality wins with share strictly below 50%

Expected: None | Calculated: 23 | Display: 23
Numerator / after operand: 23 | Denominator / before operand: 383 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}], "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "republican_plurality_below_50", "op": "eq", "value": true}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-R-PLURALITY-BELOW-50-2026.json](evidence/MT02-R-PLURALITY-BELOW-50-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## SENATE-BODNAR-VS-BANKHEAD-BODNAR: PASS

2026 precincts: bodnar_vs_bankhead = bodnar

Expected: 704 | Calculated: 704 | Display: 704
Numerator / after operand: 704 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bodnar_vs_bankhead", "op": "eq", "value": "bodnar"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-VS-BANKHEAD-BODNAR.json](evidence/SENATE-BODNAR-VS-BANKHEAD-BODNAR.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-VS-BANKHEAD-BANKHEAD: PASS

2026 precincts: bodnar_vs_bankhead = bankhead

Expected: None | Calculated: 18 | Display: 18
Numerator / after operand: 18 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bodnar_vs_bankhead", "op": "eq", "value": "bankhead"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-VS-BANKHEAD-BANKHEAD.json](evidence/SENATE-BODNAR-VS-BANKHEAD-BANKHEAD.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-VS-BANKHEAD-TIE: PASS

2026 precincts: bodnar_vs_bankhead = tie

Expected: None | Calculated: 5 | Display: 5
Numerator / after operand: 5 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bodnar_vs_bankhead", "op": "eq", "value": "tie"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-VS-BANKHEAD-TIE.json](evidence/SENATE-BODNAR-VS-BANKHEAD-TIE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-VS-ALME-BANKHEAD: PASS

2026 precincts: bankhead_vs_alme = bankhead

Expected: 62 | Calculated: 62 | Display: 62
Numerator / after operand: 62 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bankhead_vs_alme", "op": "eq", "value": "bankhead"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-VS-ALME-BANKHEAD.json](evidence/SENATE-BANKHEAD-VS-ALME-BANKHEAD.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-VS-ALME-ALME: PASS

2026 precincts: bankhead_vs_alme = alme

Expected: None | Calculated: 663 | Display: 663
Numerator / after operand: 663 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bankhead_vs_alme", "op": "eq", "value": "alme"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-VS-ALME-ALME.json](evidence/SENATE-BANKHEAD-VS-ALME-ALME.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-VS-ALME-TIE: PASS

2026 precincts: bankhead_vs_alme = tie

Expected: None | Calculated: 2 | Display: 2
Numerator / after operand: 2 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bankhead_vs_alme", "op": "eq", "value": "tie"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-VS-ALME-TIE.json](evidence/SENATE-BANKHEAD-VS-ALME-TIE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-VS-ALME-BODNAR: PASS

2026 precincts: bodnar_vs_alme = bodnar

Expected: None | Calculated: 194 | Display: 194
Numerator / after operand: 194 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bodnar_vs_alme", "op": "eq", "value": "bodnar"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-VS-ALME-BODNAR.json](evidence/SENATE-BODNAR-VS-ALME-BODNAR.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-VS-ALME-ALME: PASS

2026 precincts: bodnar_vs_alme = alme

Expected: None | Calculated: 533 | Display: 533
Numerator / after operand: 533 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bodnar_vs_alme", "op": "eq", "value": "alme"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-VS-ALME-ALME.json](evidence/SENATE-BODNAR-VS-ALME-ALME.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-VS-ALME-TIE: PASS

2026 precincts: bodnar_vs_alme = tie

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bodnar_vs_alme", "op": "eq", "value": "tie"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-VS-ALME-TIE.json](evidence/SENATE-BODNAR-VS-ALME-TIE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-WINS-BANKHEAD-TRAILS-ALME: PASS

2026 Bodnar-winning precincts: BANKHEAD-TRAILS-ALME

Expected: 131 | Calculated: 131 | Display: 131
Numerator / after operand: 131 | Denominator / before operand: 180 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "winning_candidate", "op": "eq", "value": "SETH BODNAR"}], "filters": [{"column": "winning_candidate", "op": "eq", "value": "SETH BODNAR"}, {"column": "alme_votes", "op": "gt", "right_column": "bankhead_votes"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-WINS-BANKHEAD-TRAILS-ALME.json](evidence/SENATE-BODNAR-WINS-BANKHEAD-TRAILS-ALME.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-WINS-BANKHEAD-BEATS-ALME: PASS

2026 Bodnar-winning precincts: BANKHEAD-BEATS-ALME

Expected: None | Calculated: 47 | Display: 47
Numerator / after operand: 47 | Denominator / before operand: 180 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "winning_candidate", "op": "eq", "value": "SETH BODNAR"}], "filters": [{"column": "winning_candidate", "op": "eq", "value": "SETH BODNAR"}, {"column": "bankhead_votes", "op": "gt", "right_column": "alme_votes"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-WINS-BANKHEAD-BEATS-ALME.json](evidence/SENATE-BODNAR-WINS-BANKHEAD-BEATS-ALME.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COMBINED-EXCEEDS-ALME: PASS

Precincts where Bodnar plus Bankhead votes exceed Alme

Expected: None | Calculated: 267 | Display: 267
Numerator / after operand: 267 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "combined_exceeds_alme", "op": "eq", "value": true}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COMBINED-EXCEEDS-ALME.json](evidence/SENATE-COMBINED-EXCEEDS-ALME.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-BIG-HORN: PASS

Bankhead plurality wins in BIG HORN

Expected: 7 | Calculated: 7 | Display: 7
Numerator / after operand: 7 | Denominator / before operand: 23 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "BIG HORN"}], "filters": [{"column": "county", "value": "BIG HORN"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-BIG-HORN.json](evidence/SENATE-BANKHEAD-WINS-BIG-HORN.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-BLAINE: PASS

Bankhead plurality wins in BLAINE

Expected: 3 | Calculated: 3 | Display: 3
Numerator / after operand: 3 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "BLAINE"}], "filters": [{"column": "county", "value": "BLAINE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-BLAINE.json](evidence/SENATE-BANKHEAD-WINS-BLAINE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-CASCADE: PASS

Bankhead plurality wins in CASCADE

Expected: 1 | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 26 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "CASCADE"}], "filters": [{"column": "county", "value": "CASCADE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-CASCADE.json](evidence/SENATE-BANKHEAD-WINS-CASCADE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-HILL: PASS

Bankhead plurality wins in HILL

Expected: 1 | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 17 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "HILL"}], "filters": [{"column": "county", "value": "HILL"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-HILL.json](evidence/SENATE-BANKHEAD-WINS-HILL.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-ROOSEVELT: PASS

Bankhead plurality wins in ROOSEVELT

Expected: 3 | Calculated: 3 | Display: 3
Numerator / after operand: 3 | Denominator / before operand: 12 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "ROOSEVELT"}], "filters": [{"column": "county", "value": "ROOSEVELT"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-ROOSEVELT.json](evidence/SENATE-BANKHEAD-WINS-ROOSEVELT.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-SHARE-NONREPUBLICAN-WINS: PASS

Share of non-Republican-winning precincts won by Bodnar (%)

Expected: 92.3 | Calculated: 92.3076923076923 | Display: 92.3
Numerator / after operand: 180 | Denominator / before operand: 195 (eligible rows or contest votes)

Calculation: `{"denominator_column": "non_republican_won", "filters": [], "numerator_column": "bodnar_won", "operation": "ratio", "scale": 100, "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-SHARE-NONREPUBLICAN-WINS.json](evidence/SENATE-BODNAR-SHARE-NONREPUBLICAN-WINS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TESTER-TO-BODNAR: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts subsequently won by SETH BODNAR

Expected: 170 | Calculated: 170 | Display: 170
Numerator / after operand: 170 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "winning_candidate_2026", "op": "eq", "value": "SETH BODNAR"}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-TO-BODNAR.json](evidence/SENATE-TESTER-TO-BODNAR.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-TO-ALME: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts subsequently won by KURT ALME

Expected: 35 | Calculated: 35 | Display: 35
Numerator / after operand: 35 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "winning_candidate_2026", "op": "eq", "value": "KURT ALME"}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-TO-ALME.json](evidence/SENATE-TESTER-TO-ALME.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-TO-BANKHEAD: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts subsequently won by ALANI BANKHEAD

Expected: 14 | Calculated: 14 | Display: 14
Numerator / after operand: 14 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "winning_candidate_2026", "op": "eq", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-TO-BANKHEAD.json](evidence/SENATE-TESTER-TO-BANKHEAD.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-BANKHEAD-TRAILS-ALME: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts: bankhead_trails_alme

Expected: 161 | Calculated: 161 | Display: 161
Numerator / after operand: 161 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "bankhead_trails_alme", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-TRAILS-ALME.json](evidence/SENATE-TESTER-BANKHEAD-TRAILS-ALME.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-BANKHEAD-TRAILS-BODNAR: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts: bankhead_trails_bodnar

Expected: None | Calculated: 204 | Display: 204
Numerator / after operand: 204 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "bankhead_trails_bodnar", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-TRAILS-BODNAR.json](evidence/SENATE-TESTER-BANKHEAD-TRAILS-BODNAR.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-BODNAR-BEATS-ALME: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts: bodnar_beats_alme

Expected: None | Calculated: 183 | Display: 183
Numerator / after operand: 183 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "bodnar_beats_alme", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BODNAR-BEATS-ALME.json](evidence/SENATE-TESTER-BODNAR-BEATS-ALME.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-BANKHEAD-BELOW-20PCT: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts: bankhead_below_20pct

Expected: None | Calculated: 147 | Display: 147
Numerator / after operand: 147 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "bankhead_below_20pct", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-BELOW-20PCT.json](evidence/SENATE-TESTER-BANKHEAD-BELOW-20PCT.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-BANKHEAD-BELOW-30PCT: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts: bankhead_below_30pct

Expected: None | Calculated: 186 | Display: 186
Numerator / after operand: 186 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "bankhead_below_30pct", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-BELOW-30PCT.json](evidence/SENATE-TESTER-BANKHEAD-BELOW-30PCT.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-BANKHEAD-BELOW-40PCT: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts: bankhead_below_40pct

Expected: None | Calculated: 205 | Display: 205
Numerator / after operand: 205 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "bankhead_below_40pct", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-BELOW-40PCT.json](evidence/SENATE-TESTER-BANKHEAD-BELOW-40PCT.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-COMBINED-EXCEEDS-TESTER-SHARE: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts: combined_exceeds_tester_share

Expected: None | Calculated: 174 | Display: 174
Numerator / after operand: 174 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "combined_exceeds_tester_share", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-COMBINED-EXCEEDS-TESTER-SHARE.json](evidence/SENATE-TESTER-COMBINED-EXCEEDS-TESTER-SHARE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-REPUBLICAN-SHARE-INCREASED: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts: republican_share_increased

Expected: None | Calculated: 41 | Display: 41
Numerator / after operand: 41 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "republican_share_increased", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-REPUBLICAN-SHARE-INCREASED.json](evidence/SENATE-TESTER-REPUBLICAN-SHARE-INCREASED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-REPUBLICAN-SHARE-DECREASED: NEEDS_GEOGRAPHIC_REVIEW

provisional Tester-won precincts: republican_share_decreased

Expected: None | Calculated: 178 | Display: 178
Numerator / after operand: 178 | Denominator / before operand: 219 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}, {"column": "republican_share_decreased", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-REPUBLICAN-SHARE-DECREASED.json](evidence/SENATE-TESTER-REPUBLICAN-SHARE-DECREASED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-TESTER-MATCHED: NEEDS_GEOGRAPHIC_REVIEW

Tester-won precincts in provisional sample

Expected: 219 | Calculated: 219 | Display: 219
Numerator / after operand: 219 | Denominator / before operand: 228 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "provisional_comparable", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-MATCHED.json](evidence/SENATE-TESTER-MATCHED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Name-matched sample is provisional; matching names do not prove geographic continuity.

## SENATE-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS: PASS

us-senate: provisional coverage matched_precincts

Expected: 689 | Calculated: 689 | Display: 689
Numerator / after operand: 689 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_precincts", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS.json](evidence/SENATE-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-PROVISIONAL-PRECINCTS-2024: PASS

us-senate: provisional coverage precincts_2024

Expected: None | Calculated: 727 | Display: 727
Numerator / after operand: 727 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-PROVISIONAL-PRECINCTS-2024.json](evidence/SENATE-COVERAGE-PROVISIONAL-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-PROVISIONAL-PRECINCTS-2026: PASS

us-senate: provisional coverage precincts_2026

Expected: None | Calculated: 728 | Display: 728
Numerator / after operand: 728 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-PROVISIONAL-PRECINCTS-2026.json](evidence/SENATE-COVERAGE-PROVISIONAL-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024: PASS

us-senate: provisional coverage excluded_precincts_2024

Expected: None | Calculated: 38 | Display: 38
Numerator / after operand: 38 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024.json](evidence/SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026: PASS

us-senate: provisional coverage excluded_precincts_2026

Expected: None | Calculated: 39 | Display: 39
Numerator / after operand: 39 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026.json](evidence/SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2024: PASS

us-senate: provisional coverage matched_vote_share_2024

Expected: None | Calculated: 96.98202752683356 | Display: 96.98
Numerator / after operand: 0.9698202752683356 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2024.json](evidence/SENATE-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2026: PASS

us-senate: provisional coverage matched_vote_share_2026

Expected: None | Calculated: 97.03169422137924 | Display: 97.03
Numerator / after operand: 0.9703169422137924 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2026.json](evidence/SENATE-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024: PASS

us-senate: provisional coverage excluded_vote_share_2024

Expected: None | Calculated: 3.0179724731664423 | Display: 3.02
Numerator / after operand: 0.03017972473166442 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024.json](evidence/SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026: PASS

us-senate: provisional coverage excluded_vote_share_2026

Expected: None | Calculated: 2.968305778620759 | Display: 2.97
Numerator / after operand: 0.029683057786207587 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026.json](evidence/SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## MT01-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS: PASS

us-house-west: provisional coverage matched_precincts

Expected: None | Calculated: 309 | Display: 309
Numerator / after operand: 309 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_precincts", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS.json](evidence/MT01-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-PROVISIONAL-PRECINCTS-2024: PASS

us-house-west: provisional coverage precincts_2024

Expected: None | Calculated: 345 | Display: 345
Numerator / after operand: 345 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-PROVISIONAL-PRECINCTS-2024.json](evidence/MT01-COVERAGE-PROVISIONAL-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-PROVISIONAL-PRECINCTS-2026: PASS

us-house-west: provisional coverage precincts_2026

Expected: None | Calculated: 346 | Display: 346
Numerator / after operand: 346 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-PROVISIONAL-PRECINCTS-2026.json](evidence/MT01-COVERAGE-PROVISIONAL-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024: PASS

us-house-west: provisional coverage excluded_precincts_2024

Expected: None | Calculated: 36 | Display: 36
Numerator / after operand: 36 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024.json](evidence/MT01-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026: PASS

us-house-west: provisional coverage excluded_precincts_2026

Expected: None | Calculated: 37 | Display: 37
Numerator / after operand: 37 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026.json](evidence/MT01-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2024: PASS

us-house-west: provisional coverage matched_vote_share_2024

Expected: None | Calculated: 94.65503652262417 | Display: 94.66
Numerator / after operand: 0.9465503652262417 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2024.json](evidence/MT01-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2026: PASS

us-house-west: provisional coverage matched_vote_share_2026

Expected: None | Calculated: 94.83427777383483 | Display: 94.83
Numerator / after operand: 0.9483427777383483 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2026.json](evidence/MT01-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024: PASS

us-house-west: provisional coverage excluded_vote_share_2024

Expected: None | Calculated: 5.344963477375832 | Display: 5.34
Numerator / after operand: 0.053449634773758324 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024.json](evidence/MT01-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026: PASS

us-house-west: provisional coverage excluded_vote_share_2026

Expected: None | Calculated: 5.165722226165173 | Display: 5.17
Numerator / after operand: 0.05165722226165173 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026.json](evidence/MT01-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS: PASS

us-house-east: provisional coverage matched_precincts

Expected: None | Calculated: 381 | Display: 381
Numerator / after operand: 381 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_precincts", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS.json](evidence/MT02-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-PROVISIONAL-PRECINCTS-2024: PASS

us-house-east: provisional coverage precincts_2024

Expected: None | Calculated: 383 | Display: 383
Numerator / after operand: 383 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-PROVISIONAL-PRECINCTS-2024.json](evidence/MT02-COVERAGE-PROVISIONAL-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-PROVISIONAL-PRECINCTS-2026: PASS

us-house-east: provisional coverage precincts_2026

Expected: None | Calculated: 383 | Display: 383
Numerator / after operand: 383 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-PROVISIONAL-PRECINCTS-2026.json](evidence/MT02-COVERAGE-PROVISIONAL-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024: PASS

us-house-east: provisional coverage excluded_precincts_2024

Expected: None | Calculated: 2 | Display: 2
Numerator / after operand: 2 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024.json](evidence/MT02-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026: PASS

us-house-east: provisional coverage excluded_precincts_2026

Expected: None | Calculated: 2 | Display: 2
Numerator / after operand: 2 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026.json](evidence/MT02-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2024: PASS

us-house-east: provisional coverage matched_vote_share_2024

Expected: None | Calculated: 99.65196247436899 | Display: 99.65
Numerator / after operand: 0.9965196247436898 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2024.json](evidence/MT02-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2026: PASS

us-house-east: provisional coverage matched_vote_share_2026

Expected: None | Calculated: 99.6722515367459 | Display: 99.67
Numerator / after operand: 0.996722515367459 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2026.json](evidence/MT02-COVERAGE-PROVISIONAL-MATCHED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024: PASS

us-house-east: provisional coverage excluded_vote_share_2024

Expected: None | Calculated: 0.3480375256310222 | Display: 0.35
Numerator / after operand: 0.0034803752563102217 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024.json](evidence/MT02-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026: PASS

us-house-east: provisional coverage excluded_vote_share_2026

Expected: None | Calculated: 0.32774846325409346 | Display: 0.33
Numerator / after operand: 0.0032774846325409348 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "provisional"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026.json](evidence/MT02-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## SENATE-TESTER-TO-BODNAR-VERIFIED: PASS

verified Tester-won precincts subsequently won by SETH BODNAR

Expected: None | Calculated: 2 | Display: 2
Numerator / after operand: 2 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "winning_candidate_2026", "op": "eq", "value": "SETH BODNAR"}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-TO-BODNAR-VERIFIED.json](evidence/SENATE-TESTER-TO-BODNAR-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-TO-ALME-VERIFIED: PASS

verified Tester-won precincts subsequently won by KURT ALME

Expected: None | Calculated: 6 | Display: 6
Numerator / after operand: 6 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "winning_candidate_2026", "op": "eq", "value": "KURT ALME"}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-TO-ALME-VERIFIED.json](evidence/SENATE-TESTER-TO-ALME-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-TO-BANKHEAD-VERIFIED: PASS

verified Tester-won precincts subsequently won by ALANI BANKHEAD

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "winning_candidate_2026", "op": "eq", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-TO-BANKHEAD-VERIFIED.json](evidence/SENATE-TESTER-TO-BANKHEAD-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-BANKHEAD-TRAILS-ALME-VERIFIED: PASS

verified Tester-won precincts: bankhead_trails_alme

Expected: None | Calculated: 8 | Display: 8
Numerator / after operand: 8 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "bankhead_trails_alme", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-TRAILS-ALME-VERIFIED.json](evidence/SENATE-TESTER-BANKHEAD-TRAILS-ALME-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-BANKHEAD-TRAILS-BODNAR-VERIFIED: PASS

verified Tester-won precincts: bankhead_trails_bodnar

Expected: None | Calculated: 8 | Display: 8
Numerator / after operand: 8 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "bankhead_trails_bodnar", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-TRAILS-BODNAR-VERIFIED.json](evidence/SENATE-TESTER-BANKHEAD-TRAILS-BODNAR-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-BODNAR-BEATS-ALME-VERIFIED: PASS

verified Tester-won precincts: bodnar_beats_alme

Expected: None | Calculated: 2 | Display: 2
Numerator / after operand: 2 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "bodnar_beats_alme", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BODNAR-BEATS-ALME-VERIFIED.json](evidence/SENATE-TESTER-BODNAR-BEATS-ALME-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-BANKHEAD-BELOW-20PCT-VERIFIED: PASS

verified Tester-won precincts: bankhead_below_20pct

Expected: None | Calculated: 8 | Display: 8
Numerator / after operand: 8 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "bankhead_below_20pct", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-BELOW-20PCT-VERIFIED.json](evidence/SENATE-TESTER-BANKHEAD-BELOW-20PCT-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-BANKHEAD-BELOW-30PCT-VERIFIED: PASS

verified Tester-won precincts: bankhead_below_30pct

Expected: None | Calculated: 8 | Display: 8
Numerator / after operand: 8 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "bankhead_below_30pct", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-BELOW-30PCT-VERIFIED.json](evidence/SENATE-TESTER-BANKHEAD-BELOW-30PCT-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-BANKHEAD-BELOW-40PCT-VERIFIED: PASS

verified Tester-won precincts: bankhead_below_40pct

Expected: None | Calculated: 8 | Display: 8
Numerator / after operand: 8 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "bankhead_below_40pct", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-BANKHEAD-BELOW-40PCT-VERIFIED.json](evidence/SENATE-TESTER-BANKHEAD-BELOW-40PCT-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-COMBINED-EXCEEDS-TESTER-SHARE-VERIFIED: PASS

verified Tester-won precincts: combined_exceeds_tester_share

Expected: None | Calculated: 6 | Display: 6
Numerator / after operand: 6 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "combined_exceeds_tester_share", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-COMBINED-EXCEEDS-TESTER-SHARE-VERIFIED.json](evidence/SENATE-TESTER-COMBINED-EXCEEDS-TESTER-SHARE-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-REPUBLICAN-SHARE-INCREASED-VERIFIED: PASS

verified Tester-won precincts: republican_share_increased

Expected: None | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "republican_share_increased", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-REPUBLICAN-SHARE-INCREASED-VERIFIED.json](evidence/SENATE-TESTER-REPUBLICAN-SHARE-INCREASED-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-REPUBLICAN-SHARE-DECREASED-VERIFIED: PASS

verified Tester-won precincts: republican_share_decreased

Expected: None | Calculated: 7 | Display: 7
Numerator / after operand: 7 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}, {"column": "republican_share_decreased", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-REPUBLICAN-SHARE-DECREASED-VERIFIED.json](evidence/SENATE-TESTER-REPUBLICAN-SHARE-DECREASED-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-TESTER-MATCHED-VERIFIED: PASS

Tester-won precincts in verified sample

Expected: None | Calculated: 8 | Display: 8
Numerator / after operand: 8 | Denominator / before operand: 228 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "geographically_verified", "op": "eq", "value": true}], "operation": "count", "table": "senate-tester-precincts"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/SENATE-TESTER-MATCHED-VERIFIED.json](evidence/SENATE-TESTER-MATCHED-VERIFIED.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## SENATE-COVERAGE-VERIFIED-MATCHED-PRECINCTS: PASS

us-senate: verified coverage matched_precincts

Expected: None | Calculated: 23 | Display: 23
Numerator / after operand: 23 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_precincts", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-VERIFIED-MATCHED-PRECINCTS.json](evidence/SENATE-COVERAGE-VERIFIED-MATCHED-PRECINCTS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-VERIFIED-PRECINCTS-2024: PASS

us-senate: verified coverage precincts_2024

Expected: None | Calculated: 727 | Display: 727
Numerator / after operand: 727 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-VERIFIED-PRECINCTS-2024.json](evidence/SENATE-COVERAGE-VERIFIED-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-VERIFIED-PRECINCTS-2026: PASS

us-senate: verified coverage precincts_2026

Expected: None | Calculated: 728 | Display: 728
Numerator / after operand: 728 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-VERIFIED-PRECINCTS-2026.json](evidence/SENATE-COVERAGE-VERIFIED-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2024: PASS

us-senate: verified coverage excluded_precincts_2024

Expected: None | Calculated: 704 | Display: 704
Numerator / after operand: 704 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2024.json](evidence/SENATE-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2026: PASS

us-senate: verified coverage excluded_precincts_2026

Expected: None | Calculated: 705 | Display: 705
Numerator / after operand: 705 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2026.json](evidence/SENATE-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2024: PASS

us-senate: verified coverage matched_vote_share_2024

Expected: None | Calculated: 2.899242830936235 | Display: 2.90
Numerator / after operand: 0.028992428309362352 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2024.json](evidence/SENATE-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2026: PASS

us-senate: verified coverage matched_vote_share_2026

Expected: None | Calculated: 2.9605390899484743 | Display: 2.96
Numerator / after operand: 0.029605390899484742 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2026.json](evidence/SENATE-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2024: PASS

us-senate: verified coverage excluded_vote_share_2024

Expected: None | Calculated: 97.10075716906377 | Display: 97.10
Numerator / after operand: 0.9710075716906377 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2024.json](evidence/SENATE-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2026: PASS

us-senate: verified coverage excluded_vote_share_2026

Expected: None | Calculated: 97.03946091005152 | Display: 97.04
Numerator / after operand: 0.9703946091005152 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-senate"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2026.json](evidence/SENATE-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## MT01-COVERAGE-VERIFIED-MATCHED-PRECINCTS: PASS

us-house-west: verified coverage matched_precincts

Expected: None | Calculated: 23 | Display: 23
Numerator / after operand: 23 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_precincts", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-VERIFIED-MATCHED-PRECINCTS.json](evidence/MT01-COVERAGE-VERIFIED-MATCHED-PRECINCTS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-VERIFIED-PRECINCTS-2024: PASS

us-house-west: verified coverage precincts_2024

Expected: None | Calculated: 345 | Display: 345
Numerator / after operand: 345 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-VERIFIED-PRECINCTS-2024.json](evidence/MT01-COVERAGE-VERIFIED-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-VERIFIED-PRECINCTS-2026: PASS

us-house-west: verified coverage precincts_2026

Expected: None | Calculated: 346 | Display: 346
Numerator / after operand: 346 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-VERIFIED-PRECINCTS-2026.json](evidence/MT01-COVERAGE-VERIFIED-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2024: PASS

us-house-west: verified coverage excluded_precincts_2024

Expected: None | Calculated: 322 | Display: 322
Numerator / after operand: 322 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2024.json](evidence/MT01-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2026: PASS

us-house-west: verified coverage excluded_precincts_2026

Expected: None | Calculated: 323 | Display: 323
Numerator / after operand: 323 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2026.json](evidence/MT01-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2024: PASS

us-house-west: verified coverage matched_vote_share_2024

Expected: None | Calculated: 5.447053055550384 | Display: 5.45
Numerator / after operand: 0.05447053055550384 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2024.json](evidence/MT01-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2026: PASS

us-house-west: verified coverage matched_vote_share_2026

Expected: None | Calculated: 5.413754589906128 | Display: 5.41
Numerator / after operand: 0.054137545899061286 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2026.json](evidence/MT01-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2024: PASS

us-house-west: verified coverage excluded_vote_share_2024

Expected: None | Calculated: 94.55294694444962 | Display: 94.55
Numerator / after operand: 0.9455294694444961 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2024.json](evidence/MT01-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2026: PASS

us-house-west: verified coverage excluded_vote_share_2026

Expected: None | Calculated: 94.58624541009387 | Display: 94.59
Numerator / after operand: 0.9458624541009387 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2026.json](evidence/MT01-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-VERIFIED-MATCHED-PRECINCTS: PASS

us-house-east: verified coverage matched_precincts

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_precincts", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-VERIFIED-MATCHED-PRECINCTS.json](evidence/MT02-COVERAGE-VERIFIED-MATCHED-PRECINCTS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-VERIFIED-PRECINCTS-2024: PASS

us-house-east: verified coverage precincts_2024

Expected: None | Calculated: 383 | Display: 383
Numerator / after operand: 383 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-VERIFIED-PRECINCTS-2024.json](evidence/MT02-COVERAGE-VERIFIED-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-VERIFIED-PRECINCTS-2026: PASS

us-house-east: verified coverage precincts_2026

Expected: None | Calculated: 383 | Display: 383
Numerator / after operand: 383 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-VERIFIED-PRECINCTS-2026.json](evidence/MT02-COVERAGE-VERIFIED-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2024: PASS

us-house-east: verified coverage excluded_precincts_2024

Expected: None | Calculated: 383 | Display: 383
Numerator / after operand: 383 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2024.json](evidence/MT02-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2026: PASS

us-house-east: verified coverage excluded_precincts_2026

Expected: None | Calculated: 383 | Display: 383
Numerator / after operand: 383 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_precincts_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 1, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2026.json](evidence/MT02-COVERAGE-VERIFIED-EXCLUDED-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2024: PASS

us-house-east: verified coverage matched_vote_share_2024

Expected: None | Calculated: 0.0 | Display: 0.00
Numerator / after operand: 0.0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2024.json](evidence/MT02-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2026: PASS

us-house-east: verified coverage matched_vote_share_2026

Expected: None | Calculated: 0.0 | Display: 0.00
Numerator / after operand: 0.0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "matched_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2026.json](evidence/MT02-COVERAGE-VERIFIED-MATCHED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2024: PASS

us-house-east: verified coverage excluded_vote_share_2024

Expected: None | Calculated: 100.0 | Display: 100.00
Numerator / after operand: 1.0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2024", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2024.json](evidence/MT02-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2026: PASS

us-house-east: verified coverage excluded_vote_share_2026

Expected: None | Calculated: 100.0 | Display: 100.00
Numerator / after operand: 1.0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "excluded_vote_share_2026", "filters": [{"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "sample", "op": "eq", "value": "verified"}], "operation": "sum", "scale": 100, "table": "match-coverage"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2026.json](evidence/MT02-COVERAGE-VERIFIED-EXCLUDED-VOTE-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-PONDERA-PRECINCTS-2024: PASS

Pondera precinct portions in MT01, 2024

Expected: None | Calculated: 4 | Display: 4
Numerator / after operand: 4 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-PONDERA-PRECINCTS-2024.json](evidence/MT01-PONDERA-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-PONDERA-VOTES-2024: PASS

Pondera MT01 total House votes, 2024

Expected: None | Calculated: 858 | Display: 858
Numerator / after operand: 858 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "precinct-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT01-PONDERA-VOTES-2024.json](evidence/MT01-PONDERA-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PONDERA-PRECINCTS-2024: PASS

Pondera precinct portions in MT02, 2024

Expected: None | Calculated: 5 | Display: 5
Numerator / after operand: 5 | Denominator / before operand: 5 (eligible rows or contest votes)

Calculation: `{"filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-PONDERA-PRECINCTS-2024.json](evidence/MT02-PONDERA-PRECINCTS-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PONDERA-VOTES-2024: PASS

Pondera MT02 total House votes, 2024

Expected: None | Calculated: 1947 | Display: 1947
Numerator / after operand: 1947 | Denominator / before operand: 5 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "year", "op": "eq", "value": 2024}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "precinct-results"}`

Sources: cleaned/2024/general/precinct-results.csv
Evidence: [evidence/MT02-PONDERA-VOTES-2024.json](evidence/MT02-PONDERA-VOTES-2024.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-PONDERA-PRECINCTS-2026: PASS

Pondera precinct portions in MT01, 2026

Expected: 4 | Calculated: 4 | Display: 4
Numerator / after operand: 4 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-PONDERA-PRECINCTS-2026.json](evidence/MT01-PONDERA-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-PONDERA-VOTES-2026: PASS

Pondera MT01 total House votes, 2026

Expected: 673 | Calculated: 673 | Display: 673
Numerator / after operand: 673 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "precinct-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-PONDERA-VOTES-2026.json](evidence/MT01-PONDERA-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PONDERA-PRECINCTS-2026: PASS

Pondera precinct portions in MT02, 2026

Expected: None | Calculated: 5 | Display: 5
Numerator / after operand: 5 | Denominator / before operand: 5 (eligible rows or contest votes)

Calculation: `{"filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "count", "table": "precinct-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PONDERA-PRECINCTS-2026.json](evidence/MT02-PONDERA-PRECINCTS-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT02-PONDERA-VOTES-2026: PASS

Pondera MT02 total House votes, 2026

Expected: None | Calculated: 1545 | Display: 1545
Numerator / after operand: 1545 | Denominator / before operand: 5 (eligible rows or contest votes)

Calculation: `{"column": "total_votes", "filters": [{"column": "year", "op": "eq", "value": 2026}, {"column": "race", "op": "eq", "value": "us-house-east"}, {"column": "county", "op": "eq", "value": "PONDERA"}], "operation": "sum", "table": "precinct-results"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT02-PONDERA-VOTES-2026.json](evidence/MT02-PONDERA-VOTES-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-GALLATIN-REDUCTION-RANK: PASS

GALLATIN: rank of Republican share change (most negative first)

Expected: 1 | Calculated: 1.0 | Display: 1
Numerator / after operand: 1.0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "all_candidate_rank", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "GALLATIN"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-GALLATIN-REDUCTION-RANK.json](evidence/MT01-GALLATIN-REDUCTION-RANK.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## MT01-MISSOULA-REDUCTION-RANK: PASS

MISSOULA: rank of Republican share change (most negative first)

Expected: 2 | Calculated: 2.0 | Display: 2
Numerator / after operand: 2.0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "all_candidate_rank", "filters": [{"column": "race", "op": "eq", "value": "us-house-west"}, {"column": "county", "op": "eq", "value": "MISSOULA"}], "operation": "sum", "table": "county-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv
Evidence: [evidence/MT01-MISSOULA-REDUCTION-RANK.json](evidence/MT01-MISSOULA-REDUCTION-RANK.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. County House totals cover only the district portion.

## SENATE-BANKHEAD-WINS-BEAVERHEAD: PASS

Bankhead plurality wins in BEAVERHEAD

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "BEAVERHEAD"}], "filters": [{"column": "county", "value": "BEAVERHEAD"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-BEAVERHEAD.json](evidence/SENATE-BANKHEAD-WINS-BEAVERHEAD.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BEAVERHEAD-COMBINED-SHARE-2026: PASS

BEAVERHEAD: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 36.50408298388877 | Display: 36.5
Numerator / after operand: 0.3650408298388877 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "BEAVERHEAD"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BEAVERHEAD-COMBINED-SHARE-2026.json](evidence/SENATE-BEAVERHEAD-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BIG-HORN-COMBINED-SHARE-2026: PASS

BIG HORN: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 60.36113499570077 | Display: 60.4
Numerator / after operand: 0.6036113499570077 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "BIG HORN"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BIG-HORN-COMBINED-SHARE-2026.json](evidence/SENATE-BIG-HORN-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BLAINE-COMBINED-SHARE-2026: PASS

BLAINE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 53.88066397487663 | Display: 53.9
Numerator / after operand: 0.5388066397487663 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "BLAINE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BLAINE-COMBINED-SHARE-2026.json](evidence/SENATE-BLAINE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-BROADWATER: PASS

Bankhead plurality wins in BROADWATER

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 5 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "BROADWATER"}], "filters": [{"column": "county", "value": "BROADWATER"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-BROADWATER.json](evidence/SENATE-BANKHEAD-WINS-BROADWATER.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BROADWATER-COMBINED-SHARE-2026: PASS

BROADWATER: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 29.630620985010708 | Display: 29.6
Numerator / after operand: 0.2963062098501071 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "BROADWATER"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BROADWATER-COMBINED-SHARE-2026.json](evidence/SENATE-BROADWATER-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-CARBON: PASS

Bankhead plurality wins in CARBON

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 13 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "CARBON"}], "filters": [{"column": "county", "value": "CARBON"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-CARBON.json](evidence/SENATE-BANKHEAD-WINS-CARBON.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARBON-COMBINED-SHARE-2026: PASS

CARBON: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 43.29813160032494 | Display: 43.3
Numerator / after operand: 0.4329813160032494 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "CARBON"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARBON-COMBINED-SHARE-2026.json](evidence/SENATE-CARBON-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-CARTER: PASS

Bankhead plurality wins in CARTER

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "CARTER"}], "filters": [{"column": "county", "value": "CARTER"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-CARTER.json](evidence/SENATE-BANKHEAD-WINS-CARTER.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CARTER-COMBINED-SHARE-2026: PASS

CARTER: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 15.44011544011544 | Display: 15.4
Numerator / after operand: 0.1544011544011544 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "CARTER"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CARTER-COMBINED-SHARE-2026.json](evidence/SENATE-CARTER-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CASCADE-COMBINED-SHARE-2026: PASS

CASCADE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 50.1437802361379 | Display: 50.1
Numerator / after operand: 0.501437802361379 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "CASCADE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CASCADE-COMBINED-SHARE-2026.json](evidence/SENATE-CASCADE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-CHOUTEAU: PASS

Bankhead plurality wins in CHOUTEAU

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 9 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "CHOUTEAU"}], "filters": [{"column": "county", "value": "CHOUTEAU"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-CHOUTEAU.json](evidence/SENATE-BANKHEAD-WINS-CHOUTEAU.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CHOUTEAU-COMBINED-SHARE-2026: PASS

CHOUTEAU: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 42.137538326763035 | Display: 42.1
Numerator / after operand: 0.42137538326763035 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "CHOUTEAU"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CHOUTEAU-COMBINED-SHARE-2026.json](evidence/SENATE-CHOUTEAU-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-CUSTER: PASS

Bankhead plurality wins in CUSTER

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 12 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "CUSTER"}], "filters": [{"column": "county", "value": "CUSTER"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-CUSTER.json](evidence/SENATE-BANKHEAD-WINS-CUSTER.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-CUSTER-COMBINED-SHARE-2026: PASS

CUSTER: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 33.7962962962963 | Display: 33.8
Numerator / after operand: 0.33796296296296297 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "CUSTER"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-CUSTER-COMBINED-SHARE-2026.json](evidence/SENATE-CUSTER-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-DANIELS: PASS

Bankhead plurality wins in DANIELS

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "DANIELS"}], "filters": [{"column": "county", "value": "DANIELS"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-DANIELS.json](evidence/SENATE-BANKHEAD-WINS-DANIELS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DANIELS-COMBINED-SHARE-2026: PASS

DANIELS: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 23.638613861386137 | Display: 23.6
Numerator / after operand: 0.23638613861386137 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "DANIELS"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DANIELS-COMBINED-SHARE-2026.json](evidence/SENATE-DANIELS-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-DAWSON: PASS

Bankhead plurality wins in DAWSON

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 7 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "DAWSON"}], "filters": [{"column": "county", "value": "DAWSON"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-DAWSON.json](evidence/SENATE-BANKHEAD-WINS-DAWSON.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DAWSON-COMBINED-SHARE-2026: PASS

DAWSON: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 29.34328358208955 | Display: 29.3
Numerator / after operand: 0.2934328358208955 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "DAWSON"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DAWSON-COMBINED-SHARE-2026.json](evidence/SENATE-DAWSON-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-DEER-LODGE: PASS

Bankhead plurality wins in DEER LODGE

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 6 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "DEER LODGE"}], "filters": [{"column": "county", "value": "DEER LODGE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-DEER-LODGE.json](evidence/SENATE-BANKHEAD-WINS-DEER-LODGE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-DEER-LODGE-COMBINED-SHARE-2026: PASS

DEER LODGE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 61.71114991269644 | Display: 61.7
Numerator / after operand: 0.6171114991269644 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "DEER LODGE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-DEER-LODGE-COMBINED-SHARE-2026.json](evidence/SENATE-DEER-LODGE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-FALLON: PASS

Bankhead plurality wins in FALLON

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "FALLON"}], "filters": [{"column": "county", "value": "FALLON"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-FALLON.json](evidence/SENATE-BANKHEAD-WINS-FALLON.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FALLON-COMBINED-SHARE-2026: PASS

FALLON: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 19.42324003392706 | Display: 19.4
Numerator / after operand: 0.19423240033927058 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "FALLON"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FALLON-COMBINED-SHARE-2026.json](evidence/SENATE-FALLON-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-FERGUS: PASS

Bankhead plurality wins in FERGUS

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "FERGUS"}], "filters": [{"column": "county", "value": "FERGUS"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-FERGUS.json](evidence/SENATE-BANKHEAD-WINS-FERGUS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FERGUS-COMBINED-SHARE-2026: PASS

FERGUS: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 34.59189339255968 | Display: 34.6
Numerator / after operand: 0.34591893392559686 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "FERGUS"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FERGUS-COMBINED-SHARE-2026.json](evidence/SENATE-FERGUS-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-FLATHEAD: PASS

Bankhead plurality wins in FLATHEAD

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 56 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "FLATHEAD"}], "filters": [{"column": "county", "value": "FLATHEAD"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-FLATHEAD.json](evidence/SENATE-BANKHEAD-WINS-FLATHEAD.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-FLATHEAD-COMBINED-SHARE-2026: PASS

FLATHEAD: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 40.99604533671404 | Display: 41.0
Numerator / after operand: 0.4099604533671404 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "FLATHEAD"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-FLATHEAD-COMBINED-SHARE-2026.json](evidence/SENATE-FLATHEAD-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-GALLATIN: PASS

Bankhead plurality wins in GALLATIN

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 46 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "GALLATIN"}], "filters": [{"column": "county", "value": "GALLATIN"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-GALLATIN.json](evidence/SENATE-BANKHEAD-WINS-GALLATIN.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GALLATIN-COMBINED-SHARE-2026: PASS

GALLATIN: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 62.49480537470564 | Display: 62.5
Numerator / after operand: 0.6249480537470564 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "GALLATIN"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GALLATIN-COMBINED-SHARE-2026.json](evidence/SENATE-GALLATIN-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-GARFIELD: PASS

Bankhead plurality wins in GARFIELD

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "GARFIELD"}], "filters": [{"column": "county", "value": "GARFIELD"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-GARFIELD.json](evidence/SENATE-BANKHEAD-WINS-GARFIELD.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GARFIELD-COMBINED-SHARE-2026: PASS

GARFIELD: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 13.629402756508425 | Display: 13.6
Numerator / after operand: 0.13629402756508424 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "GARFIELD"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GARFIELD-COMBINED-SHARE-2026.json](evidence/SENATE-GARFIELD-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-GLACIER: PASS

Bankhead plurality wins in GLACIER

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "GLACIER"}], "filters": [{"column": "county", "value": "GLACIER"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-GLACIER.json](evidence/SENATE-BANKHEAD-WINS-GLACIER.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GLACIER-COMBINED-SHARE-2026: PASS

GLACIER: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 69.13887506222001 | Display: 69.1
Numerator / after operand: 0.6913887506222001 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "GLACIER"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GLACIER-COMBINED-SHARE-2026.json](evidence/SENATE-GLACIER-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-GOLDEN-VALLEY: PASS

Bankhead plurality wins in GOLDEN VALLEY

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 2 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "GOLDEN VALLEY"}], "filters": [{"column": "county", "value": "GOLDEN VALLEY"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-GOLDEN-VALLEY.json](evidence/SENATE-BANKHEAD-WINS-GOLDEN-VALLEY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GOLDEN-VALLEY-COMBINED-SHARE-2026: PASS

GOLDEN VALLEY: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 20.103092783505154 | Display: 20.1
Numerator / after operand: 0.20103092783505155 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "GOLDEN VALLEY"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GOLDEN-VALLEY-COMBINED-SHARE-2026.json](evidence/SENATE-GOLDEN-VALLEY-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-GRANITE: PASS

Bankhead plurality wins in GRANITE

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "GRANITE"}], "filters": [{"column": "county", "value": "GRANITE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-GRANITE.json](evidence/SENATE-BANKHEAD-WINS-GRANITE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-GRANITE-COMBINED-SHARE-2026: PASS

GRANITE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 38.40262582056893 | Display: 38.4
Numerator / after operand: 0.38402625820568925 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "GRANITE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-GRANITE-COMBINED-SHARE-2026.json](evidence/SENATE-GRANITE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-HILL-COMBINED-SHARE-2026: PASS

HILL: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 50.55501460564752 | Display: 50.6
Numerator / after operand: 0.5055501460564752 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "HILL"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-HILL-COMBINED-SHARE-2026.json](evidence/SENATE-HILL-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-JEFFERSON: PASS

Bankhead plurality wins in JEFFERSON

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 12 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "JEFFERSON"}], "filters": [{"column": "county", "value": "JEFFERSON"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-JEFFERSON.json](evidence/SENATE-BANKHEAD-WINS-JEFFERSON.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JEFFERSON-COMBINED-SHARE-2026: PASS

JEFFERSON: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 41.047074351077875 | Display: 41.0
Numerator / after operand: 0.4104707435107787 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "JEFFERSON"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JEFFERSON-COMBINED-SHARE-2026.json](evidence/SENATE-JEFFERSON-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-JUDITH-BASIN: PASS

Bankhead plurality wins in JUDITH BASIN

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "JUDITH BASIN"}], "filters": [{"column": "county", "value": "JUDITH BASIN"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-JUDITH-BASIN.json](evidence/SENATE-BANKHEAD-WINS-JUDITH-BASIN.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-JUDITH-BASIN-COMBINED-SHARE-2026: PASS

JUDITH BASIN: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 31.615120274914087 | Display: 31.6
Numerator / after operand: 0.3161512027491409 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "JUDITH BASIN"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-JUDITH-BASIN-COMBINED-SHARE-2026.json](evidence/SENATE-JUDITH-BASIN-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-LAKE: PASS

Bankhead plurality wins in LAKE

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 22 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "LAKE"}], "filters": [{"column": "county", "value": "LAKE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-LAKE.json](evidence/SENATE-BANKHEAD-WINS-LAKE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LAKE-COMBINED-SHARE-2026: PASS

LAKE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 47.93300071275837 | Display: 47.9
Numerator / after operand: 0.4793300071275837 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "LAKE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LAKE-COMBINED-SHARE-2026.json](evidence/SENATE-LAKE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-LEWIS-AND-CLARK: PASS

Bankhead plurality wins in LEWIS AND CLARK

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 32 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "LEWIS AND CLARK"}], "filters": [{"column": "county", "value": "LEWIS AND CLARK"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-LEWIS-AND-CLARK.json](evidence/SENATE-BANKHEAD-WINS-LEWIS-AND-CLARK.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LEWIS-AND-CLARK-COMBINED-SHARE-2026: PASS

LEWIS AND CLARK: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 57.783301902965874 | Display: 57.8
Numerator / after operand: 0.5778330190296588 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "LEWIS AND CLARK"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LEWIS-AND-CLARK-COMBINED-SHARE-2026.json](evidence/SENATE-LEWIS-AND-CLARK-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-LIBERTY: PASS

Bankhead plurality wins in LIBERTY

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "LIBERTY"}], "filters": [{"column": "county", "value": "LIBERTY"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-LIBERTY.json](evidence/SENATE-BANKHEAD-WINS-LIBERTY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LIBERTY-COMBINED-SHARE-2026: PASS

LIBERTY: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 34.67011642949547 | Display: 34.7
Numerator / after operand: 0.34670116429495473 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "LIBERTY"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LIBERTY-COMBINED-SHARE-2026.json](evidence/SENATE-LIBERTY-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-LINCOLN: PASS

Bankhead plurality wins in LINCOLN

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 16 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "LINCOLN"}], "filters": [{"column": "county", "value": "LINCOLN"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-LINCOLN.json](evidence/SENATE-BANKHEAD-WINS-LINCOLN.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-LINCOLN-COMBINED-SHARE-2026: PASS

LINCOLN: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 28.72020829160825 | Display: 28.7
Numerator / after operand: 0.2872020829160825 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "LINCOLN"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-LINCOLN-COMBINED-SHARE-2026.json](evidence/SENATE-LINCOLN-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-MADISON: PASS

Bankhead plurality wins in MADISON

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 11 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "MADISON"}], "filters": [{"column": "county", "value": "MADISON"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-MADISON.json](evidence/SENATE-BANKHEAD-WINS-MADISON.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MADISON-COMBINED-SHARE-2026: PASS

MADISON: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 36.91313438509789 | Display: 36.9
Numerator / after operand: 0.3691313438509789 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "MADISON"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MADISON-COMBINED-SHARE-2026.json](evidence/SENATE-MADISON-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-MCCONE: PASS

Bankhead plurality wins in MCCONE

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 3 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "MCCONE"}], "filters": [{"column": "county", "value": "MCCONE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-MCCONE.json](evidence/SENATE-BANKHEAD-WINS-MCCONE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MCCONE-COMBINED-SHARE-2026: PASS

MCCONE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 20.374707259953162 | Display: 20.4
Numerator / after operand: 0.20374707259953162 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "MCCONE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MCCONE-COMBINED-SHARE-2026.json](evidence/SENATE-MCCONE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-MEAGHER: PASS

Bankhead plurality wins in MEAGHER

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "MEAGHER"}], "filters": [{"column": "county", "value": "MEAGHER"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-MEAGHER.json](evidence/SENATE-BANKHEAD-WINS-MEAGHER.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MEAGHER-COMBINED-SHARE-2026: PASS

MEAGHER: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 30.107526881720432 | Display: 30.1
Numerator / after operand: 0.3010752688172043 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "MEAGHER"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MEAGHER-COMBINED-SHARE-2026.json](evidence/SENATE-MEAGHER-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-MINERAL: PASS

Bankhead plurality wins in MINERAL

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 6 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "MINERAL"}], "filters": [{"column": "county", "value": "MINERAL"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-MINERAL.json](evidence/SENATE-BANKHEAD-WINS-MINERAL.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MINERAL-COMBINED-SHARE-2026: PASS

MINERAL: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 35.975103734439834 | Display: 36.0
Numerator / after operand: 0.35975103734439834 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "MINERAL"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MINERAL-COMBINED-SHARE-2026.json](evidence/SENATE-MINERAL-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-MISSOULA: PASS

Bankhead plurality wins in MISSOULA

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 65 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "MISSOULA"}], "filters": [{"column": "county", "value": "MISSOULA"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-MISSOULA.json](evidence/SENATE-BANKHEAD-WINS-MISSOULA.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MISSOULA-COMBINED-SHARE-2026: PASS

MISSOULA: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 71.93328695989777 | Display: 71.9
Numerator / after operand: 0.7193328695989777 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "MISSOULA"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MISSOULA-COMBINED-SHARE-2026.json](evidence/SENATE-MISSOULA-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-MUSSELSHELL: PASS

Bankhead plurality wins in MUSSELSHELL

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 6 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "MUSSELSHELL"}], "filters": [{"column": "county", "value": "MUSSELSHELL"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-MUSSELSHELL.json](evidence/SENATE-BANKHEAD-WINS-MUSSELSHELL.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-MUSSELSHELL-COMBINED-SHARE-2026: PASS

MUSSELSHELL: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 22.11657709797437 | Display: 22.1
Numerator / after operand: 0.22116577097974371 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "MUSSELSHELL"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-MUSSELSHELL-COMBINED-SHARE-2026.json](evidence/SENATE-MUSSELSHELL-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-PARK: PASS

Bankhead plurality wins in PARK

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 12 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "PARK"}], "filters": [{"column": "county", "value": "PARK"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-PARK.json](evidence/SENATE-BANKHEAD-WINS-PARK.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PARK-COMBINED-SHARE-2026: PASS

PARK: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 56.534859521331946 | Display: 56.5
Numerator / after operand: 0.5653485952133195 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "PARK"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PARK-COMBINED-SHARE-2026.json](evidence/SENATE-PARK-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-PETROLEUM: PASS

Bankhead plurality wins in PETROLEUM

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "PETROLEUM"}], "filters": [{"column": "county", "value": "PETROLEUM"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-PETROLEUM.json](evidence/SENATE-BANKHEAD-WINS-PETROLEUM.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PETROLEUM-COMBINED-SHARE-2026: PASS

PETROLEUM: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 15.999999999999998 | Display: 16.0
Numerator / after operand: 0.15999999999999998 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "PETROLEUM"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PETROLEUM-COMBINED-SHARE-2026.json](evidence/SENATE-PETROLEUM-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-PHILLIPS: PASS

Bankhead plurality wins in PHILLIPS

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "PHILLIPS"}], "filters": [{"column": "county", "value": "PHILLIPS"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-PHILLIPS.json](evidence/SENATE-BANKHEAD-WINS-PHILLIPS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PHILLIPS-COMBINED-SHARE-2026: PASS

PHILLIPS: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 24.92581602373887 | Display: 24.9
Numerator / after operand: 0.24925816023738873 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "PHILLIPS"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PHILLIPS-COMBINED-SHARE-2026.json](evidence/SENATE-PHILLIPS-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-PONDERA: PASS

Bankhead plurality wins in PONDERA

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 8 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "PONDERA"}], "filters": [{"column": "county", "value": "PONDERA"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-PONDERA.json](evidence/SENATE-BANKHEAD-WINS-PONDERA.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PONDERA-COMBINED-SHARE-2026: PASS

PONDERA: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 36.80679785330948 | Display: 36.8
Numerator / after operand: 0.3680679785330948 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "PONDERA"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PONDERA-COMBINED-SHARE-2026.json](evidence/SENATE-PONDERA-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-POWDER-RIVER: PASS

Bankhead plurality wins in POWDER RIVER

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 6 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "POWDER RIVER"}], "filters": [{"column": "county", "value": "POWDER RIVER"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-POWDER-RIVER.json](evidence/SENATE-BANKHEAD-WINS-POWDER-RIVER.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWDER-RIVER-COMBINED-SHARE-2026: PASS

POWDER RIVER: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 21.97055492638732 | Display: 22.0
Numerator / after operand: 0.21970554926387317 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "POWDER RIVER"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWDER-RIVER-COMBINED-SHARE-2026.json](evidence/SENATE-POWDER-RIVER-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-POWELL: PASS

Bankhead plurality wins in POWELL

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 13 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "POWELL"}], "filters": [{"column": "county", "value": "POWELL"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-POWELL.json](evidence/SENATE-BANKHEAD-WINS-POWELL.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-POWELL-COMBINED-SHARE-2026: PASS

POWELL: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 31.639281620175773 | Display: 31.6
Numerator / after operand: 0.31639281620175774 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "POWELL"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-POWELL-COMBINED-SHARE-2026.json](evidence/SENATE-POWELL-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-PRAIRIE: PASS

Bankhead plurality wins in PRAIRIE

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "PRAIRIE"}], "filters": [{"column": "county", "value": "PRAIRIE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-PRAIRIE.json](evidence/SENATE-BANKHEAD-WINS-PRAIRIE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-PRAIRIE-COMBINED-SHARE-2026: PASS

PRAIRIE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 27.147766323024058 | Display: 27.1
Numerator / after operand: 0.2714776632302406 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "PRAIRIE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-PRAIRIE-COMBINED-SHARE-2026.json](evidence/SENATE-PRAIRIE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-RAVALLI: PASS

Bankhead plurality wins in RAVALLI

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 25 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "RAVALLI"}], "filters": [{"column": "county", "value": "RAVALLI"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-RAVALLI.json](evidence/SENATE-BANKHEAD-WINS-RAVALLI.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RAVALLI-COMBINED-SHARE-2026: PASS

RAVALLI: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 38.83758157862333 | Display: 38.8
Numerator / after operand: 0.38837581578623326 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "RAVALLI"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RAVALLI-COMBINED-SHARE-2026.json](evidence/SENATE-RAVALLI-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-RICHLAND: PASS

Bankhead plurality wins in RICHLAND

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 14 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "RICHLAND"}], "filters": [{"column": "county", "value": "RICHLAND"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-RICHLAND.json](evidence/SENATE-BANKHEAD-WINS-RICHLAND.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-RICHLAND-COMBINED-SHARE-2026: PASS

RICHLAND: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 24.143600986571663 | Display: 24.1
Numerator / after operand: 0.24143600986571664 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "RICHLAND"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-RICHLAND-COMBINED-SHARE-2026.json](evidence/SENATE-RICHLAND-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROOSEVELT-COMBINED-SHARE-2026: PASS

ROOSEVELT: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 54.29243433947472 | Display: 54.3
Numerator / after operand: 0.5429243433947472 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "ROOSEVELT"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROOSEVELT-COMBINED-SHARE-2026.json](evidence/SENATE-ROOSEVELT-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-ROSEBUD: PASS

Bankhead plurality wins in ROSEBUD

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 12 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "ROSEBUD"}], "filters": [{"column": "county", "value": "ROSEBUD"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-ROSEBUD.json](evidence/SENATE-BANKHEAD-WINS-ROSEBUD.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-ROSEBUD-COMBINED-SHARE-2026: PASS

ROSEBUD: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 38.65997850232892 | Display: 38.7
Numerator / after operand: 0.3865997850232892 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "ROSEBUD"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-ROSEBUD-COMBINED-SHARE-2026.json](evidence/SENATE-ROSEBUD-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-SANDERS: PASS

Bankhead plurality wins in SANDERS

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 9 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "SANDERS"}], "filters": [{"column": "county", "value": "SANDERS"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-SANDERS.json](evidence/SENATE-BANKHEAD-WINS-SANDERS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SANDERS-COMBINED-SHARE-2026: PASS

SANDERS: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 29.294593380260597 | Display: 29.3
Numerator / after operand: 0.292945933802606 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "SANDERS"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SANDERS-COMBINED-SHARE-2026.json](evidence/SENATE-SANDERS-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-SHERIDAN: PASS

Bankhead plurality wins in SHERIDAN

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 6 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "SHERIDAN"}], "filters": [{"column": "county", "value": "SHERIDAN"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-SHERIDAN.json](evidence/SENATE-BANKHEAD-WINS-SHERIDAN.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SHERIDAN-COMBINED-SHARE-2026: PASS

SHERIDAN: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 36.304909560723516 | Display: 36.3
Numerator / after operand: 0.36304909560723514 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "SHERIDAN"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SHERIDAN-COMBINED-SHARE-2026.json](evidence/SENATE-SHERIDAN-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-SILVER-BOW: PASS

Bankhead plurality wins in SILVER BOW

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 31 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "SILVER BOW"}], "filters": [{"column": "county", "value": "SILVER BOW"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-SILVER-BOW.json](evidence/SENATE-BANKHEAD-WINS-SILVER-BOW.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SILVER-BOW-COMBINED-SHARE-2026: PASS

SILVER BOW: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 65.56470111995682 | Display: 65.6
Numerator / after operand: 0.6556470111995683 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "SILVER BOW"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SILVER-BOW-COMBINED-SHARE-2026.json](evidence/SENATE-SILVER-BOW-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-STILLWATER: PASS

Bankhead plurality wins in STILLWATER

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 9 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "STILLWATER"}], "filters": [{"column": "county", "value": "STILLWATER"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-STILLWATER.json](evidence/SENATE-BANKHEAD-WINS-STILLWATER.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-STILLWATER-COMBINED-SHARE-2026: PASS

STILLWATER: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 28.0968096809681 | Display: 28.1
Numerator / after operand: 0.280968096809681 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "STILLWATER"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-STILLWATER-COMBINED-SHARE-2026.json](evidence/SENATE-STILLWATER-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-SWEET-GRASS: PASS

Bankhead plurality wins in SWEET GRASS

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 5 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "SWEET GRASS"}], "filters": [{"column": "county", "value": "SWEET GRASS"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-SWEET-GRASS.json](evidence/SENATE-BANKHEAD-WINS-SWEET-GRASS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-SWEET-GRASS-COMBINED-SHARE-2026: PASS

SWEET GRASS: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 34.52566096423017 | Display: 34.5
Numerator / after operand: 0.3452566096423017 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "SWEET GRASS"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-SWEET-GRASS-COMBINED-SHARE-2026.json](evidence/SENATE-SWEET-GRASS-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-TETON: PASS

Bankhead plurality wins in TETON

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 5 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "TETON"}], "filters": [{"column": "county", "value": "TETON"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-TETON.json](evidence/SENATE-BANKHEAD-WINS-TETON.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TETON-COMBINED-SHARE-2026: PASS

TETON: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 35.6743535988819 | Display: 35.7
Numerator / after operand: 0.356743535988819 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "TETON"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TETON-COMBINED-SHARE-2026.json](evidence/SENATE-TETON-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-TOOLE: PASS

Bankhead plurality wins in TOOLE

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 5 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "TOOLE"}], "filters": [{"column": "county", "value": "TOOLE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-TOOLE.json](evidence/SENATE-BANKHEAD-WINS-TOOLE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TOOLE-COMBINED-SHARE-2026: PASS

TOOLE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 29.000000000000004 | Display: 29.0
Numerator / after operand: 0.29000000000000004 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "TOOLE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TOOLE-COMBINED-SHARE-2026.json](evidence/SENATE-TOOLE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-TREASURE: PASS

Bankhead plurality wins in TREASURE

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "TREASURE"}], "filters": [{"column": "county", "value": "TREASURE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-TREASURE.json](evidence/SENATE-BANKHEAD-WINS-TREASURE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-TREASURE-COMBINED-SHARE-2026: PASS

TREASURE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 18.559556786703602 | Display: 18.6
Numerator / after operand: 0.18559556786703602 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "TREASURE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-TREASURE-COMBINED-SHARE-2026.json](evidence/SENATE-TREASURE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-VALLEY: PASS

Bankhead plurality wins in VALLEY

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 4 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "VALLEY"}], "filters": [{"column": "county", "value": "VALLEY"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-VALLEY.json](evidence/SENATE-BANKHEAD-WINS-VALLEY.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-VALLEY-COMBINED-SHARE-2026: PASS

VALLEY: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 34.99838865613922 | Display: 35.0
Numerator / after operand: 0.3499838865613922 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "VALLEY"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-VALLEY-COMBINED-SHARE-2026.json](evidence/SENATE-VALLEY-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-WHEATLAND: PASS

Bankhead plurality wins in WHEATLAND

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 5 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "WHEATLAND"}], "filters": [{"column": "county", "value": "WHEATLAND"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-WHEATLAND.json](evidence/SENATE-BANKHEAD-WINS-WHEATLAND.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WHEATLAND-COMBINED-SHARE-2026: PASS

WHEATLAND: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 29.965156794425084 | Display: 30.0
Numerator / after operand: 0.29965156794425085 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "WHEATLAND"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WHEATLAND-COMBINED-SHARE-2026.json](evidence/SENATE-WHEATLAND-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-WIBAUX: PASS

Bankhead plurality wins in WIBAUX

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "WIBAUX"}], "filters": [{"column": "county", "value": "WIBAUX"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-WIBAUX.json](evidence/SENATE-BANKHEAD-WINS-WIBAUX.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-WIBAUX-COMBINED-SHARE-2026: PASS

WIBAUX: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 19.426048565121413 | Display: 19.4
Numerator / after operand: 0.19426048565121412 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "WIBAUX"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-WIBAUX-COMBINED-SHARE-2026.json](evidence/SENATE-WIBAUX-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-WINS-YELLOWSTONE: PASS

Bankhead plurality wins in YELLOWSTONE

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 59 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "county", "value": "YELLOWSTONE"}], "filters": [{"column": "county", "value": "YELLOWSTONE"}, {"column": "winning_candidate", "value": "ALANI BANKHEAD"}], "operation": "count", "table": "senate-precinct-winners-2026"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-WINS-YELLOWSTONE.json](evidence/SENATE-BANKHEAD-WINS-YELLOWSTONE.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-YELLOWSTONE-COMBINED-SHARE-2026: PASS

YELLOWSTONE: combined Bodnar–Bankhead 2026 share (%)

Expected: None | Calculated: 46.2395411499614 | Display: 46.2
Numerator / after operand: 0.46239541149961394 | Denominator / before operand: 1 (eligible rows or contest votes)

Calculation: `{"column": "combined_bodnar_bankhead_share_2026", "filters": [{"column": "county", "value": "YELLOWSTONE"}], "operation": "sum", "scale": 100, "table": "senate-county-summary"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-YELLOWSTONE-COMBINED-SHARE-2026.json](evidence/SENATE-YELLOWSTONE-COMBINED-SHARE-2026.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-VS-BANKHEAD-NO-VOTES: PASS

2026 bodnar_vs_bankhead: no-vote precincts

Expected: 1 | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bodnar_vs_bankhead", "value": "no_votes"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-VS-BANKHEAD-NO-VOTES.json](evidence/SENATE-BODNAR-VS-BANKHEAD-NO-VOTES.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BANKHEAD-VS-ALME-NO-VOTES: PASS

2026 bankhead_vs_alme: no-vote precincts

Expected: 1 | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bankhead_vs_alme", "value": "no_votes"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BANKHEAD-VS-ALME-NO-VOTES.json](evidence/SENATE-BANKHEAD-VS-ALME-NO-VOTES.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## SENATE-BODNAR-VS-ALME-NO-VOTES: PASS

2026 bodnar_vs_alme: no-vote precincts

Expected: 1 | Calculated: 1 | Display: 1
Numerator / after operand: 1 | Denominator / before operand: 728 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [], "filters": [{"column": "bodnar_vs_alme", "value": "no_votes"}], "operation": "count", "table": "senate-bodnar-bankhead-comparison"}`

Sources: cleaned/2026/general/precinct-results.csv
Evidence: [evidence/SENATE-BODNAR-VS-ALME-NO-VOTES.json](evidence/SENATE-BODNAR-VS-ALME-NO-VOTES.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement.

## MT01-VERIFIED-R-TO-D-FLIPS: PASS

MT-01: Republican_to_Democrat flips in documented comparable precincts

Expected: None | Calculated: 3 | Display: 3
Numerator / after operand: 3 | Denominator / before operand: 23 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "value": true}], "filters": [{"column": "geographically_verified", "value": true}, {"column": "flip", "value": "Republican_to_Democrat"}], "operation": "count", "table": "mt01-precinct-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/MT01-VERIFIED-R-TO-D-FLIPS.json](evidence/MT01-VERIFIED-R-TO-D-FLIPS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## MT01-VERIFIED-D-TO-R-FLIPS: PASS

MT-01: Democrat_to_Republican flips in documented comparable precincts

Expected: None | Calculated: 0 | Display: 0
Numerator / after operand: 0 | Denominator / before operand: 23 (eligible rows or contest votes)

Calculation: `{"denominator_filters": [{"column": "geographically_verified", "value": true}], "filters": [{"column": "geographically_verified", "value": true}, {"column": "flip", "value": "Democrat_to_Republican"}], "operation": "count", "table": "mt01-precinct-swings"}`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/MT01-VERIFIED-D-TO-R-FLIPS.json](evidence/MT01-VERIFIED-D-TO-R-FLIPS.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.

## MT01-VERIFIED-LARGEST-R-SHARE-DECREASE-MIN-100: PASS

Most negative Republican share change among verified MT-01 precincts with at least 100 votes in both elections (pp)

Expected: None | Calculated: -7.582205029013533 | Display: -7.58
Numerator / after operand: -7.582205029013533 | Denominator / before operand: 22 (eligible rows or contest votes)

Calculation: `Minimum unrounded Republican all-candidate share change (pp), across all verified MT-01 precincts with at least 100 contest votes in both years.`

Sources: cleaned/2024/general/precinct-results.csv, cleaned/2026/general/precinct-results.csv, analysis/election_swings/geographic-reviews.json
Evidence: [evidence/MT01-VERIFIED-LARGEST-R-SHARE-DECREASE-MIN-100.json](evidence/MT01-VERIFIED-LARGEST-R-SHARE-DECREASE-MIN-100.json)

Caveats: Snapshot arithmetic only; 2026 unofficial, write-ins excluded, 727/728 reporting with one partial. Aggregate comparisons do not identify individual voter movement. Restricted to independently documented geography; sample is not statewide representative.
