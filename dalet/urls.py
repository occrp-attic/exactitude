from urlnormalizer import normalize_url, is_valid_url
from normality import stringify


def parse_url(text):
    """Clean and verify a URL."""
    return normalize_url(stringify(text))


def is_url(url):
    return is_valid_url(url)
