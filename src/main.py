# Imports
import asyncio
import logging
import sys

from main_queue import MainQueue
from serializer import JSONDeserializer
from scraper import StandardScraper

# End Imports


async def main(num_workers = 3):
    
    # Configure Root Logger
    logging.basicConfig(
        level = logging.INFO, 
        format = '%(asctime)s - %(levelname)s - %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S'
    )
    
    # Get website data.
    logging.info("Retreiving websites from JSON File")
    website_deserializer = JSONDeserializer('websites.json')

    # Intializes Main Queue.
    main_queue = MainQueue(website_deserializer) 
    
    # Add websites into Queue.
    logging.info("Adding items to Main Queue")
    insert_website = asyncio.create_task(main_queue.put_websites())

    # Define Results List
    results = {}

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
                scraper = StandardScraper(website_from_queue)
                results[website_from_queue] = scraper.scrape()

            finally:
                main_queue.task_done()
                
    # Create Tasks to Consumer Website from Queue
    logging.info("Started Scraping Websites")
    try:
        workers = [asyncio.create_task(scrape_website()) for _ in range(num_workers)]
    
    except:
        logging.error('An Error Occured')
        sys.exit(1)        
        
    # Ensure all websites have been inserted
    await insert_website
    logging.info("All items have been added to Main Queue")

    # Add sentinel values to exit.
    for _ in range(num_workers):
        await main_queue.put(None)
    
    # Ensure that all websites have been scraped.
    await main_queue.join()
    logging.info("All websites have been scrapped")

    # Wait until all items of the Queeu have been consumed
    await asyncio.gather(*workers)

    # Export results data
    print(results)
    
if __name__ == "__main__":
    asyncio.run(main(), debug = True)