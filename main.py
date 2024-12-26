import time
import httpx
from url_filterer import URLFilterer
from url_parser import UrlParser
from crawler import Crawler

async def main():
    filterer = URLFilterer(
        allowed_domains = {"mcoding.io"},
        allowed_schemes = {"http", "https"},
        allowed_filetypes = {".html", ".php", ""}
    )
    
    start = time.perf_counter()
    async with httpx.AsyncClient() as client:
        crawler = Crawler(
            client = client,
            url = ['http://mcoding.io/'],
            filter_url = filterer.filter_url,
            worker = 5,
            limit = 30
        )

        await crawler.run()

    end = time.perf_counter()

    seen = sorted(crawler.seen)
    print("Results:")
    for url in seen:
        print(url)

    print(f"Crawled: {len(crawler.done)} URLs")
    print(f"Found: {len(seen)} URLs")
    print(f"Done in {end - start:.2f}s")

if __name__ == "__main__":
    asyncio.run(main(), debug = True)