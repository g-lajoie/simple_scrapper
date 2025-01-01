# Imports
import asyncio
from typing import List
from serializer import Deserializer

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
        
        self._websites = deserializer._create_website_list()
            
    async def put_websites(self):
        """ Inserts a website(type:List[str]) or websites (type:str) into the queue"""

        # Define Website Type
        website_type = type(self._websites)
        
        # Raise Error for Wrong Type
        if not isinstance(self._websites, (list, str)):
            raise TypeError(f"Expected list or str, instead got {type(website_type)}")

        # Add item(s) to the Queue
        if website_type is list:
            for item in self._websites:
                await super().put(item)

        if website_type is str:
            await super().put(self._websites)
