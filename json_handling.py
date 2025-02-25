# Read JSON from a file:

import json
with open('output.json', 'r') as file:
 data = json.load(file)
 print(data)

# Write JSON to a file:

import json
data = {'name': 'DevOps', 'type': 'Workflow'}
with open('output.json', 'w') as file:
 json.dump(data, file, indent=4)