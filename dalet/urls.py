from urltools import normalize
from normality import stringify
from six.moves.urllib.parse import urldefrag


def parse_url(text):
    """Clean and verify a URL."""
    # TODO: learn from https://github.com/hypothesis/h/blob/master/h/api/uri.py
    url = stringify(text)
    if url is None:
        return
    if url.startswith('//'):
        url = 'http:' + url
    try:
        norm_url = normalize(url)
        norm_url, _ = urldefrag(norm_url)
        if '://' in norm_url:
            return norm_url
    except:
        return


def is_url(url):
    return parse_url(url) is not None
