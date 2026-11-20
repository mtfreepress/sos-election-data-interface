# Reshape flat csv of precinct-level results to nested JSON
# that's easier to use in interactive data visualizations

import pandas as pd
import json

races = {
    # should match all races in parse-20XX-precinct-reults-by-county.py
    '01602UNITED STATES SENATOR 450': 'us-senate',
    '01603UNITED STATES REPRESENTAT': 'us-house-west',
    '01604UNITED STATES REPRESENTAT': 'us-house-east',
    '01605GOVERNOR & LT. GOVERNOR 4': 'governor',
    '01606SECRETARY OF STATE 450000': 'sos',
    '01607ATTORNEY GENERAL 45000000': 'ag',
    '01609STATE SUPERINTENDENT OF P': 'si-opi',
    '01608STATE AUDITOR 45000000000': 'state-audit',
    '01614SUPREME COURT CHIEF JUSTI': 'supco-chief',
    '01615SUPREME COURT JUSTICE #3 ': 'supco-3',
    '01613CLERK OF THE SUPREME COUR': 'supco-clerk',
    '01610PUBLIC SERVICE COMMISSION': 'psc-2',
    '01611PUBLIC SERVICE COMMISSION': 'psc-3',
    '01612PUBLIC SERVICE COMMISSION': 'psc-4',
    '04779CI-126 A CONSTITUTIONAL A': 'ci-126',
    '04780CI-127 A CONSTITUTIONAL A': 'ci-127',
    '04781CI-128 A CONSTITUTIONAL A': 'ci-128',
}

flat = pd.read_csv('../../cleaned/2024/general/precinct-results.csv')


def reshape_to_json(df):
    def standardize_precinct_name(val):
        return str(val).replace('&', 'and').replace('-', '_').replace(' ', '_').upper()

    precincts = df['key'].unique()
    race_keys = list(races.values())

    output = []
    for precinct in precincts:
        df_precincts = df[df['key'] == precinct]
        first_row = df_precincts.iloc[0]

        # Standardize precinct name
        precinct_key = standardize_precinct_name(precinct)

        race_results = []
        for race in race_keys:
            df_precinct_race_results = df_precincts[df_precincts['race'] == race].copy()
            df_precinct_race_results.sort_values('votes', ascending=False, inplace=True)

            total_votes = df_precinct_race_results['votes'].sum()
            if total_votes == 0:
                continue

            df_precinct_race_results = df_precinct_race_results.assign(
                votePercent=lambda n: round(n.votes / total_votes, 5)
            )

            winner = df_precinct_race_results.iloc[0]

            if len(df_precinct_race_results) > 1:
                runner_up = df_precinct_race_results.iloc[1]
                winner_margin = winner['votes'] - runner_up['votes']
                winner_percent_margin = round(winner_margin / total_votes, 5)
            else:
                winner_margin = winner['votes']
                winner_percent_margin = winner['votes'] / total_votes

            df_precinct_race_results['votes'] = df_precinct_race_results['votes'].astype('int')
            candidates = df_precinct_race_results[['candidate', 'party', 'votes', 'votePercent']].to_dict(orient='records')

            race_results.append({
                'race': race,
                'totalVotes': int(total_votes),
                'winnerParty': winner['party'] if winner_margin > 0 else 'tie',
                'winnerName': winner['candidate'] if winner_margin > 0 else 'tie',
                'winnerVotes': int(winner['votes']),
                'winnerMargin': int(winner_margin),
                'winnerPercent': round(winner['votes'] / total_votes, 5),
                'winnerPercentMargin': winner_percent_margin,
                'candidates': candidates,
            })

        output.append({
            'key': precinct_key,
            'county': first_row['county'],
            'precinct': first_row['precinct'],
            'races': race_results,
        })

    return output


reshaped = reshape_to_json(flat)

with open('../../outputs/2024/general/nested-precinct-results-2024.json', 'w') as f:
    json.dump(reshaped, f, indent=4)