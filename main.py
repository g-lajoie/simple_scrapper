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