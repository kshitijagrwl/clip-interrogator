import re

# Input file name
input_file = 'clip_interrogator/data/flavors.txt'

# Output file name
output_file = 'cleaned_output1.txt'

# Regular expression to match lines with numbers and spaces only
pattern = re.compile(r'^\d+(\s\d+)*$')

# Open the input and output files
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w',encoding='utf-8') as outfile:
    # Loop through each line in the input file
    for line in infile:
        # Strip leading and trailing whitespace
        line = line.strip()

        # Check if the line matches the regular expression pattern
        if not pattern.match(line):
            # If the line does not match the pattern, replace space-separated digits with concatenated version
            line = re.sub(r'(\d) (\d)', r'\1\2', line)
            # Write the modified line to the output file
            outfile.write(line + '\n')

# Close the files
infile.close()
outfile.close()

print(f"File '{input_file}' has been cleaned. Cleaned content is saved in '{output_file}'.")
