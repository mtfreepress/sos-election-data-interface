"""Reporter-facing findings; every numerical statement references registry IDs."""
try:
    from .core import display
except ImportError:
    from core import display


def reporting_findings(results,tables,audit):
    claims={r['id']:r for r in results}
    def n(id,digits=1):
        r=claims[id]
        return f"{display(r['calculated_value'],digits)} [{id}]"
    lines=['# Reporting findings: 2024 versus 2026', '',
           'All findings describe the retained SOS snapshots. The 2026 capture is Nov. 20, 2026, unofficial, excludes write-ins, and reports 727/728 precincts with one partial. The 2024 retained exports also say unofficial; write-in coverage is unestablished. Export coverage is not certification or completed counting.',
           f"Source commit: `{audit['source_commit_sha']}`. See source-reconciliation.json for hashes, original headers, dates and each comparison. No fresh election results are downloaded by this tool.",'',
           '## A. MT-01','',
           f"Republican share fell from {n('MT01-R-SHARE-2024',2)}% to {n('MT01-R-SHARE-2026',2)}%. Democratic share went from {n('MT01-D-SHARE-2024',2)}% to {n('MT01-D-SHARE-2026',2)}%. The Republican-minus-Democratic margin changed by {n('MT01-MARGIN-CHANGE',2)} percentage points (negative means toward Democrats).",
           f"Republican share declined in {n('MT01-COUNTIES-DECLINED',0)} county portions and increased in {n('MT01-COUNTIES-INCREASED',0)}. Gallatin and Missoula rank {n('MT01-GALLATIN-REDUCTION-RANK',0)} and {n('MT01-MISSOULA-REDUCTION-RANK',0)} for the largest reductions.", '']
    for county in ['GALLATIN','MISSOULA','SILVER-BOW','MADISON','FLATHEAD','RAVALLI','PONDERA']:
        lines.append(f"- {county.title().replace('-',' ')}: {n('MT01-'+county+'-R-SHARE-CHANGE',2)} pp in Republican all-candidate share.")
    ranked=tables['mt01-verified-rankings-min-100']
    minimum=ranked.republican_share_change_pp.min()
    leaders=ranked[ranked.republican_share_change_pp.eq(minimum)]
    leading_names='; '.join(leaders.county.str.title()+' / '+leaders.precinct_2024) if len(leaders) else 'No rankable precinct'
    lines += ['', f"In the documented MT-01 sample, {leading_names} had the largest Republican-share reduction among precincts with at least 100 votes in both years: {n('MT01-VERIFIED-LARGEST-R-SHARE-DECREASE-MIN-100',2)} pp. The verified sample contained {n('MT01-VERIFIED-R-TO-D-FLIPS',0)} Republican-to-Democratic plurality flips and {n('MT01-VERIFIED-D-TO-R-FLIPS',0)} in the other direction. These describe only the documented sample."]
    lines += ['',f"Pondera’s western House portion has {n('MT01-PONDERA-PRECINCTS-2026',0)} precinct records and {n('MT01-PONDERA-VOTES-2026',0)} contest votes in 2026. Its eastern portion has {n('MT02-PONDERA-PRECINCTS-2026',0)} records. Valier Rural appears in both House contests; these are district portions, not duplicate votes. Countywide Senate votes cannot be assigned to the western portion.",
              f"Geographically checked MT-01 comparisons cover {n('MT01-COVERAGE-VERIFIED-MATCHED-PRECINCTS',0)} precincts. The larger name-matched sample covers {n('MT01-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS',0)} and remains provisional. The verified ranking files apply no minimum, a minimum of 100 votes in both years, and a minimum of 300 in both years; these are limited samples, not districtwide precinct rankings.", '',
              '## B. Senate candidate patterns', '',
              f"2024 plurality wins: Sheehy {n('SENATE-SHEEHY-WINS-2024',0)}, Tester {n('SENATE-TESTER-WINS-2024',0)}. 2026: Alme {n('SENATE-ALME-WINS-2026',0)}, Bodnar {n('SENATE-BODNAR-WINS-2026',0)}, Bankhead {n('SENATE-BANKHEAD-WINS-2026',0)}. Ties and zero votes are separate rows in winner-summary.csv.",
              f"Bodnar outpolled Bankhead in {n('SENATE-BODNAR-VS-BANKHEAD-BODNAR',0)} precincts. Among Bodnar’s precinct wins, Bankhead trailed Alme in {n('SENATE-BODNAR-WINS-BANKHEAD-TRAILS-ALME',0)}. Bodnar accounted for {n('SENATE-BODNAR-SHARE-NONREPUBLICAN-WINS',1)}% of non-Republican plurality wins.", '',
              'Bankhead’s precinct wins by county:', '']
    for county in ['BIG-HORN','BLAINE','ROOSEVELT','CASCADE','HILL']:
        lines.append(f"- {county.title().replace('-',' ')}: {n('SENATE-BANKHEAD-WINS-'+county,0)}.")
    lines += ['', 'Highest Bodnar county vote shares (all precincts, vote-weighted):', '']
    for county in tables['senate-county-summary'].sort_values('share__SETH BODNAR_2026',ascending=False).head(6).county:
        lines.append(f"- {county.title()}: {n('SENATE-'+county.replace(' ','-')+'-SETH-BODNAR-2026',2)}%.")
    lines += ['', 'The full precinct list, candidate counts, totals, winner shares and margins are in senate-bankhead-wins.csv. County shares include every precinct, including those she did not win. High county shares describe geographic concentration and do not establish voters’ race, ethnicity or ideology.', '',
              'Highest Bankhead county vote shares (all precincts, vote-weighted):', '']
    senate=tables['senate-county-summary']
    for county in senate.sort_values('share__ALANI BANKHEAD_2026',ascending=False).head(6).county:
        slug=county.replace(' ','-')
        lines.append(f"- {county.title()}: Bankhead {n('SENATE-'+slug+'-ALANI-BANKHEAD-2026',2)}%; Bodnar {n('SENATE-'+slug+'-SETH-BODNAR-2026',2)}%.")
    lines += ['',f"In the provisional matched sample, {n('SENATE-TESTER-MATCHED',0)} Tester-winning precincts split as follows: Bodnar {n('SENATE-TESTER-TO-BODNAR',0)}, Alme {n('SENATE-TESTER-TO-ALME',0)}, Bankhead {n('SENATE-TESTER-TO-BANKHEAD',0)}. Bankhead trailed Alme in {n('SENATE-TESTER-BANKHEAD-TRAILS-ALME',0)} of these precincts. That last comparison does not mean Alme won all of them; Bodnar could win while Alme finished ahead of Bankhead.",
              f"The independently checked sample includes {n('SENATE-TESTER-MATCHED-VERIFIED',0)} Tester precincts: {n('SENATE-TESTER-TO-BODNAR-VERIFIED',0)} Bodnar, {n('SENATE-TESTER-TO-ALME-VERIFIED',0)} Alme, {n('SENATE-TESTER-TO-BANKHEAD-VERIFIED',0)} Bankhead. These are sample counts, not estimates for excluded precincts.",
              f"The name-matched Senate sample contains {n('SENATE-COVERAGE-PROVISIONAL-MATCHED-PRECINCTS',0)} precincts, excluding {n('SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2024',0)} from 2024 and {n('SENATE-COVERAGE-PROVISIONAL-EXCLUDED-PRECINCTS-2026',0)} from 2026. Excluded vote shares: {n('SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2024',2)}% and {n('SENATE-COVERAGE-PROVISIONAL-EXCLUDED-VOTE-SHARE-2026',2)}%, respectively. Unpaired and changed-boundary precincts remain in the audit.",
              f"Republican Senate share declined in {n('SENATE-COUNTIES-DECLINED',0)} counties and increased in {n('SENATE-COUNTIES-INCREASED',0)}. The increases were:", '']
    for county in senate[senate.republican_share_change_pp.gt(0)].sort_values('republican_share_change_pp',ascending=False).county:
        lines.append(f"- {county.title()}: {n('SENATE-'+county.replace(' ','-')+'-R-SHARE-CHANGE',2)} pp.")
    lines += ['', 'Counties of particular interest:', '']
    for county in ['GALLATIN','MISSOULA','BLAINE','BIG HORN','GLACIER','ROOSEVELT']:
        slug=county.replace(' ','-')
        lines.append(f"- {county.title()}: Republican share change {n('SENATE-'+slug+'-R-SHARE-CHANGE',2)} pp; Bodnar {n('SENATE-'+slug+'-SETH-BODNAR-2026',2)}%, Bankhead {n('SENATE-'+slug+'-ALANI-BANKHEAD-2026',2)}% in 2026.")
    lines += ['', '## C. MT-02','',
              f"Republican all-candidate share was {n('MT02-R-SHARE-2024',2)}% in 2024 and {n('MT02-R-SHARE-2026',2)}% in 2026. The 2026 Republican two-party share was {n('MT02-R-TWO-PARTY-2026',2)}%. Eisenhauer received {n('MT02-I-VOTES-2026',0)} votes, {n('MT02-I-SHARE-2026',2)}% of the total. Independent votes remain separate from Democratic votes.",
              f"All-candidate Republican share decreased in {n('MT02-COUNTIES-DECLINED',0)} county portions and increased in {n('MT02-COUNTIES-INCREASED',0)}. Under the two-party measure it decreased in {n('MT02-COUNTIES-DECLINED-TWO-PARTY',0)} and increased in {n('MT02-COUNTIES-INCREASED-TWO-PARTY',0)}. Compare both rankings before describing the scale of a swing.", '',
              '## D. Other reporting leads', '',
              f"1. Alme won {n('SENATE-R-PLURALITY-BELOW-50-2026',0)} precincts with strictly less than half the vote. Plurality wins and majorities describe different maps.",
              f"2. Bankhead won majorities in {n('SENATE-BANKHEAD-MAJORITIES-2026',0)} precincts; Bodnar did so in {n('SENATE-BODNAR-MAJORITIES-2026',0)}. Compare these with plurality wins before writing about strongholds.",
              f"3. Bodnar and Bankhead combined exceeded Alme in {n('SENATE-COMBINED-EXCEEDS-ALME',0)} precincts. This describes observed totals; it cannot establish the result of a hypothetical two-person election.",
              f"4. Bankhead’s share was below 20% in {n('SENATE-TESTER-BANKHEAD-BELOW-20PCT',0)} provisional Tester precincts. The geographically reviewed counterpart is {n('SENATE-TESTER-BANKHEAD-BELOW-20PCT-VERIFIED',0)}. Explore differences within the samples rather than generalizing to all Tester precincts.",
              f"5. The combined Bodnar–Bankhead share exceeded Tester’s former share in {n('SENATE-TESTER-COMBINED-EXCEEDS-TESTER-SHARE',0)} name-matched Tester precincts. This remains provisional and does not show that the same people changed preferences.",
              f"6. Republican two-party share in MT-02 changed by {n('MT02-TWO-PARTY-CHANGE',2)} pp, while all-candidate share changed by {n('MT02-R-SHARE-CHANGE',2)} pp. The independent vote is central to describing that difference.",
              f"7. The MT-01 Republican two-party change was {n('MT01-TWO-PARTY-CHANGE',2)} pp. Compare it with the all-candidate share change of {n('MT01-R-SHARE-CHANGE',2)} pp when assessing third-party denominator effects.", '',
              '## Geographic review still needed', '',
              'Lake’s county map explicitly covers 2024–2032; the verified subset uses its precinct identifiers and the 2026 judge-training legislative assignments. Beaverhead precinct 12 is supported by an explicit continuity statement in Resolution 2026-04. The five affected Dillon-area precincts are excluded. Verification methods and limitations are recorded per row; no statewide polygon overlay was performed.',
              'Missoula’s April 2026 announcement documents polling-place relocations from Lowell and C.S. Porter, suggesting renames, but does not explicitly establish every old/new precinct boundary. Powell’s 2023 resolution addresses legislative districts and does not verify the old precinct-number suffixes. Remaining Beaverhead identifiers, Carbon’s Ward label discrepancy, Petroleum’s spelling difference and Lincoln’s added Rexford record also need documentation. Do not silently pair them.', '',
              'See ../sources/geographic-investigation.md for linked official evidence. For publication, cross-election precinct claims require geographic review of their actual sample. The current verified sample is narrow and cannot support a statewide conclusion.', '',
              '## Claim exceptions', '']
    for status in ['FAIL','SOURCE_INCOMPLETE','NOT_COMPARABLE','NEEDS_GEOGRAPHIC_REVIEW']:
        ids=[r['id'] for r in results if r['verification_status']==status]
        lines.append(status+': '+(', '.join(ids) if ids else 'none')+'.')
    return '\n\n'.join(lines)+'\n'
