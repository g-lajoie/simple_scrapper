# Imports
import asyncio
import httpx
from typing import Iterable

from src.crawler import Crawler
from src.main_queue import MainQueue
from src.utils.get_websites import GetWebsites

# End Imports

async def main():
    
    # Intializes Main Queue.
    Queue = MainQueue() 
    
    # Get website data.
    website_getter = GetWebsites()
    websites = website_getter.from_json("websites.json")
    
    # Add websites into Queue.
    insert_website = asyncio.create_task(Queue.insert_website_list(websites))
    
    
    async with httpx.AsyncClient() as client:
        crawler = Crawler(
            client = client,
            urls = websites,
            workers = 5,
            limit = 30
        )

        await crawler.run()

    seen = sorted(crawler.seen)
    
    print("Results:")
    for url in seen:
        print(url)

    print(f"Crawled: {len(crawler.done)} URLs")
    print(f"Found: {len(seen)} URLs")

if __name__ == "__main__":
    asyncio.run(main(), debug = True)