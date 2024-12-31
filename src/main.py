# Imports
import asyncio
import httpx
from typing import Iterable

from queue import MainQueue
from serializer import JSONDeserializer
from scraper import Scraper

# End Imports


async def main(num_workers = 3):
    
    # Get website data.
    websites = JSONDeserializer('websites.json')

    # Intializes Main Queue.
    main_queue = MainQueue() 
    
    # Add websites into Queue.
    insert_website = asyncio.create_task(main_queue.put_websites(websites))
    
    async def scrape_website():
        while True:
            # Get the next item from main_queue
            website_from_queue = await main_queue.get()

            # Scape the data
            if website_from_queue is None:
                # Sentinel value is receieved, exiting the loop.
                main_queue.task_done()
                break

            try:
                scraper = Scraper(website_from_queue)
                results = await scraper.scrape()
                return results

            finally:
                main_queue.task_done()
                
    # Create Tasks to Consumer Website from Queue
    workers = [scrape_website for _ in range(num_workers)]
        
    # Ensure all websites have been inserted
    await insert_website

    # Ensure that all websites have been scraped.
    await asyncio.gather(*workers, return_exceptions=True)

    # Add sentinel values to exit.
    for _ in range(num_workers):
        await main_queue.put(None)
    
    # Wait until all items of the Queeu have been consumed
    await asyncio.gather(*workers, return_exceptions = True)

if __name__ == "__main__":
    asyncio.run(main(), debug = True)