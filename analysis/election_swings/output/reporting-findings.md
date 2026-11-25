# Reporting findings: 2024 versus 2026



All findings describe the retained SOS snapshots. The 2026 capture is Nov. 20, 2026, unofficial, excludes write-ins, and reports 727/728 precincts with one partial. The 2024 retained exports also say unofficial; write-in coverage is unestablished. Export coverage is not certification or completed counting.

Source commit: `f265c997357082f30e3ca7dd680376c8bb19517d`. See source-reconciliation.json for hashes, original headers, dates and each comparison. No fresh election results are downloaded by this tool.



## A. MT-01



Republican share fell from 52.29 [MT01-R-SHARE-2024]% to 46.64 [MT01-R-SHARE-2026]%. Democratic share went from 44.62 [MT01-D-SHARE-2024]% to 50.48 [MT01-D-SHARE-2026]%. The Republican-minus-Democratic margin changed by -11.52 [MT01-MARGIN-CHANGE] percentage points (negative means toward Democrats).

Republican share declined in 15 [MT01-COUNTIES-DECLINED] county portions and increased in 1 [MT01-COUNTIES-INCREASED]. Gallatin and Missoula rank 1 [MT01-GALLATIN-REDUCTION-RANK] and 2 [MT01-MISSOULA-REDUCTION-RANK] for the largest reductions.



- Gallatin: -7.42 [MT01-GALLATIN-R-SHARE-CHANGE] pp in Republican all-candidate share.

- Missoula: -6.47 [MT01-MISSOULA-R-SHARE-CHANGE] pp in Republican all-candidate share.

- Silver Bow: -5.96 [MT01-SILVER-BOW-R-SHARE-CHANGE] pp in Republican all-candidate share.

- Madison: -5.91 [MT01-MADISON-R-SHARE-CHANGE] pp in Republican all-candidate share.

- Flathead: -5.07 [MT01-FLATHEAD-R-SHARE-CHANGE] pp in Republican all-candidate share.

- Ravalli: -4.89 [MT01-RAVALLI-R-SHARE-CHANGE] pp in Republican all-candidate share.

- Pondera: 2.05 [MT01-PONDERA-R-SHARE-CHANGE] pp in Republican all-candidate share.



In the documented MT-01 sample, Lake / RON-03 HD13 had the largest Republican-share reduction among precincts with at least 100 votes in both years: -7.58 [MT01-VERIFIED-LARGEST-R-SHARE-DECREASE-MIN-100] pp. The verified sample contained 3 [MT01-VERIFIED-R-TO-D-FLIPS] Republican-to-Democratic plurality flips and 0 [MT01-VERIFIED-D-TO-R-FLIPS] in the other direction. These describe only the documented sample.



Pondera’s western House portion has 4 [MT01-PONDERA-PRECINCTS-2026] precinct records and 673 [MT01-PONDERA-VOTES-2026] contest votes in 2026. Its eastern portion has 5 [MT02-PONDERA-PRECINCTS-2026] records. Valier Rural appears in both House contests; these are district portions, not duplicate votes. Countywide Senate votes cannot be assigned to the western portion.

Geographically checked MT-01 comparisons cover 23 [MT01-COVERAGE-VERIFIED-MATCHED-PRECINCTS] precincts. The larger name-matched sample covers 309 [MT01-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS] and remains provisional. The verified ranking files apply no minimum, a minimum of 100 votes in both years, and a minimum of 300 in both years; these are limited samples, not districtwide precinct rankings.



## B. Senate candidate patterns



2024 plurality wins: Sheehy 497 [SENATE-SHEEHY-WINS-2024], Tester 228 [SENATE-TESTER-WINS-2024]. 2026: Alme 532 [SENATE-ALME-WINS-2026], Bodnar 180 [SENATE-BODNAR-WINS-2026], Bankhead 15 [SENATE-BANKHEAD-WINS-2026]. Ties and zero votes are separate rows in winner-summary.csv.

Bodnar outpolled Bankhead in 704 [SENATE-BODNAR-VS-BANKHEAD-BODNAR] precincts. Among Bodnar’s precinct wins, Bankhead trailed Alme in 131 [SENATE-BODNAR-WINS-BANKHEAD-TRAILS-ALME]. Bodnar accounted for 92.3 [SENATE-BODNAR-SHARE-NONREPUBLICAN-WINS]% of non-Republican plurality wins.



Bankhead’s precinct wins by county:



- Big Horn: 7 [SENATE-BANKHEAD-WINS-BIG-HORN].

- Blaine: 3 [SENATE-BANKHEAD-WINS-BLAINE].

- Roosevelt: 3 [SENATE-BANKHEAD-WINS-ROOSEVELT].

- Cascade: 1 [SENATE-BANKHEAD-WINS-CASCADE].

- Hill: 1 [SENATE-BANKHEAD-WINS-HILL].



Highest Bodnar county vote shares (all precincts, vote-weighted):



- Missoula: 59.12 [SENATE-MISSOULA-SETH-BODNAR-2026]%.

- Silver Bow: 48.73 [SENATE-SILVER-BOW-SETH-BODNAR-2026]%.

- Gallatin: 48.29 [SENATE-GALLATIN-SETH-BODNAR-2026]%.

- Lewis And Clark: 48.01 [SENATE-LEWIS-AND-CLARK-SETH-BODNAR-2026]%.

- Deer Lodge: 45.52 [SENATE-DEER-LODGE-SETH-BODNAR-2026]%.

- Park: 44.17 [SENATE-PARK-SETH-BODNAR-2026]%.



The full precinct list, candidate counts, totals, winner shares and margins are in senate-bankhead-wins.csv. County shares include every precinct, including those she did not win. High county shares describe geographic concentration and do not establish voters’ race, ethnicity or ideology.



Highest Bankhead county vote shares (all precincts, vote-weighted):



- Big Horn: Bankhead 28.58 [SENATE-BIG-HORN-ALANI-BANKHEAD-2026]%; Bodnar 31.79 [SENATE-BIG-HORN-SETH-BODNAR-2026]%.

- Glacier: Bankhead 27.53 [SENATE-GLACIER-ALANI-BANKHEAD-2026]%; Bodnar 41.61 [SENATE-GLACIER-SETH-BODNAR-2026]%.

- Roosevelt: Bankhead 26.70 [SENATE-ROOSEVELT-ALANI-BANKHEAD-2026]%; Bodnar 27.60 [SENATE-ROOSEVELT-SETH-BODNAR-2026]%.

- Blaine: Bankhead 23.06 [SENATE-BLAINE-ALANI-BANKHEAD-2026]%; Bodnar 30.82 [SENATE-BLAINE-SETH-BODNAR-2026]%.

- Hill: Bankhead 17.70 [SENATE-HILL-ALANI-BANKHEAD-2026]%; Bodnar 32.85 [SENATE-HILL-SETH-BODNAR-2026]%.

- Silver Bow: Bankhead 16.83 [SENATE-SILVER-BOW-ALANI-BANKHEAD-2026]%; Bodnar 48.73 [SENATE-SILVER-BOW-SETH-BODNAR-2026]%.



In the provisional matched sample, 219 [SENATE-TESTER-MATCHED] Tester-winning precincts split as follows: Bodnar 170 [SENATE-TESTER-TO-BODNAR], Alme 35 [SENATE-TESTER-TO-ALME], Bankhead 14 [SENATE-TESTER-TO-BANKHEAD]. Bankhead trailed Alme in 161 [SENATE-TESTER-BANKHEAD-TRAILS-ALME] of these precincts. That last comparison does not mean Alme won all of them; Bodnar could win while Alme finished ahead of Bankhead.

The independently checked sample includes 8 [SENATE-TESTER-MATCHED-VERIFIED] Tester precincts: 2 [SENATE-TESTER-TO-BODNAR-VERIFIED] Bodnar, 6 [SENATE-TESTER-TO-ALME-VERIFIED] Alme, 0 [SENATE-TESTER-TO-BANKHEAD-VERIFIED] Bankhead. These are sample counts, not estimates for excluded precincts.

The name-matched Senate sample contains 689 [SENATE-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS] precincts, excluding 38 [SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024] from 2024 and 39 [SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026] from 2026. Excluded vote shares: 3.02 [SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024]% and 2.97 [SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026]%, respectively. Unpaired and changed-boundary precincts remain in the audit.

Republican Senate share declined in 48 [SENATE-COUNTIES-DECLINED] counties and increased in 8 [SENATE-COUNTIES-INCREASED]. The increases were:



- Blaine: 4.93 [SENATE-BLAINE-R-SHARE-CHANGE] pp.

- Treasure: 3.78 [SENATE-TREASURE-R-SHARE-CHANGE] pp.

- Roosevelt: 2.41 [SENATE-ROOSEVELT-R-SHARE-CHANGE] pp.

- Wibaux: 1.77 [SENATE-WIBAUX-R-SHARE-CHANGE] pp.

- Big Horn: 1.66 [SENATE-BIG-HORN-R-SHARE-CHANGE] pp.

- Glacier: 1.47 [SENATE-GLACIER-R-SHARE-CHANGE] pp.

- Powell: 0.82 [SENATE-POWELL-R-SHARE-CHANGE] pp.

- Sheridan: 0.14 [SENATE-SHERIDAN-R-SHARE-CHANGE] pp.



Counties of particular interest:



- Gallatin: Republican share change -7.24 [SENATE-GALLATIN-R-SHARE-CHANGE] pp; Bodnar 48.29 [SENATE-GALLATIN-SETH-BODNAR-2026]%, Bankhead 14.21 [SENATE-GALLATIN-ALANI-BANKHEAD-2026]% in 2026.

- Missoula: Republican share change -5.45 [SENATE-MISSOULA-R-SHARE-CHANGE] pp; Bodnar 59.12 [SENATE-MISSOULA-SETH-BODNAR-2026]%, Bankhead 12.82 [SENATE-MISSOULA-ALANI-BANKHEAD-2026]% in 2026.

- Blaine: Republican share change 4.93 [SENATE-BLAINE-R-SHARE-CHANGE] pp; Bodnar 30.82 [SENATE-BLAINE-SETH-BODNAR-2026]%, Bankhead 23.06 [SENATE-BLAINE-ALANI-BANKHEAD-2026]% in 2026.

- Big Horn: Republican share change 1.66 [SENATE-BIG-HORN-R-SHARE-CHANGE] pp; Bodnar 31.79 [SENATE-BIG-HORN-SETH-BODNAR-2026]%, Bankhead 28.58 [SENATE-BIG-HORN-ALANI-BANKHEAD-2026]% in 2026.

- Glacier: Republican share change 1.47 [SENATE-GLACIER-R-SHARE-CHANGE] pp; Bodnar 41.61 [SENATE-GLACIER-SETH-BODNAR-2026]%, Bankhead 27.53 [SENATE-GLACIER-ALANI-BANKHEAD-2026]% in 2026.

- Roosevelt: Republican share change 2.41 [SENATE-ROOSEVELT-R-SHARE-CHANGE] pp; Bodnar 27.60 [SENATE-ROOSEVELT-SETH-BODNAR-2026]%, Bankhead 26.70 [SENATE-ROOSEVELT-ALANI-BANKHEAD-2026]% in 2026.



## C. MT-02



Republican all-candidate share was 65.99 [MT02-R-SHARE-2024]% in 2024 and 58.10 [MT02-R-SHARE-2026]% in 2026. The 2026 Republican two-party share was 64.29 [MT02-R-TWO-PARTY-2026]%. Eisenhauer received 17199 [MT02-I-VOTES-2026] votes, 7.80 [MT02-I-SHARE-2026]% of the total. Independent votes remain separate from Democratic votes.

All-candidate Republican share decreased in 41 [MT02-COUNTIES-DECLINED] county portions and increased in 0 [MT02-COUNTIES-INCREASED]. Under the two-party measure it decreased in 25 [MT02-COUNTIES-DECLINED-TWO-PARTY] and increased in 16 [MT02-COUNTIES-INCREASED-TWO-PARTY]. Compare both rankings before describing the scale of a swing.



## D. Other reporting leads



1. Alme won 89 [SENATE-R-PLURALITY-BELOW-50-2026] precincts with strictly less than half the vote. Plurality wins and majorities describe different maps.

2. Bankhead won majorities in 2 [SENATE-BANKHEAD-MAJORITIES-2026] precincts; Bodnar did so in 103 [SENATE-BODNAR-MAJORITIES-2026]. Compare these with plurality wins before writing about strongholds.

3. Bodnar and Bankhead combined exceeded Alme in 267 [SENATE-COMBINED-EXCEEDS-ALME] precincts. This describes observed totals; it cannot establish the result of a hypothetical two-person election.

4. Bankhead’s share was below 20% in 147 [SENATE-TESTER-BANKHEAD-BELOW-20PCT] provisional Tester precincts. The geographically reviewed counterpart is 8 [SENATE-TESTER-BANKHEAD-BELOW-20PCT-VERIFIED]. Explore differences within the samples rather than generalizing to all Tester precincts.

5. The combined Bodnar–Bankhead share exceeded Tester’s former share in 174 [SENATE-TESTER-COMBINED-EXCEEDS-TESTER-SHARE] name-matched Tester precincts. This remains provisional and does not show that the same people changed preferences.

6. Republican two-party share in MT-02 changed by -1.70 [MT02-TWO-PARTY-CHANGE] pp, while all-candidate share changed by -7.89 [MT02-R-SHARE-CHANGE] pp. The independent vote is central to describing that difference.

7. The MT-01 Republican two-party change was -5.94 [MT01-TWO-PARTY-CHANGE] pp. Compare it with the all-candidate share change of -5.66 [MT01-R-SHARE-CHANGE] pp when assessing third-party denominator effects.



## Geographic review still needed



Lake’s county map explicitly covers 2024–2032; the verified subset uses its precinct identifiers and the 2026 judge-training legislative assignments. Beaverhead precinct 12 is supported by an explicit continuity statement in Resolution 2026-04. The five affected Dillon-area precincts are excluded. Verification methods and limitations are recorded per row; no statewide polygon overlay was performed.

Missoula’s April 2026 announcement documents polling-place relocations from Lowell and C.S. Porter, suggesting renames, but does not explicitly establish every old/new precinct boundary. Powell’s 2023 resolution addresses legislative districts and does not verify the old precinct-number suffixes. Remaining Beaverhead identifiers, Carbon’s Ward label discrepancy, Petroleum’s spelling difference and Lincoln’s added Rexford record also need documentation. Do not silently pair them.



See ../sources/geographic-investigation.md for linked official evidence. For publication, cross-election precinct claims require geographic review of their actual sample. The current verified sample is narrow and cannot support a statewide conclusion.



## Claim exceptions



FAIL: none.

SOURCE_INCOMPLETE: none.

NOT_COMPARABLE: none.

NEEDS_GEOGRAPHIC_REVIEW: SENATE-TESTER-TO-BODNAR, SENATE-TESTER-TO-ALME, SENATE-TESTER-TO-BANKHEAD, SENATE-TESTER-BANKHEAD-TRAILS-ALME, SENATE-TESTER-BANKHEAD-TRAILS-BODNAR, SENATE-TESTER-BODNAR-BEATS-ALME, SENATE-TESTER-BANKHEAD-BELOW-20PCT, SENATE-TESTER-BANKHEAD-BELOW-30PCT, SENATE-TESTER-BANKHEAD-BELOW-40PCT, SENATE-TESTER-COMBINED-EXCEEDS-TESTER-SHARE, SENATE-TESTER-REPUBLICAN-SHARE-INCREASED, SENATE-TESTER-REPUBLICAN-SHARE-DECREASED, SENATE-TESTER-MATCHED.
