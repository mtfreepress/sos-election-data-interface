# Fetch precinct results data available county-by-county
# Downloads one file per county (relies on MacOs reduntant file numbering scheme to label files)

from selenium import webdriver
import time

counties = [str(i+1).rjust(2,'0') for i in range(56)]
for c in counties:
    driver = webdriver.Firefox()
    driver.get(f"https://electionresults.mt.gov/ResultsSW.aspx?type=CTYALL&cty={c}&map=CTY")
    driver.execute_script("DownloadFile(); __doPostBack('ctl00$NavLinks$lnkbtnSWExport','')")
    time.sleep(10)
    driver.quit()