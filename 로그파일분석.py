import re

# Open the input and output files
with open('input_file.txt', 'r') as input_file, open('results.txt', 'w') as output_file:

    # Loop through each line in the input file
    for line in input_file:

        # Use regular expression to find a year in the line
        match = re.search(r'\d{4}', line)

        # If a year is found, write the line to the output file
        if match:
            output_file.write(line)
