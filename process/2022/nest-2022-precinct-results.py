# Reshape flat csv of precinct-level results to nested JSON 
# that's easier to use in interactive data visualizations

import pandas as pd
import json

races = {
    'UNITED STATES REPRESENTAT 0745': 'us-house-west',
    'UNITED STATES REPRESENTAT 0746': 'us-house-east',
    'SUPREME COURT JUSTICE #1 0849': 'supco-1',
    'SUPREME COURT JUSTICE #2 0850': 'supco-2',
    'CONSTITUTIONAL AMENDMENT  2127': 'ci-48',
    'LEGISLATIVE REFERENDUM NO 2128': 'lr-131',
}

flat = pd.read_csv('./cleaned/2022/general/precinct-results.csv')

def reshape_to_json(df):
    precincts = df['key'].unique()
    race_keys = list(races.values())

    output = []
    for precinct in precincts:
        df_precincts = df[df['key'] == precinct]
        first_row = df_precincts.iloc[0]

        race_results = []
        for race in race_keys:            
            df_precinct_race_results = df_precincts[df_precincts['race'] == race].copy()
            df_precinct_race_results.sort_values('votes', ascending=False, inplace=True)

            total_votes = df_precinct_race_results['votes'].sum()
            if (total_votes == 0): continue
            
            df_precinct_race_results = df_precinct_race_results.assign(votePercent=lambda n: round(n.votes / total_votes, 5))
            
            winner = df_precinct_race_results.iloc[0]

            if (len(df_precinct_race_results) > 1):
                runner_up = df_precinct_race_results.iloc[1]
                winner_margin = winner['votes'] - runner_up['votes']
                winner_percent_margin = round(winner_margin / total_votes, 5)
            else:
                winner_margin = winner['votes']
                winner_percent_margin = winner['votes'] / total_votes
            df_precinct_race_results['votes'] = df_precinct_race_results['votes'].astype('int')
            candidates = df_precinct_race_results[['candidate','party','votes','votePercent']].to_dict(orient='records')

            race_results.append({
                'race': race,
                'totalVotes': int(total_votes),
                'winnerParty': winner['party'] if (winner_margin > 0) else 'tie',
                'winnerName': winner['candidate'] if (winner_margin > 0) else 'tie',
                'winnerVotes': int(winner['votes']),
                'winnerMargin': int(winner_margin),
                'winnerPercent': round(winner['votes'] / total_votes, 5),
                'winnerPercentMargin': winner_percent_margin,
                'candidates': candidates,
            })

        output.append({
            'key': precinct,
            'county': first_row['county'],
            'precinct': first_row['precinct'],
            'races': race_results,
        })

    return output

reshaped = reshape_to_json(flat)

with open('./outputs/2022/general/nested-precinct-results-2022.json', 'w') as f:
    json.dump(reshaped, f, indent=4)