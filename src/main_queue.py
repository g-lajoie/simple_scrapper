# Imports
import asyncio

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