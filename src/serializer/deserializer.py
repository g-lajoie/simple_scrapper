# Imports
from typing import List, Dict, Protocol, runtime_checkable

# End Imports

@runtime_checkable
class Deserializer(Protocol):
    
    website:List # A list of websites that.
    
    def _create_website_list():
        """ Return List[str] each containing valid websites """
        