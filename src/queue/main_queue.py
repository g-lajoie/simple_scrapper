# Imports
import asyncio
from typing import List
from src.serializer import Deserializer

# End Imports

class MainQueue(asyncio.Queue):
    
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        """ Checks to see if class is already created. If already created, return same instance of the class."""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
    
        return cls.__instance
    
    def __init__(self, deserializer:Deserializer):
        if not hasattr(self, "_intialized"):
            super().__init__()
            self._intialized = True
        
        self.website_list = deserializer.create_website_list()
            
    async def put_websites(self, website:List[str] | str = None):
        """ Inserts a website(of type str) or websites (of type list) into the queue"""
        if website is None:
            website = self.website_list

        if not isinstance(website, (list, str)):
            return TypeError(f"Expected list or str, instead got {type(website)}")

        website_type = type(website)

        if website_type is list:
            for item in list:
                super().put(item)

        if website_type is str:
            super().put(website)
