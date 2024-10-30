# Montana Secretary of State interface

System for wrangling election data from the MT Secretary of State's office and exporting it in more convenient formats. Developed for internal use at [Montana Free Press](https://montanafreepress.org).

### `/sos-data`

Raw data files in `sos-data` were downloaded from https://sosmt.gov/elections/results/ on on Oct. 30, 2024. As of that date, the Montana SOS didn't have an comprehensive Precinct by Precinct file data file available for the 2022 General Election. Precinct-level results for that election were instead stitched together from unofficial county-by-county vote data files downloaded from [electionresults.mt.gov](https://electionresults.mt.gov/) on 11/23/22.

### `/inputs`

Other data inputs fed into various data pipelines used by MTFP.
- `daves-redistricting` - [Dave's Redistricting](https://davesredistricting.org/) analysis for the state's 2023-2034 legislative districts.

### `/process`

Scripts for data workflow, organized by election year they apply to. Includes some one-off scripts for particular projects done at particular times. Filepaths in these are designed to be run from the repository root, e.g. as `python3 process/2022/parse-2022-precinct-results-by-county-files.py`

### `/cleaned`

Cleaned and (theoretically) standardized flat data, organized by election year.

### `/outputs`

Output files for specific purposes, organized by election year.

### `/utilities`

One-off tool scripts that may be helpful but don't fit into a neat data pipeline at this point.

