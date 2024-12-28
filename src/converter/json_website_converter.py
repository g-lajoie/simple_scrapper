# Imports
from .website_converter import IWebsiteConverter
import re
from typing import List

# End Imports


class JsonWebsiteConverter(IWebsiteConverter):
    
    def __init__(self):
        pass
        
    def create_websites(self) -> List:
        """Create a list of websites from the self.from_json attribute.
        
        The from_json attributes takes a file that has been deserailized (converted to python dictionary), using the
        json.load(s) function
        """
        
        if not isinstance(self.from_json, dict):
            raise TypeError(f"{self.from_json} is not of type list")
        
        if isinstance(self.from_json.values(), list):
            pass
        
    def validate_website_key(self):
        """If self.from_json attribute is used, validate that at least one key contains websites"""
        
        if self.from_json is None:
            return
        
        if "websites" not in self.from_json:
            raise KeyError('The key website is missing form the dictionary parsed from json')
        
    def website_presence_check(self, website:str) -> bool:
        """Checks to see the presence of a website"""
                         
        # Check top level domain to make sure item is a website.
        search_result = bool(re.search(r"\.com|\.org|\.edu|\.net", website, re.IGNORECASE))
        
        # Check to see if any white spaces are in the string.
        white_space_result = bool(re.fullmatch(r'\S*', website))
        
        results = [search_result, white_space_result]
        
        return all(results)