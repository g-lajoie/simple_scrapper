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
    # Define data and create instance of MainQueue
    websites = ["example1.com", "example2.org", "example3.com"]
    MQ = main_queue
    
    # Execute Function
    await MQ.insert_website_list(websites)
    
    # Extract the contents from the queue
    contents = []
    while not MQ.empty():
        contents.append(await MQ.get())
    
    # Test Results
    assert contents == websites
    
@pytest.mark.asyncio
async def test_insert_website(main_queue):
    # Define data and create instance of MainQueue
    website = "example1.com"
    MQ = main_queue
    
    # Execute Function
    await MQ.insert_website(website)
    
    # Extract the content from the queue
    contents = []
    while not MQ.empty():
        contents.append(await MQ.get())
        
    # Test Results
    assert contents == [website]