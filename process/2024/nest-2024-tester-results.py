# Reshape flat csv of precinct-level results to nested JSON
# that's easier to use in interactive data visualizations
import pandas as pd
import json

flat = pd.read_csv('../../cleaned/2024/general/precinct-results.csv')


def reshape_to_json(df):
    def standardize_precinct_name(val):
        return str(val).replace('&', 'and').replace('-', '_').replace(' ', '_').upper()
    
    precincts = df['key'].unique()

    
    output = []
    for precinct in precincts:
        df_precincts = df[df['key'] == precinct]
        first_row = df_precincts.iloc[0]

        precinct_key = standardize_precinct_name(precinct)

        df_us_senate = df_precincts[df_precincts['race'] == 'us-senate'].copy()
        
        if df_us_senate.empty:
            continue

        df_us_senate.sort_values('votes', ascending=False, inplace=True)
        total_votes = df_us_senate['votes'].sum()

        if total_votes == 0:
            continue

        df_us_senate = df_us_senate.assign(
            votePercent=lambda n: round(n.votes / total_votes, 5)
        )

        winner = df_us_senate.iloc[0]
        if len(df_us_senate) > 1:
            runner_up = df_us_senate.iloc[1]
            winner_margin = winner['votes'] - runner_up['votes']
            winner_percent_margin = round(winner_margin / total_votes, 5)
        else:
            winner_margin = winner['votes']
            winner_percent_margin = round(winner_margin / total_votes, 5)

        df_us_senate['votes'] = df_us_senate['votes'].astype(int)
        candidates = df_us_senate[['candidate', 'party', 'votes', 'votePercent']].to_dict(orient='records')

        output.append({
            'key': precinct_key,
            'county': first_row['county'],
            'precinct': first_row['precinct'],
            'totalVotes': int(total_votes),
            'winnerParty': winner['party'] if winner_margin > 0 else 'tie',
            'winnerName': winner['candidate'] if winner_margin > 0 else 'tie',
            'winnerVotes': int(winner['votes']),
            'winnerMargin': int(winner_margin),
            'winnerPercent': round(winner['votes'] / total_votes, 5),
            'winnerPercentMargin': winner_percent_margin,
            'candidates': candidates,
        })

    return output


reshaped = reshape_to_json(flat)

with open('../../outputs/2024/general/tester-nested-precinct-results-2024.json', 'w') as f:
    json.dump(reshaped, f, indent=4)