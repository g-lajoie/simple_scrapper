# Imports
from converter.json_website_converter import JsonWebsiteConverter
from typing import Dict, Any, List

# End Imports

# Type Aliases
JSON = Dict[str, Any]

# Implementation
class GetWebsites():
    def __init__(self):
        self.websites:List = []
            
    def get_websites(self):       
        return self.webstites
    
    def from_json(self, json_path:str):
        """ Add websites from json into self.websites attribute"""
        return self.insert_into_websites('json', path = json_path)
    
    def insert_into_websites(self, type:str, path:str = None):
        # Enforce format for type parameter.
        type = type.lower()
        
        # Add websites to websites list
        if type == 'json' and path is not None:
            self.websites.extend(JsonWebsiteConverter(path).create_website_list())
    
    
        
        
    
        