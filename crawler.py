# Imports

import httpx
from typing import Iterable, Callable
import asyncio
from url_parser import UrlParser

# End Imports

class Crawler:
    def __init__(
        self,
        client: httpx.AsyncClient,
        urls: Iterable[str],
        filter_url: Callable[[str, str], str | None],
        workers:int = 10,
        limit:int = 25
    ):
        self.client = client
        
        self.start_urls = set(urls)
        self.todo = asyncio.Queue()
        self.seen = set()
        self.done = set()
        
        self.filter_url = filter_url
        self.num_workers = workers
        self.limit = limit
        self.total = 0
        
    async def run(self):
        await self.on_found_links(self.start_urls)
        workers = [
            asyncio.create_task(self.worker()) for _ in range(self.num_workers)
        ]
        await self.todo.join()
        
        for worker in workers:
            worker.cancel()
            
    async def on_found_links(self, urls: set[str]):
        new = urls - self.seen
        self.seen.update(new)
        
        # await save to database or file  here...
        
        for url in new:
            await self.put_todo(url)
            
    async def put_todo(self, url:str):
        if self.total >= self.limit:
            return
        
        self.total += 1
        await self.todo.put(url)
        
    async def worker(self):
        while True:
            try:
                await self.process_one()
            except asyncio.CancelledError:
                return
            
    async def proocess_one(self):
        url = await self.todo.get()
        
        try:
            await self.crawl(url)
        except Exception as e:
            # retry hadingling done
            pass
        finally:
            self.todo.task_done()
    
    async def crawl(self, url:str):
        
        # rate limit here...
        await asyncio.sleep(.1)
        
        response = await self.client.get(url, follow_redirects=True)
        
        found_links = await self.parse_links(
            base=str(response.url),
            text=response.text
        )
        
        await self.on_found_links(found_links)
        
        self.done.add(url)
        
    def parse_links(self, base:str, text:str) -> set[str]:
        parser = UrlParser(base, self.filter_url)
        parser.feed(text)
        return parser.found_task
            
    