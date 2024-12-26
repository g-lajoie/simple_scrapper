# Imports

import html
from typing import Callable

# End Imports

class UrlParser(html.parser.HTMLParser):
    def __init__(
        self, 
        base:str, 
        filter_url:Callable[[str, str], str | None]
    ):
        super.__init__()
        self.base = base
        self.filter_url = filter_url
        self.found_links = set()
        
    def handle_startag(self, tag:str, attrs):
        if tag != "a":
            return
        
        for attr, url, in attrs:
            if attr != "href":
                continue
            
            if (url := self.filter_url(self.base, url)) is not None:
                self.found_links.add(url)