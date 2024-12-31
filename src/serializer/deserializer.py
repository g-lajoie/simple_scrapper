# Imports
from typing import Dict, Protocol, runtime_checkable

# End Imports

@runtime_checkable
class Deserializer(Protocol):
    
    def create_website_list():
        """ Return List[str] each containing valid websites """
        