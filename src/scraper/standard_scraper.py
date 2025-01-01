# Imports
from bs4 import BeautifulSoup, FeatureNotFound
from requests.exceptions import SSLError

import requests
import logging
# End Imports

class StandardScraper:
    
    def __init__(self, website):
        self.website = website
    
    def scrape(self):
        
        html_data = self.request_website()
        return self.parser(html_data)
    
    def request_website(self):
        """ Retreieves HTML Data from website """
        
        response = requests.get(self.website)
        
        if response.status_code == 200:
            return response.text 
        
        elif response.status_code == 404:
            error_message = f'Resource not found(404): Unable to connect to website {self.website}'
            logging.debug(error_message)
            raise ConnectionError(error_message)
        
    def parser(self, html_data):
        
        try:
            soup = BeautifulSoup(html_data, "html.parser")
        
        except FeatureNotFound:
            logging.error("The parser is not found. Change selected parser")
            
        soup_dictionary ={
            "title":soup.title.string.strip()
        }
        
        return soup_dictionary