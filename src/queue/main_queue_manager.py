# Imports
from src.serializer import Deserializer
from typing import Dict, Any, List

# End Imports

# Type Aliases
JSON = Dict[str, Any]

# Implementation
class MainQueueManager():
    def __init__(self, deserializer:Deserializer):
        self.websites:List = []
        self.deserializer = deserializer
            
    def get_websites(self):       
        return self.deserializer.create_website_list()
    
    def insert_into_websites(self, type:str, path:str = None):
        # Enforce format for type parameter.
        type = type.lower()
        
        # Add websites to websites list
        if type == 'json' and path is not None:
            self.websites.extend(JsonWebsiteConverter(path).create_website_list())
    
    
        
        
    
        