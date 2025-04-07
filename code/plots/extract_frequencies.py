#this code extracts the freqencies of words overtime and plots

import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def extract_synonyms(input_file_path):
    # Initialize an empty dictionary to store the synonyms
    synonym_group = {}
    # Open the CSV file and read it line by line
    with open(input_file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                key = row[0]
                values = row[1:6]  # Get columns 2 to 6
                synonym_group[key] = [value for value in values if value]  # Filter out empty values
    return synonym_group


def opms_per_year(year):
    frequencies = dict()
    frequencies_normalized = dict()
    total_count = 0
    file_path = f'/home/tom/delve4/pos_tagged_counted/{year}.txt'
    with open(file_path, 'r') as year_file:
        for line in year_file:
            line = line.strip()
            entry = line.split()[0]
            count = int(line.split()[1])
            total_count += count
            frequencies[entry] = count
    
    for entry in frequencies:
        frequencies_normalized[entry] = frequencies[entry] / total_count
    return frequencies_normalized


if __name__ == '__main__':
    synonym_file_path = '/home/tom/delve4/plots_new/gpt_most_relevant_synonyms_cleaned.csv'
    synonym_group = extract_synonyms(synonym_file_path)

    for target in synonym_group:
        synonyms = synonym_group[target]
        columns = ["year", target, *synonyms]
        df = pd.DataFrame(columns=columns)        
        for year in range(1975, 2025):
            opms = opms_per_year(year)
            target_freq = opms.get(target, 0)  # Default to 0 if target is not found
            synonym_freqs = [opms.get(synonym, 0) for synonym in synonyms]  # Default to 0 if synonym is not found
            row = [year, target_freq, *synonym_freqs]
            df.loc[len(df)] = row
        
        blue_shades = ["darkblue", "blue", "deepskyblue", "mediumspringgreen", "limegreen"]  # Adjust range for distinct shades
        plt.figure(figsize=(12, 6))  # Set the figure size

        

        # Plot the remaining columns in shades of blue
        for i, column in enumerate(columns[2:]):  # Exclude 'year' and first column
            plt.plot(df["year"], df[column], label=column, color=blue_shades[i])
        
        # Plot the first column in purple
        plt.plot(df["year"], df[columns[1]], label=columns[1], color="deeppink")

        # Add labels, title, and legend
        plt.xlabel("Year")
        plt.ylabel("Frequency")
        plt.title("Frequency of Synonyms Over Time")
        plt.legend(title="Synonyms", loc="upper left")
        plt.grid(True, linestyle="--", alpha=0.6)  # Optional: Add gridlines

        plot_save_path = f'/home/tom/delve4/plots_new/plots/{target}.png'
        plt.savefig(plot_save_path)
        plt.close()
        
            
            
