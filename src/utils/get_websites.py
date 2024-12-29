# Imports
from src.converter.json_website_converter import JsonWebsiteConverter
from typing import Dict, Any

# End Imports

# Type Aliases
JSON = Dict[str, Any]

# Implementation
class GetWebsites():
    
    def __init__(self):
        self.from_json:str | None = None
        
    def get_websites(self):
        """Generates the websites according to which attribute is used"""
        
        if self.from_json is not None:
            return JsonWebsiteConverter(self.from_json).create_websites()
        