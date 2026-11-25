"""Election arithmetic and conservative, one-to-one precinct matching.

Shares are fractions (0..1); changes and winning margins ending in _pp are
percentage points. No intermediate values are rounded. No network access.
"""
from decimal import Decimal, ROUND_HALF_UP
import re

import pandas as pd

RACES = ('us-senate', 'us-house-west', 'us-house-east')
VERIFIED = {'verified_rename', 'verified_geography'}
PROVISIONAL = {'exact_name_match', 'normalized_name_match'}
FIELDS = ['election', 'type', 'race', 'key', 'county', 'precinct', 'party', 'candidate', 'votes']


def load_precincts(path, year):
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    missing = set(FIELDS) - set(df)
    if missing:
        raise ValueError(f'Missing fields: {sorted(missing)}')
    if df.race.str.strip().eq('').any():
        raise ValueError('Missing race')
    df['source_file'] = str(path)
    df['source_row'] = df.index + 2
    df = df[df.race.isin(RACES)].copy()
    if df.empty:
        raise ValueError('No federal records')
    for col in FIELDS:
        if df[col].str.strip().eq('').any():
            raise ValueError(f'Missing {col}')
    if not df.election.eq(f'{year}-gen').all():
        raise ValueError('Wrong election year/type')
    if not df.votes.str.fullmatch(r'\d+').all():
        raise ValueError('Votes must be nonnegative integers')
    df['votes'] = df.votes.astype('int64')
    if df.duplicated(['election', 'race', 'county', 'precinct', 'candidate']).any():
        raise ValueError('Duplicate candidate/precinct records')
    if (df.groupby(['race', 'candidate']).party.nunique() != 1).any():
        raise ValueError('Inconsistent candidate party')
    if (df.groupby(['race', 'county', 'precinct']).key.nunique() != 1).any():
        raise ValueError('Inconsistent source key')
    if (df.groupby(['race', 'key']).apply(lambda g: len(g[['county','precinct']].drop_duplicates()), include_groups=False) != 1).any():
        raise ValueError('Ambiguous source key')
    df['year'] = year
    return df


def ratio(numerator, denominator):
    return numerator / denominator if denominator else None


def statistics(rows):
    total = int(rows.votes.sum())
    votes = rows.groupby('party').votes.sum().to_dict()
    r, d = int(votes.get('Republican', 0)), int(votes.get('Democrat', 0))
    result = {'total_votes': total, 'republican_votes': r, 'democratic_votes': d,
              'republican_share': ratio(r, total), 'democratic_share': ratio(d, total),
              'republican_margin': ratio(r-d, total), 'republican_two_party_share': ratio(r, r+d)}
    for party in ['Libertarian', 'Independent', 'Green']:
        v = int(votes.get(party, 0))
        result[party.lower()+'_votes'] = v
        result[party.lower()+'_share'] = ratio(v, total)
    return result


def aggregate(df, keys):
    records = []
    for key, group in df.groupby(keys, sort=True):
        if not isinstance(key, tuple):
            key = (key,)
        records.append(dict(zip(keys, key), **statistics(group)))
    return pd.DataFrame(records)


def winner(rows, expected_candidates=None):
    """Return an explicit exception before identifying a unique plurality winner."""
    base = dict(status='missing_results', winning_candidate='', winning_party='',
                winning_votes=None, winner_share=None, runner_up='', runner_up_votes=None,
                winning_margin_votes=None, winning_margin_pp=None, total_votes=None,
                tied_candidates='', majority_candidate='', republican_plurality_below_50=False)
    if rows.empty:
        return base
    values = pd.to_numeric(rows.votes, errors='coerce')
    if values.isna().any() or (values < 0).any() or (values % 1 != 0).any() or rows.candidate.duplicated().any():
        return dict(base, status='invalid_data')
    if expected_candidates is not None and set(rows.candidate) != set(expected_candidates):
        return base
    total = int(values.sum())
    base['total_votes'] = total
    if not total:
        return dict(base, status='no_votes')
    ordered = rows.assign(votes=values).sort_values(['votes','candidate'], ascending=[False,True])
    top = ordered.iloc[0]
    tied = ordered[ordered.votes == top.votes]
    if len(tied) > 1:
        return dict(base, status='tie', tied_candidates=' | '.join(tied.candidate))
    second = ordered.iloc[1] if len(ordered) > 1 else None
    second_votes = int(second.votes) if second is not None else 0
    return dict(base, status='candidate_winner', winning_candidate=top.candidate,
                winning_party=top.party, winning_votes=int(top.votes), winner_share=int(top.votes)/total,
                runner_up=second.candidate if second is not None else '', runner_up_votes=second_votes,
                winning_margin_votes=int(top.votes)-second_votes,
                winning_margin_pp=(int(top.votes)-second_votes)/total*100,
                majority_candidate=top.candidate if int(top.votes)*2 > total else '',
                republican_plurality_below_50=bool(top.party == 'Republican' and int(top.votes)*2 < total))


def precinct_table(df):
    records = []
    for (year, race), contest in df.groupby(['year','race']):
        candidates = set(contest.candidate)
        # House records define district portions; a split precinct can occur in both races.
        universe = df[df.year == year][['county','precinct','key']].drop_duplicates() if race == 'us-senate' else contest[['county','precinct','key']].drop_duplicates()
        groups = {(c,p): g for (c,p),g in contest.groupby(['county','precinct'])}
        for row in universe.to_dict('records'):
            group = groups.get((row['county'],row['precinct']), contest.iloc[:0])
            item = dict(row, year=int(year), race=race) | statistics(group) | winner(group,candidates)
            for candidate in sorted(candidates):
                selected = group[group.candidate == candidate]
                item['votes__'+candidate] = int(selected.votes.sum()) if not selected.empty else None
                item['share__'+candidate] = ratio(item['votes__'+candidate], item['total_votes']) if not selected.empty else None
            records.append(item)
    return pd.DataFrame(records).sort_values(['race','year','county','precinct']).reset_index(drop=True)


def normalize(name):
    return re.sub('[^A-Z0-9]', '', name.upper()).replace('PRECINCT','PREC')


def crosswalk(a, b, reviews=()):
    """Never use fuzzy matching. Identical names remain geographically provisional.

    Reviews name exact source IDs; stale reviews fail closed. Aggregations require
    separate common-geography inputs, and are intentionally not accepted here.
    """
    left = a[['county','precinct','key']].drop_duplicates().rename(columns={'precinct':'precinct_2024','key':'key_2024'})
    right = b[['county','precinct','key']].drop_duplicates().rename(columns={'precinct':'precinct_2026','key':'key_2026'})
    left['normalized'] = left.precinct_2024.map(normalize)
    right['normalized'] = right.precinct_2026.map(normalize)
    # Collisions are kept as individual, unpaired ambiguous records.
    bad = set(map(tuple,left[left.duplicated(['county','normalized'],False)][['county','normalized']].values)) | set(map(tuple,right[right.duplicated(['county','normalized'],False)][['county','normalized']].values))
    left['collision'] = [tuple(x) in bad for x in left[['county','normalized']].values]
    right['collision'] = [tuple(x) in bad for x in right[['county','normalized']].values]
    pairs = left[~left.collision].merge(right[~right.collision],on=['county','normalized'],how='outer',validate='one_to_one')
    records = []
    for row in pairs.fillna('').to_dict('records'):
        x,y = row['precinct_2024'],row['precinct_2026']
        records.append({k: row.get(k,'') for k in ['county','precinct_2024','key_2024','precinct_2026','key_2026']} | {'match_status': ('exact_name_match' if x==y else 'normalized_name_match') if x and y else 'unmatched', 'evidence':'', 'notes':''})
    for frame, year in [(left,2024),(right,2026)]:
        for row in frame[frame.collision].to_dict('records'):
            records.append({'county':row['county'],'precinct_2024':'','precinct_2026':'','key_2024':'','key_2026':'',f'precinct_{year}':row[f'precinct_{year}'],f'key_{year}':row[f'key_{year}'],'match_status':'ambiguous','evidence':'','notes':'Normalization collision'})
    result = pd.DataFrame(records)
    result['name_matched'] = result.match_status.isin(PROVISIONAL)
    for review in reviews:
        c,x,y = [review[k] for k in ['county','precinct_2024','precinct_2026']]
        li = result.index[(result.county==c)&(result.precinct_2024==x)] if x else []
        ri = result.index[(result.county==c)&(result.precinct_2026==y)] if y else []
        if len(li)!=1 or len(ri)!=1:
            raise ValueError(f'Stale/ambiguous geographic review: {review}')
        if review['match_status'] not in VERIFIED | {'boundary_changed','ambiguous'} or not review.get('evidence'):
            raise ValueError('Review requires supported status and evidence')
        i,j = li[0],ri[0]
        if i != j:
            if result.loc[i,'precinct_2026'] or result.loc[j,'precinct_2024']:
                raise ValueError('Review would overwrite a different pair')
            result.loc[i,['precinct_2026','key_2026']] = result.loc[j,['precinct_2026','key_2026']].values
            result = result.drop(j)
        for k in ['match_status','evidence','notes']:
            result.loc[i,k] = review.get(k,'')
    result['geographically_verified'] = result.match_status.isin(VERIFIED)
    result['provisional_comparable'] = result.name_matched & result.match_status.isin(VERIFIED | PROVISIONAL)
    result['exclusion_reason'] = result.apply(lambda r: '' if r.geographically_verified else ('Geographic continuity unverified' if r.provisional_comparable else r.match_status),axis=1)
    for year in (2024,2026):
        ids = result[result[f'precinct_{year}']!=''][['county',f'precinct_{year}']]
        if ids.duplicated().any() or len(ids) != len(a if year==2024 else b):
            raise ValueError('Crosswalk must represent every precinct exactly once')
    return result.sort_values(['county','precinct_2024','precinct_2026']).reset_index(drop=True)


def compare_precincts(a, b, walk):
    result = walk.copy()
    for year, df in [(2024,a),(2026,b)]:
        renamed = df.drop(columns=['year','race','key']).rename(
            columns={c:f'{c}_{year}' for c in df if c not in ['county','year','race','key']})
        result = result.merge(renamed, on=['county',f'precinct_{year}'],
                              how='left',validate='many_to_one')
    for metric in ['republican_share','democratic_share','republican_margin','republican_two_party_share']:
        result[metric+'_change_pp'] = (result[metric+'_2026']-result[metric+'_2024'])*100
    result['flip'] = ''
    valid = result.provisional_comparable & result.status_2024.eq('candidate_winner') & result.status_2026.eq('candidate_winner')
    for old,new,label in [('Republican','Democrat','Republican_to_Democrat'),('Democrat','Republican','Democrat_to_Republican')]:
        result.loc[valid & result.winning_party_2024.eq(old) & result.winning_party_2026.eq(new),'flip'] = label
    return result


def threshold_filter(frame, threshold=0, verified=True):
    return frame[(frame.geographically_verified if verified else frame.provisional_comparable) & frame.total_votes_2024.ge(threshold) & frame.total_votes_2026.ge(threshold) & frame.total_votes_2024.gt(0) & frame.total_votes_2026.gt(0) & frame.status_2024.isin(['candidate_winner','tie']) & frame.status_2026.isin(['candidate_winner','tie'])].copy()


def transition_matrix(frame, sample):
    subset = frame[frame.geographically_verified if sample=='verified' else frame.provisional_comparable] if sample != 'audit' else frame
    out = subset.copy()
    for year in (2024,2026):
        out[f'winner_{year}'] = out[f'winning_candidate_{year}'].fillna('')
        nonwinner = ~out[f'status_{year}'].eq('candidate_winner')
        out.loc[nonwinner,f'winner_{year}'] = out.loc[nonwinner,f'status_{year}'].fillna('unmatched')
    matrix = out.groupby(['winner_2024','winner_2026'],dropna=False).size().reset_index(name='precinct_count')
    matrix['sample'] = sample
    if int(matrix.precinct_count.sum()) != len(subset):
        raise ValueError('Transition denominator mismatch')
    return matrix


def display(value, digits=1):
    if value is None or pd.isna(value):
        return 'NA'
    return str(Decimal(str(value)).quantize(Decimal(1).scaleb(-digits), rounding=ROUND_HALF_UP))
