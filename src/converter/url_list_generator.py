# Imports
from .json_website_converter import JsonWebsiteConverter
from typing import Dict, Any

# End Imports

# Create Type Alias
JSON = Dict[str, Any]

class UrlListGenerator():
    
    def __init__(self):
        self.from_json:JSON | None = None
        
    def get_websites(self):
        """Generates the websites according to which attribute is used"""
        
        if self.from_json is not None:
            return JsonWebsiteConverter().create_websites()