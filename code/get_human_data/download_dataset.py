"""
A module to download PubMed XML datasets from a specified URL.

Usage:
    python download_dataset.py
"""

import urllib.request
import logging
from pathlib import Path


# Code has been refactored using Copilot and ChatGPT
# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
BASE_URL = "https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/"
SAVE_DIR = Path("pubmed_data_2024_update") #specify the path to save the files
FILE_RANGE = range(1220, 1398)


def create_directory(directory):
    """Ensure directory exists."""
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)

def download_file(file_url, local_path):
    """Download a file from a specific URL to a local path."""
    try:
        logging.info(f"Downloading {local_path.name}...")
        urllib.request.urlretrieve(file_url, local_path)
    except Exception as e:
        logging.error(f"Failed to download {local_path.name}: {e}")

def main():
    """Main function to orchestrate the downloading of files."""
    create_directory(SAVE_DIR)
    
    for i in FILE_RANGE:
        file_name = f"pubmed24n{i:04}.xml.gz"
        file_url = BASE_URL + file_name
        local_path = SAVE_DIR / file_name
        
        download_file(file_url, local_path)
    
    logging.info("Download complete.")


if __name__ == "__main__":
    main()

""" 
command line script:
/Users/rachel/CLionProjects/1Cop3014/cmake-build-debug/CMakeFiles/1Cop3014.dir/Users/rachel/CLionProjects/delve/tjs_focalword/process_pubmed_files.py --input-dir /Users/rachel/CLionProjects/1Cop3014/cmake-build-debug/CMakeFiles/1Cop3014.dir/Users/rachel/CLionProjects/delve/tjs_focalword/pubmed_data_years_update --output-dir /Users/rachel/CLionProjects/1Cop3014/cmake-build-debug/CMakeFiles/1Cop3014.dir/Users/rachel/CLionProjects/delve/tjs_focalword/pubmed_data_years_clean_update
"""
