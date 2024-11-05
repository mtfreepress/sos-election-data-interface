# Parse one-page-per-district spreadsheet files

import pandas as pd
import re
import json

ELECTION_KEY = '2024-primary'
INPUT = '~/Downloads/Legislative Results-2024-primary.xlsx'
OUTPUT = './test.json'

# Tools for parsing one-tab-per-district tabulations
def parse_sheet(file, sheet_name, election):
    dfi = pd.read_excel(file, sheet_name, skiprows=6)
    district = re.search(r'(S|H)D\s[0-9]{1,3}', sheet_name).group(0)
    district = re.sub(r"0+(?=[1-9]+)",'', district)
    candidate_columns = dfi.columns[2:]
    candidates = []
    vote_row = dfi[dfi['County'] == 'TOTALS']
    # return vote_row[candidate_columns]
    ranked_by_vote = vote_row[candidate_columns].transpose()
    ranked_by_vote.columns = ['votes']
    ranked_by_vote['candidate'] = ranked_by_vote.index.map(lambda r: r.split('\n')[0])
    ranked_by_vote['party'] = ranked_by_vote.index.map(lambda r: r.split('\n')[1][0])
    ranked_by_vote = ranked_by_vote.sort_values('votes', ascending=False)
    winner_votes = ranked_by_vote.iloc[0].iloc[0]
    if (len(ranked_by_vote) > 1):
        runner_up_votes =  ranked_by_vote.iloc[1].iloc[0]
    else:
        runner_up_votes = 0
    
    total_votes = ranked_by_vote.sum().iloc[0]

    for col in candidate_columns:
        split = col.split('\n')
        candidate_votes = vote_row[col].iloc[0]
        isWinner = (candidate_votes == winner_votes)
        if (isWinner):
            vote_margin = candidate_votes - runner_up_votes
        else:
            vote_margin = candidate_votes - winner_votes
        candidates.append({
            # 'election': election,
            # 'district': district,
            'name': split[0].title(),
            'party': split[1][:1],
            'district': district,
            'winner': 'true' if isWinner else 'false',
            'votes': int(candidate_votes),
            'vote_fraction': candidate_votes / total_votes,
            'vote_margin': int(vote_margin),
            'percent_margin': vote_margin / total_votes,
        })
    return {
        'election': election,
        'district': district,
        'candidates': candidates,
        'winnerVotes': int(winner_votes),
        'totalVotes': int(total_votes),
        'winnerParty': ranked_by_vote['party'].iloc[0],
        'winnerName': ranked_by_vote['candidate'].iloc[0],
    }

def parse_file(file, election):
    xl = pd.ExcelFile(file)
    sheet_names = xl.sheet_names
    districts = []
    for sheet in sheet_names:
        data = parse_sheet(file, sheet, election)
        districts.append(data)
    return districts

results = parse_file(INPUT, ELECTION_KEY)

with open(OUTPUT, 'w') as f:
    json.dump(results, f, indent=4)