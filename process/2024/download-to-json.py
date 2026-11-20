## Needs testing 11-18-2024

# import subprocess
# import os
# ## all in one runs the download, parse and nest functions to go from json to 
# def run_script(script_path):
#     """Runs a script using subprocess."""
#     try:
#         result = subprocess.run(['python', script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         print(f"Successfully ran {script_path}")
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         print(f"Error running {script_path}: {e.stderr.decode()}")
#         raise

# def download_to_json():
#     # script paths
#     utilities_path = os.path.join(os.path.dirname(__file__), '../../utilities', 'manual-file-download.py')
#     parse_script = os.path.join(os.path.dirname(__file__), 'parse-2024-precinct-results-by-county-files.py')
#     nest_script = os.path.join(os.path.dirname(__file__), 'nest-2024-precinct-results.py')

#     # run scripts in order
#     run_script(utilities_path)
#     run_script(parse_script)
#     run_script(nest_script)

# if __name__ == "__main__":
#     download_to_json()
