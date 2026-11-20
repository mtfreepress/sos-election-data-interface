# Fetch precinct results data available county-by-county
# Downloads one file per county (relies on MacOs reduntant file numbering scheme to label files)

import os
import time
import signal
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime

# create custom download directory in utilities/manual-download-results
download_dir = os.path.join(os.path.dirname(__file__), 'manual-download-results')
os.makedirs(download_dir, exist_ok=True)

def clear_download_dir(directory):
    """Clear all files from the download directory."""
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

counties = [str(i + 1).rjust(2, '0') for i in range(56)]

def get_existing_files(directory):
    """Get a list of files currently in the directory."""
    return set(os.listdir(directory))

def verify_download(url, base_filename, max_retries=2, timeout=30):
    """Verify if the file downloads successfully."""
    retries = 0
    while retries < max_retries:
        try:
            # custom download directory in project
            options = Options()
            options.set_preference("browser.download.dir", download_dir)
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(options=options)

            # check files in directory
            initial_files = get_existing_files(download_dir)
            
            # download
            driver.get(url)
            driver.execute_script("DownloadFile(); __doPostBack('ctl00$NavLinks$lnkbtnSWExport','')")
            
            # wait for file to appear to trigger closing window
            start_time = time.time()
            while time.time() - start_time < timeout:
                current_files = get_existing_files(download_dir)
                new_files = current_files - initial_files

                # check to make sure file matches expected pattern
                for new_file in new_files:
                    if new_file.startswith(base_filename):
                        # delay to avoid closing too soon and firefox erroring
                        time.sleep(1)
                        print(f"Successfully downloaded: {new_file}")
                        driver.quit()
                        return True
                time.sleep(1)  # Poll every second
            
            # timeout - retry
            print(f"Download timed out for {url}.")
            driver.quit()
            retries += 1
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f"Error during download: {e}")
            retries += 1

        print(f"Retrying ({retries}/{max_retries})...")

    print(f"Failed to download {url} after {max_retries} retries.")
    return False

def signal_handler(sig, frame):
    print('You pressed Ctrl+C, exiting...')
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

# clear custom directory before starting
clear_download_dir(download_dir)

# main script
all_successful = True
for c in counties:
    url = f"https://electionresults.mt.gov/ResultsSW.aspx?type=CTYALL&cty={c}&map=CTY"
    base_filename = "CTYALL Results"  # Base name of the expected file
    if not verify_download(url, base_filename):
        print(f"Failed to download data for county {c}")
        all_successful = False

# update-time.txt with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
update_time_path = os.path.join(download_dir, 'update-time.txt')
with open(update_time_path, 'w') as f:
    f.write(f"Last update time: {timestamp}\n")

# final log
if all_successful:
    print(f"All files downloaded successfully. Update time written to {update_time_path}.")
else:
    print(f"Some files failed to download. Update time written to {update_time_path}.")