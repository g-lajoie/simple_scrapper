# Imports
import asyncio
import httpx
from typing import Iterable

from queue import MainQueue, MainQueueManager
from scraper import Scraper

# End Imports


async def main():
    
    # Get website data.
    websites = MainQueueManager().from_json('websites.json')

    # Intializes Main Queue.
    Queue = MainQueue() 
    
    # Add websites into Queue.
    insert_website = asyncio.create_task(Queue.insert_into_queue(websites))
    
    # Get websites from Queue & Scrape the website
    websites_from_queue = Queue.get_websites()
    Scrape = Scraper(websites_from_queue)
    
    get_website = asyncio.create_task(Queue.get_website())
    
    

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