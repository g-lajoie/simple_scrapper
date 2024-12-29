# Imports
from abc import ABC, abstractmethod
from typing import Dict

# End Imports

class IWebsiteConverter:
    
    @abstractmethod
    def create_website():
        "Implement create list method in child class"
        