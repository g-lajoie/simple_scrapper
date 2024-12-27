import json

with open('websites.json', 'r') as json_file:
    websites = json.load(json_file)
    
print(*websites.values())