# Imports
import time
import asyncio
import httpx
import json
from typing import Iterable

from crawler import Crawler
# End Imports

async def main():
    
    with open('websites.json', 'r') as json_file:
        websites = json.load(json_file)    
    
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
    print(f"Done in {end - start:.2f}s")

if __name__ == "__main__":
    asyncio.run(main(), debug = True)