from abc import ABC, abstractmethod
from urllib.parse import urlparse

class ISerializer(ABC):

    @abstractmethod
    def url_information(self):
        "Return URL Information"

    @abstractmethod
    @property
    def url(self):
        "url attribute"
    
class UrlSerializer:

    def ___init__(self, url):
        self.url = url

    @property
    def url(self):
        return self.url
    
    def parse_url(self):
        parse_result = urlparse(self.url)
        
        return {
            "scheme": parse_result.scheme,
            "netloc": parse_result.netloc,
            "path": parse_result.path,
            "hostname": parse_result.hostname
        }

    @property
    def hostname(self):
        return self.parse_url(self.url).hostname

    