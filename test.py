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
response = requests.get(first_website)

# Check if Status Code was successful and return data
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup.prettify())
    
else:
    print(f'{response.code}: Failed to fetch {first_website}')