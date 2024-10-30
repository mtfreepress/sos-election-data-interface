# Parses SOS General election precinct result .xls files
# 2018 and 2020 files were  edited to remove custom SOS headers

import pandas as pd
import re
import json

years = ['2014','2016','2018','2020']

def cat_race(race_name):
    if (re.search(r'STATE SENATOR DISTRICT \d+', race_name)):
        return 'senate'
    if (re.search(r'STATE REPRESENTATIVE DISTRICT \d+', race_name)):
        return 'house'
    if (re.search(r'GOVERNOR & LT. GOVERNOR', race_name)):
        return 'governor'
    if (re.search(r'PRESIDENT', race_name)):
        return 'president'
    if (re.search(r'PRESIDENT AND VICE PRESIDENT', race_name)):
        return 'president'
    if (re.search(r'SECRETARY OF STATE', race_name)):
        return 'secretary of state'
    if (re.search(r'ATTORNEY GENERAL', race_name)):
        return 'attorney general'
    if (re.search(r'STATE AUDITOR', race_name)):
        return 'state auditor'
    if (re.search(r'UNITED STATES SENATOR', race_name)):
        return 'us senate'
    else:
        return 'omit'

def clean(year):
    results = pd.read_excel(f'./sos-data/{year}/general/{year}-General-Statewide-by-Precinct.xlsx')
    results['election'] = f'{year}-gen'
    results['race'] = results['RaceName'].apply(cat_race)
    results['key'] = results['CountyName'] + '-' + results['PrecinctName'].astype("string")
    results['county'] = results['CountyName']
    results['precinct'] = results['PrecinctName']
    results['party'] = results['PartyCode'].str[:1]
    results['candidate'] = results['NameOnBallot']
    results['votes'] = results['Votes']
    

    return results[['election','race', 'key', 'county', 'precinct', 'party', 'candidate', 'votes']]
    
for year in years:
    clean(year).to_csv(f'./cleaned/{year}/general/precinct-results.csv', index=False)
print('Done')