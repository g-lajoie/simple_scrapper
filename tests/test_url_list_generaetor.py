# Imports
import pytest
from src.utils import UrlListGenerator

# End Imports

class TestUrlListGenerator:

    @pytest.fixture
    def url_list_generator(self):
        """Fixture for creating UrlListGenerator Instances"""        
        return UrlListGenerator()
    
    @pytest.mark.parametrize("from_json_value, expected",[
        (None, None)    
    ])
    def test_from_json(self, url_list_generator, from_json_value, expected):
        """Test the .from_json attribute"""
        
        # Set the attribute
        url_list_generator.from_json = from_json_value
        
        # Assert the attribute value
        assert url_list_generator.from_json == expected
        
    def test_create_website_from_json(self, url_list_generator):
        assert isinstance(url_list_generator.get_websites(), list)