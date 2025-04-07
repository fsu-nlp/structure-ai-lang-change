
#This code is for analysis of synonyms


input_file_synonym = open("/gpt_most_relevant_synonyms_cleaned.csv", "r")
input_file_brute_force = open("brute_force_new_pos.txt", "r")
output_file = open("explore_relevant_synonyms.csv", "w")

# Read brute force file into a dictionary for efficient lookup
brute_force_dict = {}
for line in input_file_brute_force:
    parts = line.strip().split("\t")  # Split line by tab
    if len(parts) >= 2:  # Ensure there are at least `word` and `change (%)`
        word = parts[0]
        percent_change = parts[1]
        opm_base = parts[2]
        opm_inst = parts[3]
        significance = parts[4]
        brute_force_dict[word] = [percent_change, opm_base, opm_inst, significance]  # Map word to its percent change

c = 0
for line in input_file_synonym:
    line_cp = line
    try:
        c += 1
        print(c, end=" ", flush=True)

        # Process the line
        line = line.strip()
        words = line.split(",")
        target = words[0]
        synonyms = words[1:] 

        # Look up synonyms in the brute force dictionary and save matches with percent change
        matches = []
        for synonym in synonyms:
            if synonym in brute_force_dict:
                percent_change = brute_force_dict[synonym][0]
                opm_base = brute_force_dict[synonym][1]
                opm_inst = brute_force_dict[synonym][2]
                significance=brute_force_dict[synonym][3]
                percent_change = float(percent_change)
                if percent_change < 0:
                    sign = "DEC"
                    #matches.append(f"({synonym} : {sign} by {percent_change} %, opm_base : {opm_base}, opm_inst : {opm_inst}, and significance : {significance} )")
                else:
                    sign = "inc"
                matches.append(f"({synonym} : {sign} by {percent_change} %, opm_base : {opm_base}, opm_inst : {opm_inst}, and significance : {significance} )")  # Append synonym and percent change

        # Write to output
        matches_str = ",".join(matches)  # Convert matches list to a comma-separated string
        output_file.write(target + "," + matches_str + "\n")

    except Exception as e:
        print("\nError at synonym number:", c)
        print(e)
        output_file.write(line_cp)
        continue

# Close files
input_file_synonym.close()
input_file_brute_force.close()
output_file.close()
