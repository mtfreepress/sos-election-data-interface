# Parse one-page-per-race, one-file-per-county precinct result files

import pandas as pd
# import re
import json

counties = [
	{"number":1,"county":"BEAVERHEAD"},
	{"number":2,"county":"BIG HORN"},
	{"number":3,"county":"BLAINE"},
	{"number":4,"county":"BROADWATER"},
	{"number":5,"county":"CARBON"},
	{"number":6,"county":"CARTER"},
	{"number":7,"county":"CASCADE"},
	{"number":8,"county":"CHOUTEAU"},
	{"number":9,"county":"CUSTER"},
	{"number":10,"county":"DANIELS"},
	{"number":11,"county":"DAWSON"},
	{"number":12,"county":"DEER LODGE"},
	{"number":13,"county":"FALLON"},
	{"number":14,"county":"FERGUS"},
	{"number":15,"county":"FLATHEAD"},
	{"number":16,"county":"GALLATIN"},
	{"number":17,"county":"GARFIELD"},
	{"number":18,"county":"GLACIER"},
	{"number":19,"county":"GOLDEN VALLEY"},
	{"number":20,"county":"GRANITE"},
	{"number":21,"county":"HILL"},
	{"number":22,"county":"JEFFERSON"},
	{"number":23,"county":"JUDITH BASIN"},
	{"number":24,"county":"LAKE"},
	{"number":25,"county":"LEWIS AND CLARK"},
	{"number":26,"county":"LIBERTY"},
	{"number":27,"county":"LINCOLN"},
	{"number":28,"county":"MADISON"},
	{"number":29,"county":"MCCONE"},
	{"number":30,"county":"MEAGHER"},
	{"number":31,"county":"MINERAL"},
	{"number":32,"county":"MISSOULA"},
	{"number":33,"county":"MUSSELSHELL"},
	{"number":34,"county":"PARK"},
	{"number":35,"county":"PETROLEUM"},
	{"number":36,"county":"PHILLIPS"},
	{"number":37,"county":"PONDERA"},
	{"number":38,"county":"POWDER RIVER"},
	{"number":39,"county":"POWELL"},
	{"number":40,"county":"PRAIRIE"},
	{"number":41,"county":"RAVALLI"},
	{"number":42,"county":"RICHLAND"},
	{"number":43,"county":"ROOSEVELT"},
	{"number":44,"county":"ROSEBUD"},
	{"number":45,"county":"SANDERS"},
	{"number":46,"county":"SHERIDAN"},
	{"number":47,"county":"SILVER BOW"},
	{"number":48,"county":"STILLWATER"},
	{"number":49,"county":"SWEET GRASS"},
	{"number":50,"county":"TETON"},
	{"number":51,"county":"TOOLE"},
	{"number":52,"county":"TREASURE"},
	{"number":53,"county":"VALLEY"},
	{"number":54,"county":"WHEATLAND"},
	{"number":55,"county":"WIBAUX"},
	{"number":56,"county":"YELLOWSTONE"}
]

races = {
    # There are more races in these files — these are just the ones I was interested in
    'UNITED STATES REPRESENTAT 0745': 'us-house-west',
    'UNITED STATES REPRESENTAT 0746': 'us-house-east',
    'SUPREME COURT JUSTICE #1 0849': 'supco-1',
    'SUPREME COURT JUSTICE #2 0850': 'supco-2',
    'CONSTITUTIONAL AMENDMENT  2127': 'ci-48',
    'LEGISLATIVE REFERENDUM NO 2128': 'lr-131',
}

def parse_sheet(file, county, sheet_name, election):
    dfi = pd.read_excel(file, sheet_name, skiprows=6)
    dfi = dfi.iloc[:,1:].copy()
    dfi = dfi[dfi['Precinct'] != 'TOTALS'].copy()

    long = dfi.melt(id_vars=['Precinct'], var_name='raw_candidate', value_name='votes')
    long.rename(columns={'Precinct': 'precinct'}, inplace=True)
    
    long['county'] = county
    long['key'] = long['precinct'].map(lambda precinct: f'{county}-{precinct}')
    long['election'] = election
    long['race'] = races[sheet_name]
    long['candidate'] = long['raw_candidate'].map(lambda n: n.split('\n')[0])

    def get_party(n):
        if (len(n.split('\n')) == 1): return n.split('\n')[0]
        return n.split('\n')[1]
    long['party'] = long['raw_candidate'].map(get_party)
    long.drop('raw_candidate',axis=1, inplace=True)

    long = long[['election', 'race', 'key', 'county', 'precinct', 'party', 'candidate', 'votes']]

    return long


def parse_file(file, county, election):
    xl = pd.ExcelFile(file)
    sheet_names = xl.sheet_names

    races_in_sheet = [race for race in races.keys() if race in sheet_names]

    df = pd.DataFrame()
    for sheet in races_in_sheet:
        # print(sheet)
        dfi = parse_sheet(file, county, sheet, election)
        df = pd.concat([df, dfi])
    return df


def parse_county_files():
    df = pd.DataFrame()
    for county in counties:
        number = county['number']
        dfi = parse_file(f'./sos-data/2022/general/precinct-results-by-county/CTYALL Results({number}).xlsx', county['county'], '2023-gen')
        df = pd.concat([df, dfi])
    return df

results = parse_county_files()

# OUT_PATH = './cleaned/2022/general/precinct-results.json'
# results.to_json(OUT_PATH, orient='records')
OUT_PATH = './cleaned/2022/general/precinct-results.csv'
results.to_csv(OUT_PATH, index=False)
print('Writen to', OUT_PATH)