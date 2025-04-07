
"""
This script is used to generate AI-written abstracts for scientific papers using the OpenAI API.

- The script reads input from a file containing summary notes.
- It sends each note as a prompt to the GPT model to generate a corresponding abstract.
- The generated abstracts are written to an output file.
- The script also includes a cleaning step that removes unwanted prefixes like 'Abstract:' and 'Title:' from the generated abstracts.

The OpenAI API key must be set as an environment variable for security purposes.
"""


import os
import re
import openai 


# Code has been refactored using Copilot and ChatGPT
# Fetch API key from environment variables for security

api_key = os.getenv("OPENAI_API_KEY", " Replace with your actual API key")  
if not api_key:
    raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")
openai.api_key = api_key

# Define the GPT engine to use
gpt_engine = "gpt-4o-mini"  # Replace with the specific GPT engine you prefer

# Define file paths
input_file_path = "ai_summary.txt"
output_file_path = f"ai_abstracts.txt"

def process_abstracts(input_path, output_path):
    """
    Processes abstracts from the input file, generates responses using the OpenAI API, 
    and writes the generated abstracts to the output file.

    Parameters:
    - input_path (str): The path to the input file containing the abstracts to process.
    - output_path (str): The path to the output file where the generated abstracts will be written.
    """
    # Read abstracts from the input file
    with open(input_path, "r") as file:
        abstracts = file.read().splitlines()

    # Process each abstract and generate a response using GPT
    with open(output_path, "a") as output_file:
        for idx, abstract in enumerate(abstracts):
            try:
                abstract = abstract.strip()
                prompt = f"""Please write an abstract for a scientific paper, about 200 words in length, based on the following notes: "{abstract}" """
                response = openai.ChatCompletion.create(
                    model=gpt_engine,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=2000
                )

                # Extract and clean the generated response
                gpt_response = response['choices'][0]['message']['content'].strip().replace("\n", " ")
                output_file.write(gpt_response + "\n")
                print(f"Processed abstract {idx}")


            except Exception as e:
                print(f"Error at abstract number {idx}: {e}")
                continue

def clean_abstracts(output_path):
    """
    Cleans the abstracts in the output file by removing unnecessary lines and formatting issues.
    Removes text preceding 'Abstract:' and lines containing 'Title:'.

    Parameters:
    - output_path (str): The path to the output file that will be cleaned.
    """
    # Read the output file
    with open(output_path, "r") as input_file:
        lines = input_file.readlines()

    # Regular expression to match leading content before 'Abstract:'
    pattern = re.compile(r'.*?[Aa]bstract:')

    # Clean the abstracts
    cleaned_output = []
    for line in lines:
        line = line.strip()
        if "bstract:" in line[:80]:
            line = re.sub(pattern, '', line).strip()
        if not ("Title:" in line[:25] or "title:" in line[:25]):
            cleaned_output.append(line)

    # Ensure no more than one consecutive newline
    output_string = "\n".join(cleaned_output)
    output_string = re.sub(r'\n{2,}', '\n', output_string).lstrip("\n")

    # Write the cleaned content back to the file
    with open(output_path, "w") as output_file:
        output_file.write(output_string)

if __name__ == "__main__":
    """
    Main entry point for the script.
    Calls the functions to process and clean abstracts.
    """
    process_abstracts(input_file_path, output_file_path)
    clean_abstracts(output_file_path)
