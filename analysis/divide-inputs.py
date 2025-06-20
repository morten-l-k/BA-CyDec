import json

# Set threshold of number of characters to divide at
THRESHOLD = 100

# Input and output file paths
input_file = 'extracted_inputs.json'
short_output = 'short.json'
long_output = 'long.json'

# Read the fixed JSON list
with open(input_file, 'r') as infile:
    data = json.load(infile)

# Split into short and long commands
short_cmds = []
long_cmds = []

#Run through each line in the data
for entry in data:
    if len(entry.get('input', '')) <= THRESHOLD:
        short_cmds.append(entry)
    else:
        long_cmds.append(entry)

# Write output to files
with open(short_output, 'w') as short_file:
    json.dump(short_cmds, short_file, indent=2)

with open(long_output, 'w') as long_file:
    json.dump(long_cmds, long_file, indent=2)
