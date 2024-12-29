# Imports
import asyncio
import httpx
from typing import Iterable

from crawler import Crawler
from main_queue import MainQueue
from utils.get_websites import GetWebsites

# End Imports


async def main():
    
    # Intializes Main Queue.
    Queue = MainQueue() 
    
    # Get website data.
    websites = GetWebsites()
    websites.from_json('websites.json')
    
    # Add websites into Queue.
    insert_website = asyncio.create_task(Queue.insert_website_list(websites.websites))
    
    # Get website from queue
    async def website_consumer():
        while True:
            website = await Queue.get()
            try:
                print(website)
            finally:
                Queue.task_done()
                
    # Create Tasks to Consumer Website from Queue
    num_wokers = 3
    workers = [asyncio.create_task(website_consumer()) for _ in num_wokers]
        
    # Ensure all websites have been inserted
    await insert_website
    
    # Wait until all items of the Queeu have been consumed
    await Queue.join()
    
    # Cancled Remaining workers
    _ = [worker.cancel() for worker in workers]
    
    # Wait for workers to handle cancellation
    await asyncio.gather(*workers, return_exceptions = True)    

if __name__ == "__main__":
    asyncio.run(main(), debug = True)