# Imports
from typing import List, Protocol, runtime_checkable

# End Imports

@runtime_checkable
class WensiteScraper(Protocol):
    
   async def scrape():
       """ Return a dictionary that has content from the webstie that we are scraping"""
