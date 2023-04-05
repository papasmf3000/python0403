import re

# Open the log file for reading
with open('pv3.txt', 'r') as f:
    # Create a new file for writing the matching lines
    with open('result.txt', 'w') as result_file:
        # Loop through each line in the log file
        for line in f:
            # Use regular expression to match the year format (yyyy.mm.dd.hh)
            match = re.search(r'\d{4}\.\d{2}\.\d{2}\.\d{2}', line)
            # If a match is found, write the line to the result file
            if match:
                result_file.write(line)
