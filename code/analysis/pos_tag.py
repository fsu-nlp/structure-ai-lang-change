
#this code is to tag a file for part of speech using spacy
import spacy

# Load the SpaCy language model
nlp = spacy.load("en_core_web_sm")

#if spacy.prefer_gpu():
#    nlp = nlp.cuda()

def pos_tag_sentence(sentence):
    doc = nlp(sentence)
    tagged_sentence = " ".join([f"{token.lemma_}_{token.pos_}" for token in doc])
    return tagged_sentence

# Example usage
input_sentence = "This is a sentence"
output_sentence = pos_tag_sentence(input_sentence)
print(output_sentence)

# If you want to process a file
input_file = "pubmed_sample.txt"
output_file = "pubmed_sample_pos.txt"

c = 0
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        tagged_line = pos_tag_sentence(line.strip())
        outfile.write(tagged_line + "\n")
        c += 1
        if c % 500 == 0:
            print(f"Processed {c} lines")
