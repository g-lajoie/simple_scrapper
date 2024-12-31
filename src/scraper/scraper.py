# Imports
from bs4 import BeautifulSoup

import asyncio
import json
import requests
from typing import List
# End Imports


class Scraper:
    
    def __init__(self, website:str):
        self.websites = website
    
    async def scrape():
        

    def request_website(self):
        response = requests.get(self.website)

        if not response.status_code == 200:
            return 

        return response.text

    
    
