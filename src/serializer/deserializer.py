# Imports
from typing import Dict, Protocol

# End Imports


class Deserializer(Protocol):
    
    def create_website_list():
        """ Return List[str] each containing valid websites """

    def from_json(self, json_path:str):
        """ Add websites from json into self.websites attribute"""
        return self.insert_into_websites('json', path = json_path)
        