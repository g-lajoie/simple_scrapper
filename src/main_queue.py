# Imports
import asyncio
from typing import List

# End Imports

class MainQueue(asyncio.Queue):
    
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        """ Checks to see if class is already created. If already created, return same instance of the class."""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
    
        return cls.__instance
    
    def __init__(self):
        if not hasattr(self, "_intialized"):
            super().__init__()
            self._intialized = True
            
    async def insert_website_list(website_list:List[str]):
        """ Inserts a list of website into the main queue"""
        _ = [super().put(item) for item in website_list]
    
    async def insert_website(website:str):
        """ Insert a single website into the main queue."""
        super().put(website)