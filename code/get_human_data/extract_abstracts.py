"""
A module to extract abstracts from PubMed XML files and save them grouped by publication year.

Usage:
    python extract_abstracts.py
"""

import xml.etree.ElementTree as ET
import os
import re
import logging
from pathlib import Path
import gzip
import shutil



# Code has been refactored using Copilot and ChatGPT
# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
DIRECTORY_PATH = Path("pubmed_data_2024_update")
OUTPUT_DIR = Path("pubmed_data_years_update")
SPACE_RE = re.compile(r' +')

def decompress_file(gz_path):
    """Decompress a .gz file and return the path to the decompressed file."""
    decompressed_path = gz_path.with_suffix('')  # Remove .gz extension
    try:
        with gzip.open(gz_path, 'rb') as f_in:
            with open(decompressed_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        logging.info(f"Decompressed {gz_path} to {decompressed_path}")
    except Exception as e:
        logging.error(f"Error decompressing {gz_path}: {e}")
        return None
    return decompressed_path

def process_pubmed_file(file_path):
    """
    Process a single PubMed XML file to extract and save abstracts.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        abstracts = {}

        for pubmed_article in root.findall('.//PubmedArticle'):
            year_element = pubmed_article.find('.//PubDate/Year')
            abstract_text_elements = pubmed_article.findall('.//Abstract/AbstractText')
            
            if year_element is not None and abstract_text_elements:
                abstract_text = ' '.join(''.join(abstract.itertext()) for abstract in abstract_text_elements)
                abstract_text = abstract_text.replace("\n", " ").strip()
                abstract_text = SPACE_RE.sub(' ', abstract_text)

                year = year_element.text
                if year not in abstracts:
                    abstracts[year] = []
                abstracts[year].append(abstract_text)
    
        for year, abstract_list in abstracts.items():
            year_file = OUTPUT_DIR / f"{year}.txt"
            with open(year_file, 'a') as file:
                file.write('\n'.join(abstract_list) + '\n')
    except ET.ParseError as e:
        logging.error(f"XML parsing error in {file_path}: {e}")
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")

def main():
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for gz_file in DIRECTORY_PATH.glob("*.gz"):
        logging.info(f"Decompressing {gz_file}...")
        decompressed_file = decompress_file(gz_file)
        if decompressed_file:
            process_pubmed_file(decompressed_file)
            
    for filename in DIRECTORY_PATH.glob("*.xml"):
        logging.info(f"Processing {filename}...")
        process_pubmed_file(filename)


if __name__ == "__main__":
    main()
