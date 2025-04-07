#this code uses OpenAI api to evaluate 5 most relevant synonyms of a word.

from openai import OpenAI


def gpt_evaluates_synonyms(target_word, target_pos, synonyms):
    # Create a prompt to instruct GPT-4
    prompt = f"""
    In the context of scientific writing, I am looking for the most relevant synonyms for the word "{target_word}" which is a {target_pos}.
    The synonyms I have found are: {", ".join(synonyms)}.
    Could you please help me find the most relevant synonyms for this word?
    Please only reply with a comma-separated list of the most relevant synonyms.
    """

    client = OpenAI(
        api_key="",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user", #TODO: check for alternatives
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",
    )
    
    # Access the response content correctly
    cleaned_synonyms = chat_completion.choices[0].message.content.strip()
    # remove newlines from the response
    cleaned_synonyms = cleaned_synonyms.replace("\n", " ")
    cleaned_synonyms = cleaned_synonyms.replace(" ", "")
    cleaned_synonyms = cleaned_synonyms.replace(",", f"_{target_pos},")
    cleaned_synonyms = cleaned_synonyms + f"_{target_pos}"
    return cleaned_synonyms


input_file = open("/home/tom/Downloads/flairs/synonyms_mw.csv", "r")
output_file = open("/home/tom/Downloads/flairs/synonyms_mw_gpt_evaled.csv", "w")

c = 0
for line in input_file:
    line_cp = line
    try:
        c += 1
        print(c, end=" ", flush=True)
        line = line.strip()
        words = line.split(",")
        target = words[0]
        target_word = target.split("_")[0]
        target_pos = target.split("_")[1]
        synonyms = words[1:]
        relevant_synonyms = gpt_evaluates_synonyms(target_word, target_pos, synonyms)
        output_file.write(target + "," + relevant_synonyms + "\n")
    except Exception as e:
        print("Error at abstract number: ", c)
        print(e)
        output_file.write(line_cp)
        continue

input_file.close()
output_file.close()
