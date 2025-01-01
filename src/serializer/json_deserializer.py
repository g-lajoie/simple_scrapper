# Imports
import re
import json
from typing import List, Dict, Tuple

from utils import valid_top_level_domains
# End Imports


class JSONDeserializer:
    def __init__(self, json_file_path:str, filter_websites:bool = False):
        self.filter_websites = filter_websites
        self.file_data = self.load_json_file(json_file_path)
        
    def load_json_file(self, json_file_path:str) -> Dict[str, List[str]]:
        """ Return a dictionary from JSON"""
        # Loads the JSON File.
        with open(json_file_path, 'r') as file:
            file_data = json.load(file)
        
        return file_data
            
    def _create_website_list(self) -> List[str]:
        """ Given a file_path to a JSON file, load the JSON file and return a list of websites. """
        
        # Check the JSON structure.
        if self.__validate_website_key(necessary_key = 'websites'):
            pass
        
        # Check website list in JSON.
        if self.__validate_domain():
            pass
            
        return self.file_data['websites']
        
    def __validate_website_key(self, necessary_key:str, file_data:dict = None) -> Tuple[bool, str]:
        """ Validates if necessary websites key exists.

        Raises:
            TypeError: If website key not in file_data dictionary. 
            
        Returns:
            True: If validation check pass.
        """
        # Default file_data to self parameter
        if file_data is None:
            file_data = self.file_data
        
        # Checks to see if necessary keys exists.
        if necessary_key not in file_data:
            raise KeyError("Issue with JSON structure, websites key is missing")
        
        return True
    
    def __validate_domain(self, file_data:dict = None) -> Tuple[bool, str]:
        """ Validates if all domain checks pass. """
        
        # Default file_data to self parameter
        if file_data is None:
            file_data = self.file_data
        
        # Get the list of websites
        websites = file_data['websites']
        
        if not isinstance(websites, list):
            raise TypeError(f"Expected type:List got type:{type(websites)}")
        
        domain_validators = [
            self.__validate_top_level_domain(websites)]
        
        if all(domain_validators):
            return True            
        
    def __validate_top_level_domain(self, website_list:List[str]) -> bool:
        """ Validates if valid top level domain exits is given.

        Raises:
            
            
        Returns:
            True: If validation check pass.
            False: If validaiton check fail
            
            List[str]: If filter website is True.
        """
        
        # Obtain a list of valid top level domains and define pattern.
        tld_list = [rf"\{tld}$" for tld in valid_top_level_domains()]
        
        # Define the returned re.search list.
        checked_websites = []

        for tld_pattern in tld_list:
            for website in website_list:
                checked_websites.append(re.search(tld_pattern, website, re.IGNORECASE))

        # If all websites fail the check.
        if not checked_websites:
            raise Exception("All websites failed check, check to make sure website contain top level domains")
        
        # If some websites fail the check.
        """ If self.filter_websites set to True then will return only websites that pass check, else fails """
        
        if not set(checked_websites).issubset(website_list):
            if self.filter_websites == True:
                self.file_data['websites'] = checked_websites
            
            else:
                return False
            
        if set(checked_websites).issubset(website_list):
            return True