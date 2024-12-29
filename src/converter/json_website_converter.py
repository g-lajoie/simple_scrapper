# Imports
import re
import json
from typing import List, Dict, Tuple

from converter.website_converter import IWebsiteConverter
# End Imports


class JsonWebsiteConverter(IWebsiteConverter):
    
    def __init__(self, json_file_path:str):
        self.__file_data = self.load_json_file(json_file_path)
        
    def create_website_list(self):
        """ Return a list of websites."""
        
        return self.__file_data['websites']
        
        
    def load_json_file(self, json_file_path:str) -> Dict[str, List[str]]:
        """ Given a file_path to a JSON file, load the JSON file and return a python dict of the data.

        Args:
            json_file_path (_type_): A file path that leads to JSON Data.

        Returns:
            Dict[str, List[str]]: Return a dictionary of the JSON data.
        """
        # Loads the JSON File.
        with open(json_file_path, 'r') as file:
            file_data = json.load(file)
        
        # Checks the structure and content of the JSON File. 
        validation_checks = [
            self.__validate_website_key(file_data),
            self.__website_presence_check(file_data)
            ]          
        
        for check, message in validation_checks:
            if check:
                continue
            
            else:
                file_data = None
                raise Exception(message)
            
        return file_data
        
    def __validate_website_key(self, file_data:str) -> Tuple[bool, str]:
        """ Validates if necessary websites key exists.

        Returns:
            (None, None): If file_data is not present
            (True, None): If all validation check pass.)
            (False, error_message): If at least one validation check fails
        """
        
        # Return None if file data does not exist.
        if not file_data:
            return None, None
        
        # Checks to see if necessary keys exists.
        if "websites" not in file_data:
            error_message = "Issue with JSON structure, websites key is missing"
            return False, error_message
        
        return True, None
        
    def __website_presence_check(self, file_data:str) -> bool:
        """ Validates if data contains websites.
        
        Raises:
            TypeError: If values in dict is not list.

        Returns:
            (None, None): If file_data is not present
            (True, None): If all validation check pass.)
            (False, error_message): If at least one validation check fails
        """

        # Return None if file data does not exist.
        if not file_data:
            return None, None
        
        # Get the list of websites
        websites = file_data.values() 
        
        if not isinstance(websites, list):
            raise TypeError(f"Expected type:List got type:{type(websites)}")
        
        # Check top level domain to make sure item is a website.
        search_result = bool(re.search(r"\.com|\.org|\.edu|\.net", websites, re.IGNORECASE))
        
        # Check to see if any white spaces are in the string.
        white_space_result = bool(re.fullmatch(r'\S*', websites))
        
        # Complies all check in a List       
        results = [search_result, white_space_result]
        
        # Error Message. 
        error_message = "Issue with website data"
        
        # Return True if all test pass.
        if not all(results):
            return False, error_message
        
        else:
            return True, None