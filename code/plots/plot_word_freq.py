
# this code plots the word freqency of the data using panndas and numpy
import pandas as pd
import numpy as np

# Load the TSV data
file_name = 'all_words_syn_underscore'
file_path = f'/home/tom/Downloads/flairs/plots/{file_name}.tsv'
df = pd.read_csv(file_path, sep='\t')

# Display the first few rows and data types to understand its structure
df.head(), df.dtypes

# Restructure the data for plotting
# Pivot the table to have words as columns and years as rows
pivot_df = df.pivot(index='year', columns='lexit', values='opm')

# Plot the data
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))

for word in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df[word], label=word)

plt.xlabel('Year')
plt.ylabel('Relative frequency')
plt.title('Word frequencies 1975-2024 (per million)')
plt.xticks(np.arange(min(pivot_df.index), max(pivot_df.index) + 2, 5))
plt.legend(title='Words', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
# Save the plot
plt.savefig(f'/home/tom/Downloads/flairs/plots/{file_name}.png')
plt.show()
