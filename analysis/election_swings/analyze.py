"""Reproducible snapshot analysis. Run directly or through verify_claims.py."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

import pandas as pd

try:
    from .core import (RACES, aggregate, precinct_table, crosswalk, compare_precincts,
                       threshold_filter, transition_matrix, load_precincts, display)
except ImportError:
    from core import (RACES, aggregate, precinct_table, crosswalk, compare_precincts,
                      threshold_filter, transition_matrix, load_precincts, display)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUT = HERE / 'output'
RACE_NAMES = {'U.S. Senate':'us-senate','U.S. House 1':'us-house-west','U.S. House 2':'us-house-east'}


def serial(value):
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, 'item'):
        return value.item()
    raise TypeError(type(value).__name__)


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, default=serial, allow_nan=False)+'\n')


def candidate_comparisons(frame):
    f = frame[frame.year.eq(2026)&frame.race.eq('us-senate')].copy()
    names = {'bodnar':'SETH BODNAR','bankhead':'ALANI BANKHEAD','alme':'KURT ALME','austin':'KYLE AUSTIN'}
    for short, name in names.items():
        f[short+'_votes'] = f['votes__'+name]
        f[short+'_share'] = f['share__'+name]
    for x,y in [('bodnar','bankhead'),('bankhead','alme'),('bodnar','alme')]:
        f[x+'_vs_'+y] = 'missing_results'
        valid = f.status.isin(['candidate_winner','tie','no_votes'])
        f.loc[valid,x+'_vs_'+y] = 'tie'
        f.loc[valid & f[x+'_votes'].gt(f[y+'_votes']),x+'_vs_'+y] = x
        f.loc[valid & f[x+'_votes'].lt(f[y+'_votes']),x+'_vs_'+y] = y
        f.loc[f.status.eq('no_votes'),x+'_vs_'+y] = 'no_votes'
        f[x+'_minus_'+y+'_pp'] = (f[x+'_share']-f[y+'_share'])*100
    f['bodnar_bankhead_votes'] = f.bodnar_votes+f.bankhead_votes
    f['bodnar_bankhead_share'] = f.bodnar_share+f.bankhead_share
    f['combined_exceeds_alme'] = f.bodnar_bankhead_votes > f.alme_votes
    f['bodnar_won']=f.winning_candidate.eq('SETH BODNAR').astype(int)
    f['non_republican_won']=(f.status.eq('candidate_winner') & f.winning_party.ne('Republican')).astype(int)
    return f


def winner_summary(precincts, raw):
    records = []
    for (year,race),group in precincts.groupby(['year','race']):
        scopes = [('contest','ALL',group)] + [('county',c,g) for c,g in group.groupby('county')]
        if race=='us-senate':
            for district,g in group.groupby('district_scope'):
                scopes.append(('congressional_district',district,g))
        candidates = raw[raw.year.eq(year)&raw.race.eq(race)][['candidate','party']].drop_duplicates()
        for scope, name, g in scopes:
            for c in candidates.to_dict('records'):
                records.append(dict(year=int(year),race=race,scope=scope,geography=name,
                    kind='candidate',name=c['candidate'],party=c['party'],
                    precinct_count=len(g),wins=int(g.winning_candidate.eq(c['candidate']).sum()),
                    majority_precincts=int(g.majority_candidate.eq(c['candidate']).sum()),
                    republican_plurality_below_50=int((g.republican_plurality_below_50 & g.winning_candidate.eq(c['candidate'])).sum())))
            for party,gp in candidates.groupby('party'):
                records.append(dict(year=int(year),race=race,scope=scope,geography=name,kind='party',name=party,party=party,
                    precinct_count=len(g),wins=int(g.winning_party.eq(party).sum()),
                    majority_precincts=int(g.majority_candidate.isin(gp.candidate).sum())))
            records.append(dict(year=int(year),race=race,scope=scope,geography=name,kind='republican_category',name='non-Republican',party='',
                precinct_count=len(g),wins=int((g.status.eq('candidate_winner')&~g.winning_party.eq('Republican')).sum())))
            for status in ['tie','no_votes','missing_results','invalid_data']:
                records.append(dict(year=int(year),race=race,scope=scope,geography=name,kind='status',name=status,party='',
                    precinct_count=len(g),wins=int(g.status.eq(status).sum())))
            assert int(g.status.value_counts().sum()) == len(g)
    return pd.DataFrame(records)


def reconcile(raw, root):
    checks = []
    def compare(expected, keys, source, year):
        actual = raw[raw.year.eq(year)].groupby(keys).votes.sum().rename('calculated')
        expected = expected[expected.race.isin(RACES)].groupby(keys).votes.sum().rename('expected')
        joined = actual.to_frame().join(expected,how='outer')
        for k,row in joined.iterrows():
            checks.append(dict(year=year,source=source,identifiers=dict(zip(keys,k if isinstance(k,tuple) else (k,))),
                calculated=None if pd.isna(row.calculated) else int(row.calculated),expected=None if pd.isna(row.expected) else int(row.expected),
                status='PASS' if row.calculated==row.expected else 'FAIL'))
    for year in [2024,2026]:
        path = root/f'outputs/{year}/general/{year}-general-statewide-vote-counts.csv'
        totals = pd.read_csv(path)
        totals['race'] = totals.race.replace(RACE_NAMES)
        compare(totals,['race','party','candidate'],str(path.relative_to(root)),year)
    path = root/'cleaned/2026/general/county-results.csv'
    compare(pd.read_csv(path),['race','county','party','candidate'],str(path.relative_to(root)),2026)
    # Independent reconstruction from 2024 statewide workbook (county rows).
    path = root/'sos-data/2024/general/2024-12-11-statewide-results.xlsx'
    workbook = pd.ExcelFile(path)
    records = []
    sheets = {'01602UNITED STATES SENATOR':'us-senate','01603UNITED STATES REPRESENTAT':'us-house-west','01604UNITED STATES REPRESENTAT':'us-house-east'}
    for sheet,race in sheets.items():
        f = pd.read_excel(workbook,sheet_name=sheet,skiprows=6).iloc[:,1:]
        geo = f.columns[0]
        for column in f.columns[1:]:
            candidate,party = column.split('\n')[:2]
            for row in f[[geo,column]].itertuples(index=False,name=None):
                county,votes = row
                county = county.strip().upper().replace('LEWIS & CLARK','LEWIS AND CLARK') if isinstance(county,str) else county
                if pd.isna(county) or county=='TOTALS' or pd.isna(votes):
                    continue
                if float(votes)<0 or int(votes)!=float(votes):
                    raise ValueError('Invalid workbook vote count')
                # Statewide House sheets include zero rows outside the district.
                if county not in set(raw[raw.year.eq(2024)&raw.race.eq(race)].county) and votes==0:
                    continue
                records.append(dict(race=race,county=county,party=party,candidate=candidate,votes=int(votes)))
    compare(pd.DataFrame(records),['race','county','party','candidate'],str(path.relative_to(root)),2024)
    return checks


def metadata(root, files, checks):
    v=json.loads((root/'cleaned/2026/general/validation.json').read_text())
    manifest=json.loads((root/v['snapshot']/'manifest.json').read_text())
    headers = [dict(file=s['file'],race=s['race'],county=s.get('county'),source_header=s['source_header'],
                    status=s['status'],precincts_reporting=s['precincts_reporting'],precincts_total=s['precincts_total'])
               for s in v['sheets'] if s['race'] in RACES]
    historical=[]
    for p in sorted((root/'sos-data/2024/general/precinct-results-by-county').glob('*.xlsx')):
        header = pd.read_excel(p,sheet_name=0,header=None,nrows=4).iloc[:,0].astype(str).tolist()
        historical.append({'file':str(p.relative_to(root)),'header':header})
    return dict(source_commit_sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),
        inputs=[dict(filename=str(p.relative_to(root)),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in files],
        elections={'2024':dict(year=2024,result_status='unofficial (retained workbook headers)',processing_date='not recorded by historical script',
            snapshot_dates='2024-12-11 statewide workbook; county download headers retained below',county_headers=historical,
            reported_completeness='727 of 727 reporting; 0 partially reported in retained headers',write_ins='coverage not independently established'),
            '2026':dict(year=2026,result_status='unofficial',snapshot_date=manifest['downloaded_at'],processing_date=v['processed_at'],
                reported_completeness='727 of 728 reporting; 1 partially reported (source headers)',
                precinct_coverage_complete=v['precinct_coverage_complete'],write_ins=v['write_ins'],source_headers=headers)},
        limitations=['Coverage checks describe export availability, not completed counting or certification.',
                     '2026 live results exclude write-ins; 2024 write-in coverage is not established.',
                     'Exact and normalized names alone do not establish geographic continuity.',
                     'Split House precincts are contest portions; Senate votes cannot be apportioned to districts.',
                     'Counts and PASS claims verify the retained snapshot, not final certified election results.',
                     'Candidate totals reconcile against separate exports of the same SOS system, not an independent ballot count.'],
        geographic_aliases={'2024 statewide workbook': {'LEWIS & CLARK':'LEWIS AND CLARK'}, 'county case':'uppercased for comparison; source file preserved'},
        checks=checks,reconciliation_status='PASS' if all(c['status']=='PASS' for c in checks) else 'FAIL')


def build(root=ROOT, reviews_path=HERE/'geographic-reviews.json'):
    frames = [load_precincts(root/f'cleaned/{y}/general/precinct-results.csv',y) for y in [2024,2026]]
    raw = pd.concat(frames,ignore_index=True)
    raw['source_file'] = raw.source_file.map(lambda p:str(Path(p).relative_to(root)))
    precincts = precinct_table(raw)
    # Senate counts by district: preserve unsplittable Senate records in a split category.
    house = precincts[precincts.race.ne('us-senate')].groupby(['year','county','precinct']).race.agg(lambda s:' | '.join(sorted(s.unique()))).rename('district_scope')
    precincts = precincts.merge(house,on=['year','county','precinct'],how='left',validate='many_to_one')
    precincts['district_scope'] = precincts.district_scope.fillna('unknown')
    precincts.loc[precincts.district_scope.str.contains(' | ',regex=False),'district_scope'] = 'split_house_precinct_unallocated'
    district = aggregate(raw,['race','year'])
    district['two_party_votes']=district.republican_votes+district.democratic_votes
    district['republican_minus_democratic_votes']=district.republican_votes-district.democratic_votes
    county = aggregate(raw,['race','year','county'])
    # Preserve all candidate counts and shares in county and district tables.
    for frame,keys in [(county,['race','year','county']),(district,['race','year'])]:
        for (candidate,party),g in raw.groupby(['candidate','party']):
            counts = g.groupby(keys).votes.sum()
            frame['votes__'+candidate] = [counts.get(tuple(r),None) for r in frame[keys].values]
            frame['share__'+candidate] = frame['votes__'+candidate]/frame.total_votes
    swings = county[county.year.eq(2024)].drop(columns='year').merge(county[county.year.eq(2026)].drop(columns='year'),on=['race','county'],how='outer',suffixes=('_2024','_2026'),validate='one_to_one')
    for metric in ['republican_share','republican_margin','republican_two_party_share']:
        swings[metric+'_change_pp'] = (swings[metric+'_2026']-swings[metric+'_2024'])*100
    swings['all_candidate_rank'] = swings.groupby('race').republican_share_change_pp.rank(method='min')
    swings['two_party_rank'] = swings.groupby('race').republican_two_party_share_change_pp.rank(method='min')
    reviews=json.loads(reviews_path.read_text())['reviews']
    audits=[]; comparisons=[]; coverage=[]
    for race in RACES:
        a,b=[precincts[precincts.race.eq(race)&precincts.year.eq(y)].copy() for y in [2024,2026]]
        local=[r for r in reviews if r.get('race',race)==race and r['county'] in set(a.county)]
        walk=crosswalk(a,b,local)
        compared=compare_precincts(a,b,walk)
        walk['race']=race;compared['race']=race
        audits.append(walk);comparisons.append(compared)
        for sample,col in [('provisional','provisional_comparable'),('verified','geographically_verified')]:
            matched=compared[compared[col]]
            item=dict(race=race,sample=sample,matched_precincts=len(matched),
                      exact_name_matches=int((walk.name_matched & walk.precinct_2024.eq(walk.precinct_2026)).sum()),normalized_name_matches=int((walk.name_matched & walk.precinct_2024.ne(walk.precinct_2026)).sum()),
                      independently_verified=int(walk.geographically_verified.sum()),boundary_changed=int(walk.match_status.eq('boundary_changed').sum()))
            for y,f in [(2024,a),(2026,b)]:
                total=int(f.total_votes.sum());votes=int(matched[f'total_votes_{y}'].sum())
                item.update({f'precincts_{y}':len(f),f'excluded_precincts_{y}':len(f)-len(matched),f'matched_votes_{y}':votes,
                             f'total_votes_{y}':total,f'matched_vote_share_{y}':votes/total,
                             f'excluded_votes_{y}':total-votes,f'excluded_vote_share_{y}':(total-votes)/total,
                             f'unpaired_precincts_{y}':int((compared[f'precinct_{y}'].ne('') & compared[f'precinct_{2026 if y==2024 else 2024}'].eq('')).sum())})
            coverage.append(item)
    comparisons=pd.concat(comparisons,ignore_index=True)
    senate=comparisons[comparisons.race.eq('us-senate')].copy()
    tester=senate[senate.winning_candidate_2024.eq('JON TESTER')].copy()
    for name in ['JON TESTER','TIM SHEEHY']:
        tester[name.lower().replace(' ','_')+'_share_2024']=tester['share__'+name+'_2024']
    for short,name in [('bodnar','SETH BODNAR'),('bankhead','ALANI BANKHEAD'),('alme','KURT ALME')]:
        tester[short+'_share_2026']=tester['share__'+name+'_2026']
        tester[short+'_votes_2026']=tester['votes__'+name+'_2026']
    tester['combined_bodnar_bankhead_share_2026']=tester.bodnar_share_2026+tester.bankhead_share_2026
    tester['bankhead_minus_alme_pp']=(tester.bankhead_share_2026-tester.alme_share_2026)*100
    tester['bodnar_minus_alme_pp']=(tester.bodnar_share_2026-tester.alme_share_2026)*100
    for level in [20,30,40]:
        tester[f'bankhead_below_{level}pct']=tester.bankhead_share_2026.lt(level/100)&tester.total_votes_2026.gt(0)
    tester['bankhead_trails_alme']=tester.bankhead_votes_2026.lt(tester.alme_votes_2026)
    tester['bankhead_trails_bodnar']=tester.bankhead_votes_2026.lt(tester.bodnar_votes_2026)
    tester['bodnar_beats_alme']=tester.bodnar_votes_2026.gt(tester.alme_votes_2026)
    tester['combined_exceeds_tester_share']=tester.combined_bodnar_bankhead_share_2026.gt(tester.jon_tester_share_2024)
    for direction,sign in [('increased',1),('decreased',-1)]:
        tester['republican_share_'+direction]=tester.republican_share_change_pp.mul(sign).gt(0)
    candidate_compare=candidate_comparisons(precincts)
    comparison_counts=[]
    for relation in ['bodnar_vs_bankhead','bankhead_vs_alme','bodnar_vs_alme']:
        for (status,outcome),g in candidate_compare.groupby(['status',relation]):
            comparison_counts.append(dict(comparison=relation,result_status=status,outcome=outcome,precinct_count=len(g),total_precincts=len(candidate_compare)))
    summary=winner_summary(precincts,raw)
    swings['combined_bodnar_bankhead_share_2026']=swings['share__SETH BODNAR_2026']+swings['share__ALANI BANKHEAD_2026']
    # Add precinct winner counts and provisional/verified Tester transitions to county summaries.
    for (y,race,candidate),_ in raw.groupby(['year','race','candidate']):
        counts=precincts[precincts.year.eq(y)&precincts.race.eq(race)&precincts.winning_candidate.eq(candidate)].groupby('county').size()
        swings[f'wins__{candidate}_{y}']=swings.county.map(counts).fillna(0).where(swings.race.eq(race))
    for sample,col in [('provisional','provisional_comparable'),('verified','geographically_verified')]:
        for candidate in sorted(raw[raw.race.eq('us-senate')&raw.year.eq(2026)].candidate.unique()):
            counts=tester[tester[col]&tester.winning_candidate_2026.eq(candidate)].groupby('county').size()
            swings[f'tester_to__{candidate}_{sample}']=swings.county.map(counts).fillna(0).where(swings.race.eq('us-senate'))
    district_swings = district[district.year.eq(2024)].drop(columns='year').merge(district[district.year.eq(2026)].drop(columns='year'),on='race',suffixes=('_2024','_2026'),validate='one_to_one')
    for metric in ['republican_share','democratic_share','republican_margin','republican_two_party_share']:
        district_swings[metric+'_change_pp']=(district_swings[metric+'_2026']-district_swings[metric+'_2024'])*100
    tables={'senate-candidate-comparison-summary':pd.DataFrame(comparison_counts),'district-swings':district_swings,'source-records':raw,'district-summary':district,'county-results':county,'county-swings':swings,
            'precinct-results':precincts,'precinct-swings':comparisons,'winner-summary':summary,
            'precinct-crosswalk-audit':pd.concat(audits,ignore_index=True),'match-coverage':pd.DataFrame(coverage),
            'senate-precinct-winners-2024':precincts[precincts.race.eq('us-senate')&precincts.year.eq(2024)],
            'senate-precinct-winners-2026':precincts[precincts.race.eq('us-senate')&precincts.year.eq(2026)],
            'senate-winner-transitions':senate,
            'senate-transition-matrix':pd.concat([transition_matrix(senate,s) for s in ['provisional','verified','audit']],ignore_index=True),
            'senate-tester-precincts':tester,'senate-bodnar-bankhead-comparison':candidate_compare,
            'senate-bankhead-wins':candidate_compare[candidate_compare.winning_candidate.eq('ALANI BANKHEAD')],
            'senate-county-summary':swings[swings.race.eq('us-senate')],
            'mt01-county-summary':swings[swings.race.eq('us-house-west')],
            'mt02-county-summary':swings[swings.race.eq('us-house-east')],
            'mt01-precinct-swings':comparisons[comparisons.race.eq('us-house-west')]}
    for label,race in [('mt01','us-house-west'),('mt02','us-house-east'),('senate','us-senate')]:
        f=comparisons[comparisons.race.eq(race)]
        for threshold in [0,100,300]:
            ranked=threshold_filter(f,threshold)
            for metric in ['republican_share_change_pp','republican_margin_change_pp']:
                ranked['rank_decrease_'+metric]=ranked[metric].rank(method='min')
                ranked['rank_increase_'+metric]=ranked[metric].rank(ascending=False,method='min')
            tables[f'{label}-verified-rankings-min-{threshold}']=ranked.sort_values(['republican_share_change_pp','county','precinct_2024'])
    return {name:frame.reset_index(drop=True) for name,frame in tables.items()}


def run(output=OUTPUT, root=ROOT):
    tables=build(root)
    checks=reconcile(tables['source-records'],root)
    paths=[root/f'cleaned/{y}/general/precinct-results.csv' for y in [2024,2026]]
    paths += [root/'cleaned/2026/general/county-results.csv',root/'cleaned/2026/general/validation.json',
              root/'sos-data/2026/general/2026-11-20-live/manifest.json',root/'sos-data/2024/general/2024-12-11-statewide-results.xlsx']
    paths += [root/f'outputs/{y}/general/{y}-general-statewide-vote-counts.csv' for y in [2024,2026]]
    paths += [HERE/'geographic-reviews.json',HERE/'claims.json',HERE/'sources/geographic-investigation.md',HERE/'sources/lake-precincts-20260519.png']
    paths += sorted(HERE.glob('*.py'))
    output.mkdir(parents=True,exist_ok=True)
    for name,table in tables.items():
        table.to_csv(output/(name+'.csv'),index=False)
    audit=metadata(root,paths,checks)
    write_json(output/'source-reconciliation.json',audit)
    return tables,audit


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=OUTPUT)
    args=parser.parse_args()
    run(args.output)
    print(f'Analysis tables written to {args.output}. Run verify_claims.py to generate claim and findings reports.')
