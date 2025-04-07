# Exploring the Structure of AI-Induced Language Change in Scientific English

This repository contains the code and data of the paper "Exploring the Structure of AI-Induced Language Change in Scientific English".

## Abstract

Scientific English has undergone rapid and unprecedented changes in recent years, with words such as "delve," "intricate," and "crucial" showing significant spikes in frequency since around 2022. These changes are widely attributed to the growing influence of Large Language Models like ChatGPT in the discourse surrounding bias and misalignment. However, apart from changes in frequency, the exact structure of these linguistic shifts have remained unclear. The present study fills this gap and investigates whether these changes involve the replacement of synonyms by a "buzzword,” for example, "crucial" replacing "essential" and "key," or whether they reflect broader stylistic and pragmatic trends. To further investigate structural changes, we include part of speech tagging in our analysis to quantify linguistic shifts over grammatical categories and differentiate between word forms. We systematically analyze synonym groups for widely discussed "buzzwords" based on frequency trends in scientific abstracts from PubMed. We find that entire semantic clusters often shift together, with most or all words in a group increasing in usage. This pattern suggests that changes induced by Large Language Models are primarily stylistic and pragmatic rather than purely lexical. Notably, the adjective "important" shows a significant decline, which prompted us to systematically analyze decreasing lexical items. Our analysis of “collapsing” words reveals a more complex picture, which is consistent with organic language change and contrasts with the patterns of the abrupt spikes. These insights into the structure of language change contribute to our understanding of how language technology continues to shape human language.

## Repository Contents

* data: This repository contains sample data, as the full data is too large and needs to be built locally with the code.
* code: Python scripts are used for the extraction of focal words (brute_force_div.py and process_PubMed_files.py in /get_human_data/)and generating AI abstracts (in /generate_ai_data/). Plots can be generated with the code in /plots/. 


## Requirements and Running the Code
* Python 3.9+
* SpaCy 
* Install required packages via pip

## Note on Code
The following scripts were used from "Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models" (not sure how to cite here)
* /ai_write_abstracts.py, /brute_force_div.py, /download_dataset.py, /extract_abstracts.py,/process_PubMed_files.py ,/sample_human_abstracts.py, /extract_frequencies.py, /plot_word_freq.py, 
## Citation

If you use this code or data in your research, please cite:
 ```bibtex
 @article{Anonymous2025, title={Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models}, author={Anonymous}, journal={tbd}, year={2025}
 ```

## Licence

The licence of this project has yet to be determined.


## Contact

For any questions or issues, please contact the repo owner.
