from urlnorm import norm
from normality import stringify
from urlparse import urldefrag

from dalet.validate import format_checker


def parse_url(text):
    """Clean and verify a URL."""
    # TODO: learn from https://github.com/hypothesis/h/blob/master/h/api/uri.py
    url = stringify(text)
    if url is None:
        return
    if url.startswith('//'):
        url = 'http:' + url
    elif '://' not in url:
        url = 'http://' + url
    try:
        norm_url = norm(url)
        norm_url, _ = urldefrag(norm_url)
        return norm_url
    except:
        return


@format_checker.checks('url')
def is_url(url):
    return parse_url(url) is not None
