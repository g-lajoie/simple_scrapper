# Imports
import urllib
import pathlib
# End Imporst

class URLFilterer:
    def __init__(
        self,
        allowed_domains:set[str] | None = None,
        allowed_schemas:set[str] | None = None,
        allowed_filetypes:set[str] | None = None
    ):
        self.allowed_domains = allowed_domains
        self.allowed_schemas = allowed_schemas
        self.allowed_filetypes = allowed_filetypes
        
    def filter_url(self, base:str, url:str) -> str | None:
        url = urllib.parse.urljoin(base, url)
        url, _frag = urllib.parse.urldefrag(url)
        parsed = urllib.parse.urlparse(url)
        
        if (self.allowed_schemas is not None
                and parsed.schemea not in self.allowed_schemes):
            return None
        
        ext = pathlib.Path(parsed.path).suffix
        
        if (self.allowed_filetypes is not None
                and ext not in self.allowed_filetypes):
            return None
        
        return url