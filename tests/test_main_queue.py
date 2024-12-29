# Imports
import pytest
import asyncio
from src.main_queue import MainQueue

# End Imports

   
@pytest.fixture()
def main_queue():
    """ Fixture for MainQueue """
    return MainQueue()


@pytest.mark.asyncio
async def test_insert_website_list(main_queue):
    data_list = ['a', 'b', 'c']
    
    await main_queue.insert_website_list(data_list)
    
    # Extract the contents from the queue
    contents = []
    while not main_queue.empty():
        contents.append(await main_queue.get())
        
    assert contents == data_list