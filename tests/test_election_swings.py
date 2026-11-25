"""Run with python -m unittest discover -s tests -v. No network calls."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import pandas as pd

from analysis.election_swings import core
from analysis.election_swings.analyze import ROOT, HERE, build, reconcile
from analysis.election_swings.claim_engine import evaluate, expected_matches, load_registry, select

FIXTURES=ROOT/'tests/fixtures/election_swings'


def rows(votes=(40,35,25), parties=('Republican','Democrat','Independent')):
    return pd.DataFrame([dict(candidate=f'C{i}',party=p,votes=v) for i,(p,v) in enumerate(zip(parties,votes))])


def places(names):
    return pd.DataFrame([dict(county='COUNTY',precinct=n,key='COUNTY-'+n) for n in names])


class ParsingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)/'input.csv'
        self.frame=pd.read_csv(FIXTURES/'2024-precinct-results.csv',dtype=str)

    def parse(self):
        self.frame.to_csv(self.path,index=False)
        return core.load_precincts(self.path,2024)

    def test_both_source_schemas_and_row_references(self):
        for y in [2024,2026]:
            f=core.load_precincts(FIXTURES/f'{y}-precinct-results.csv',y)
            self.assertTrue(f.year.eq(y).all());self.assertTrue(f.source_row.ge(2).all())
            self.assertTrue(pd.api.types.is_integer_dtype(f.votes))

    def test_missing_column_rejected(self):
        self.frame=self.frame.drop(columns='party')
        with self.assertRaisesRegex(ValueError,'Missing fields'):self.parse()

    def test_missing_identifiers_rejected(self):
        for column in ['county','precinct','candidate','votes','key','race']:
            with self.subTest(column=column):
                original=self.frame.copy();self.frame.loc[0,column]=''
                with self.assertRaises(ValueError):self.parse()
                self.frame=original

    def test_duplicate_candidate_rejected(self):
        self.frame=pd.concat([self.frame,self.frame.iloc[:1]])
        with self.assertRaisesRegex(ValueError,'Duplicate'):self.parse()

    def test_votes_must_be_nonnegative_whole_numbers(self):
        for value in ['-1','1.5','nan','inf','1e3']:
            with self.subTest(value=value):
                self.frame.loc[0,'votes']=value
                with self.assertRaisesRegex(ValueError,'nonnegative'):self.parse()

    def test_wrong_year_rejected(self):
        self.frame.loc[0,'election']='2026-gen'
        with self.assertRaisesRegex(ValueError,'Wrong election'):self.parse()

    def test_candidate_party_inconsistency_rejected(self):
        self.frame.loc[0,'party']='Other'
        with self.assertRaisesRegex(ValueError,'candidate party'):self.parse()

    def test_key_inconsistency_rejected(self):
        self.frame.loc[0,'key']='WRONG'
        with self.assertRaisesRegex(ValueError,'source key'):self.parse()


class ArithmeticTests(unittest.TestCase):
    def test_independent_denominator_and_margin(self):
        s=core.statistics(rows())
        self.assertEqual(s['total_votes'],100)
        self.assertEqual(s['republican_share'],0.4)
        self.assertEqual(s['democratic_share'],0.35)
        self.assertEqual(s['republican_margin'],0.05)
        self.assertAlmostEqual(s['republican_two_party_share'],40/75)
        self.assertEqual(s['independent_share'],0.25)

    def test_candidate_votes_aggregate_before_share(self):
        a=rows((4,3,3));b=rows((80,10,10));s=core.statistics(pd.concat([a,b]))
        self.assertEqual(s['republican_votes'],84)
        self.assertEqual(s['total_votes'],110)
        self.assertAlmostEqual(s['republican_share'],84/110)
        self.assertNotEqual(s['republican_share'],(0.4+0.8)/2)

    def test_county_and_contest_aggregations(self):
        f=pd.concat([rows().assign(county='A',race='west'),rows((1,2,7)).assign(county='B',race='west')])
        county=core.aggregate(f,['race','county']);district=core.aggregate(f,['race'])
        self.assertEqual(county.total_votes.sum(),district.total_votes.iloc[0])
        self.assertEqual(district.republican_votes.iloc[0],41)

    def test_zero_denominator_is_undefined(self):
        s=core.statistics(rows((0,0,0)))
        self.assertIsNone(s['republican_share']);self.assertIsNone(s['republican_two_party_share'])

    def test_plurality_is_not_majority(self):
        w=core.winner(rows())
        self.assertEqual(w['winning_candidate'],'C0');self.assertEqual(w['status'],'candidate_winner')
        self.assertEqual(w['majority_candidate'],'');self.assertTrue(w['republican_plurality_below_50'])
        self.assertEqual(w['runner_up'],'C1');self.assertEqual(w['runner_up_votes'],35)
        self.assertEqual(w['winning_margin_votes'],5);self.assertEqual(w['winning_margin_pp'],5)

    def test_majority_requires_strictly_more_than_half(self):
        self.assertEqual(core.winner(rows((50,30,20)))['majority_candidate'],'')
        self.assertFalse(core.winner(rows((50,30,20)))['republican_plurality_below_50'])
        self.assertEqual(core.winner(rows((51,29,20)))['majority_candidate'],'C0')

    def test_independent_can_win(self):
        w=core.winner(rows((30,25,45)))
        self.assertEqual(w['winning_party'],'Independent');self.assertEqual(w['winner_share'],0.45)

    def test_tie_is_explicit(self):
        w=core.winner(rows((40,40,20)))
        self.assertEqual(w['status'],'tie');self.assertEqual(w['tied_candidates'],'C0 | C1')
        self.assertEqual(w['winning_candidate'],'')

    def test_zero_votes_have_no_winner(self):
        w=core.winner(rows((0,0,0)))
        self.assertEqual(w['status'],'no_votes');self.assertEqual(w['winning_candidate'],'')
        self.assertIsNone(w['winner_share'])

    def test_empty_and_partial_candidate_results(self):
        self.assertEqual(core.winner(rows().iloc[:0])['status'],'missing_results')
        self.assertEqual(core.winner(rows().iloc[:2],{'C0','C1','C2'})['status'],'missing_results')

    def test_invalid_votes_or_duplicate_candidates(self):
        for f in [rows((-1,4,5)),rows((1.5,4,5)),rows((None,4,5)),pd.concat([rows(),rows().iloc[:1]])]:
            self.assertEqual(core.winner(f)['status'],'invalid_data')

    def test_rounding_is_decimal_half_up(self):
        self.assertEqual(core.display(1.005,2),'1.01')
        self.assertEqual(core.display(-1.005,2),'-1.01')
        self.assertEqual(core.display(64.29463609412544,2),'64.29')
        self.assertEqual(core.display(None,2),'NA')


class MatchingTests(unittest.TestCase):
    def test_exact_and_normalized_are_provisional(self):
        w=core.crosswalk(places(['PRECINCT #01','PCT2']),places(['PREC 01','PCT2']))
        self.assertEqual(set(w.match_status),{'exact_name_match','normalized_name_match'})
        self.assertTrue(w.provisional_comparable.all());self.assertFalse(w.geographically_verified.any())

    def test_county_is_part_of_key(self):
        a=places(['A']);b=places(['A']).assign(county='OTHER')
        w=core.crosswalk(a,b)
        self.assertEqual(len(w),2);self.assertFalse(w.provisional_comparable.any())

    def test_fuzzy_names_are_not_matched(self):
        w=core.crosswalk(places(['PRECINCT 1 - D CITY']),places(['PREC 1']))
        self.assertEqual(len(w),2);self.assertTrue(w.match_status.eq('unmatched').all())

    def test_normalization_collisions_stay_ambiguous(self):
        w=core.crosswalk(places(['P-1','P 1']),places(['P1']))
        self.assertEqual(len(w),3);self.assertTrue(w.match_status.eq('ambiguous').all())

    def test_review_requires_documentation_and_valid_identifiers(self):
        r=dict(county='COUNTY',precinct_2024='A',precinct_2026='B',match_status='verified_rename',evidence='county-resolution',notes='same territory')
        w=core.crosswalk(places(['A']),places(['B']),[r])
        self.assertEqual(len(w),1);self.assertTrue(w.geographically_verified.all())
        self.assertFalse(w.provisional_comparable.any()) # not part of original name sample
        with self.assertRaises(ValueError):core.crosswalk(places(['A']),places(['B']),[dict(r,evidence='')])
        with self.assertRaises(ValueError):core.crosswalk(places(['A']),places(['B']),[dict(r,precinct_2026='gone')])

    def test_boundary_changed_excluded_despite_identical_name(self):
        r=dict(county='COUNTY',precinct_2024='A',precinct_2026='A',match_status='boundary_changed',evidence='resolution')
        w=core.crosswalk(places(['A']),places(['A']),[r])
        self.assertFalse(w.provisional_comparable.any());self.assertFalse(w.geographically_verified.any())
        self.assertEqual(w.exclusion_reason.iloc[0],'boundary_changed')

    def test_verified_aggregation_not_misrepresented_as_single_precinct(self):
        r=dict(county='COUNTY',precinct_2024='A',precinct_2026='B',match_status='verified_aggregation',evidence='map')
        with self.assertRaises(ValueError):core.crosswalk(places(['A']),places(['B']),[r])

    def test_threshold_applies_to_both_years(self):
        f=pd.DataFrame(dict(geographically_verified=[True,True,True,False],provisional_comparable=[True]*4,total_votes_2024=[100,300,99,500],total_votes_2026=[100,299,400,500],status_2024=['candidate_winner']*4,status_2026=['candidate_winner']*4))
        self.assertEqual(len(core.threshold_filter(f,100)),2)
        self.assertEqual(len(core.threshold_filter(f,300)),0)
        self.assertEqual(len(core.threshold_filter(f,300,False)),1)


class ClaimTests(unittest.TestCase):
    def setUp(self):
        self.tables={'x':pd.DataFrame(dict(county=['A','B'],r=[40,60],d=[35,20],total=[100,100],geographically_verified=[True,False]))}
        self.base=dict(id='TEST',table='x',filters=[],operation='ratio',numerator_column='r',denominator_column='total',scale=100,source_files=['fixture.csv'],display_rounding=1,calculation='Fixture calculation')

    def test_ratio_aggregates_counts(self):
        r,e,_,_=evaluate(self.base,self.tables)
        self.assertEqual(r['calculated_value'],50);self.assertEqual(r['numerator'],100);self.assertEqual(r['denominator'],200)
        self.assertEqual(e['selected_csv_rows'],[2,3])

    def test_minimum_does_not_sum_tied_ranked_values(self):
        table=pd.DataFrame({'r':[-5,-5,2]})
        c=dict(self.base,operation='minimum',column='r',scale=1)
        self.assertEqual(evaluate(c,{'x':table})[0]['calculated_value'],-5)

    def test_expected_value_pass_and_fail(self):
        self.assertEqual(evaluate(dict(self.base,expected_value=50),self.tables)[0]['verification_status'],'PASS')
        self.assertEqual(evaluate(dict(self.base,expected_value=49),self.tables)[0]['verification_status'],'FAIL')

    def test_expected_rounding_and_tolerance(self):
        self.assertTrue(expected_matches(1.005,{'expected_value':1.01,'expected_rounding':2}))
        self.assertTrue(expected_matches(64.294636,{'expected_value':64.30,'absolute_tolerance':0.01}))
        self.assertFalse(expected_matches(64.28,{'expected_value':64.30,'absolute_tolerance':0.01}))

    def test_statuses_never_upgrade_provisional(self):
        self.assertEqual(evaluate(dict(self.base,sample='provisional',expected_value=50),self.tables)[0]['verification_status'],'NEEDS_GEOGRAPHIC_REVIEW')
        self.assertEqual(evaluate(self.base,self.tables,False)[0]['verification_status'],'SOURCE_INCOMPLETE')
        self.assertEqual(evaluate(dict(self.base,requires_final_results=True),self.tables)[0]['verification_status'],'SOURCE_INCOMPLETE')
        c=dict(self.base,operation='count',sample='verified',filters=[{'column':'county','value':'missing'}])
        self.assertEqual(evaluate(c,self.tables)[0]['verification_status'],'NOT_COMPARABLE')

    def test_filters_and_difference(self):
        c=dict(self.base,operation='difference',filters=[{'column':'county','value':'A'}],after_column='r',before_column='d',scale=1)
        self.assertEqual(evaluate(c,self.tables)[0]['calculated_value'],5)
        self.assertEqual(len(select(self.tables['x'],[{'column':'r','op':'gt','right_column':'d'}])),2)

    def test_omitted_sample_never_verifies_unreviewed_geography(self):
        table=self.tables['x'].assign(status_2024='candidate_winner',status_2026='candidate_winner')
        self.assertEqual(evaluate(self.base,{'x':table})[0]['verification_status'],'NEEDS_GEOGRAPHIC_REVIEW')
        with self.assertRaisesRegex(ValueError,'unverified selected'):
            evaluate(dict(self.base,sample='verified'),{'x':table})

    def test_registry_unique_and_all_required_metadata(self):
        registry=load_registry(HERE/'claims.json')
        self.assertEqual(len(registry),len({c['id'] for c in registry}))
        self.assertTrue(all(c['source_files'] and c['calculation'] for c in registry))


class VersionedFixtureTests(unittest.TestCase):
    def test_retained_source_record_winners(self):
        snapshot=json.loads((FIXTURES/'snapshot.json').read_text())
        for y in [2024,2026]:
            frame=core.load_precincts(FIXTURES/f'{y}-precinct-results.csv',y)
            for expected in snapshot['expected'][str(y)]:
                with self.subTest(year=y,precinct=expected['precinct']):
                    g=frame[frame.county.eq(expected['county'])&frame.precinct.eq(expected['precinct'])]
                    w=core.winner(g)
                    for key in ['status','winning_candidate','total_votes']:
                        self.assertEqual(w[key],expected[key])
                    if expected['winning_votes']!='':self.assertEqual(w['winning_votes'],expected['winning_votes'])


class CurrentSourceInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tables=build()
        cls.registry=load_registry(HERE/'claims.json')

    def test_every_precinct_counted_exactly_once_per_race(self):
        f=self.tables['precinct-results']
        self.assertFalse(f.duplicated(['year','race','county','precinct']).any())
        self.assertEqual(len(f),sum(self.tables['source-records'].groupby(['year','race']).apply(lambda g:len(g[['county','precinct']].drop_duplicates()),include_groups=False)))

    def test_winners_and_exceptions_reconcile(self):
        f=self.tables['winner-summary'].query('scope=="contest"')
        for _,g in f.groupby(['year','race']):
            total=g[g.kind.eq('candidate')].wins.sum()+g[g.kind.eq('status')].wins.sum()
            self.assertEqual(total,g.precinct_count.iloc[0])

    def test_transitions_and_denominators_reconcile(self):
        f=self.tables['senate-winner-transitions'];m=self.tables['senate-transition-matrix']
        for sample,column in [('provisional','provisional_comparable'),('verified','geographically_verified')]:
            self.assertEqual(m[m['sample'].eq(sample)].precinct_count.sum(),f[column].sum())
        self.assertEqual(m[m['sample'].eq('audit')].precinct_count.sum(),len(f))
        self.assertTrue(f.precinct_2024.eq('').any());self.assertTrue(f.precinct_2026.eq('').any())

    def test_crosswalk_coverage_and_vote_denominators(self):
        for r in self.tables['match-coverage'].to_dict('records'):
            for y in [2024,2026]:
                self.assertEqual(r[f'precincts_{y}'],r['matched_precincts']+r[f'excluded_precincts_{y}'])
                self.assertEqual(r[f'total_votes_{y}'],r[f'matched_votes_{y}']+r[f'excluded_votes_{y}'])
                self.assertAlmostEqual(r[f'matched_vote_share_{y}']+r[f'excluded_vote_share_{y}'],1)

    def test_counties_sum_to_contest_using_race_portions(self):
        county=self.tables['county-results'];district=self.tables['district-summary']
        for r in district.to_dict('records'):
            c=county[county.year.eq(r['year'])&county.race.eq(r['race'])]
            for col in ['total_votes','republican_votes','democratic_votes','independent_votes']:
                self.assertEqual(c[col].sum(),r[col])

    def test_statistics_independently_recalculate_from_python_counts(self):
        raw=self.tables['source-records']
        for name,keys in [('district-summary',['race','year']),('county-results',['race','year','county'])]:
            lookup={tuple(r[k] for k in keys):r for r in self.tables[name].to_dict('records')}
            for key,g in raw.groupby(keys):
                record=lookup[key]
                source=g.to_dict('records')
                total=sum(r['votes'] for r in source)
                republican=sum(r['votes'] for r in source if r['party']=='Republican')
                democratic=sum(r['votes'] for r in source if r['party']=='Democrat')
                self.assertEqual(record['total_votes'],total)
                self.assertAlmostEqual(record['republican_share'],republican/total)
                self.assertAlmostEqual(record['democratic_share'],democratic/total)
                self.assertAlmostEqual(record['republican_margin'],(republican-democratic)/total)
                self.assertAlmostEqual(record['republican_two_party_share'],republican/(republican+democratic))

    def test_plurality_counts_independent_of_winner_function(self):
        from collections import Counter
        raw=self.tables['source-records']
        expected={}
        for key,g in raw.groupby(['year','race','county','precinct']):
            votes={r['candidate']:r['votes'] for r in g.to_dict('records')}
            top=max(votes.values());tied=[name for name,v in votes.items() if v==top]
            expected[key]=('no_votes','') if not sum(votes.values()) else ('tie','') if len(tied)>1 else ('candidate_winner',tied[0])
        for r in self.tables['precinct-results'].to_dict('records'):
            self.assertEqual((r['status'],r['winning_candidate']),expected[(r['year'],r['race'],r['county'],r['precinct'])])

    def test_county_winner_columns_use_their_own_race(self):
        f=self.tables['precinct-results'];swings=self.tables['county-swings']
        for row in swings.to_dict('records'):
            for year in [2024,2026]:
                contest=f[f.race.eq(row['race'])&f.year.eq(year)&f.county.eq(row['county'])]
                for name in self.tables['source-records'].loc[lambda x:x.race.eq(row['race'])&x.year.eq(year),'candidate'].unique():
                    self.assertEqual(row[f'wins__{name}_{year}'],contest.winning_candidate.eq(name).sum())
            if row['race']!='us-senate':
                self.assertTrue(pd.isna(row['tester_to__SETH BODNAR_provisional']))

    def test_candidate_pair_comparisons_separate_zero_votes_and_reconcile(self):
        f=self.tables['senate-candidate-comparison-summary']
        for relation,g in f.groupby('comparison'):
            self.assertEqual(g.precinct_count.sum(),g.total_precincts.iloc[0])
            self.assertTrue(g[g.result_status.eq('no_votes')].outcome.eq('no_votes').all())

    def test_source_aggregate_reconciliation(self):
        checks=reconcile(self.tables['source-records'],ROOT)
        self.assertTrue(all(c['status']=='PASS' for c in checks),[c for c in checks if c['status']!='PASS'][:5])

    def test_every_registered_claim_calculates_and_has_valid_evidence(self):
        for c in self.registry:
            with self.subTest(claim=c['id']):
                r,e,selected,denominator=evaluate(c,self.tables)
                self.assertEqual(e['table'],c['table']+'.csv')
                self.assertTrue(all(2<=i<=len(self.tables[c['table']])+1 for i in e['selected_csv_rows']))
                if c.get('sample')=='provisional':self.assertEqual(r['verification_status'],'NEEDS_GEOGRAPHIC_REVIEW' if r['expected_matches'] is not False else 'FAIL')
                self.assertIsNotNone(r['calculated_value'])

    def test_changed_boundaries_never_enter_verified_rankings(self):
        for name,f in self.tables.items():
            if '-verified-rankings-' in name:
                self.assertTrue(f.geographically_verified.all())
                self.assertFalse(f.match_status.eq('boundary_changed').any())

    def test_snapshot_benchmarks_only_when_source_hashes_match(self):
        snapshot=json.loads((FIXTURES/'snapshot.json').read_text())
        for y,item in snapshot['files'].items():
            if hashlib.sha256((ROOT/item['source_file']).read_bytes()).hexdigest()!=item['source_sha256']:
                self.skipTest('Source snapshot updated; calculation invariants still run. Review old draft expectations separately.')
        expected={2024:{'TIM SHEEHY':497,'JON TESTER':228},2026:{'KURT ALME':532,'SETH BODNAR':180,'ALANI BANKHEAD':15}}
        for y,names in expected.items():
            f=self.tables[f'senate-precinct-winners-{y}']
            for name,count in names.items():self.assertEqual(f.winning_candidate.eq(name).sum(),count)
        for c in self.registry:
            if c.get('expected_value') is not None:
                self.assertIsNot(evaluate(c,self.tables)[0]['expected_matches'],False,c['id'])
