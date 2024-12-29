# Imports
from bs4 import BeautifulSoup

import json
import requests
# End Imports

# Load websites.json
with open("websites.json", 'r') as file:
    json_data = json.load(file)
    
# Get First website
first_website = json_data['websites'][0]

# Request website data

with open(first_website) as fp:
    soup = BeautifulSoup(fp, 'lxml')
    
print(soup)