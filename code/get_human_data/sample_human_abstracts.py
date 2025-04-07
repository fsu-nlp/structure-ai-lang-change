"""
A module to randomly sample abstracts from a specified text file for further analysis.

Usage:
    python sample_human_abstracts.py --file-path <file_path> --sample-size <sample_size>
"""

import random
import argparse
import logging
from pathlib import Path


# Code has been refactored using Copilot and ChatGPT
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sample_abstracts(file_path, sample_size):
    """Sample a specified number of lines from a file."""
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        if len(lines) < sample_size:
            logging.error("Sample size is greater than the total number of lines available.")
            return
        
        random_sample = random.sample(lines, sample_size)
        output_path = Path(file_path).parent / f"input_human_abstracts_sample_{Path(file_path).stem}.txt"
        
        with open(output_path, "w") as file:
            file.writelines(random_sample)
        
        logging.info(f"Sampled {sample_size} abstracts to {output_path}")
    except FileNotFoundError:
        logging.error(f"The file {file_path} does not exist.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    """Run the script with command-line arguments."""
    parser = argparse.ArgumentParser(description="Sample abstracts from a text file.")
    parser.add_argument('--file-path', type=str, required=True, help="Path to the text file.")
    parser.add_argument('--sample-size', type=int, required=True, help="Number of abstracts to sample.")
    args = parser.parse_args()

    sample_abstracts(args.file_path, args.sample_size)


if __name__ == "__main__":
    main()
