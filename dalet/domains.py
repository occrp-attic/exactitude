import socket
from normality import stringify
from urlparse import urlparse


def is_domain(domain):
    """Validate an IDN compatible domain."""
    domain = stringify(domain)
    if domain is None:
        return False
    try:
        domain = domain.encode('idna').lower()
        socket.getaddrinfo(domain, None)
        return True
    except:
        return False


def parse_domain(text):
    """Extract a domain name from a piece of text."""
    domain = stringify(text)
    if domain is None:
        return
    try:
        domain = urlparse(domain).hostname or domain
    except ValueError:
        pass

    if '@' in domain:
        _, domain = domain.rsplit('@', 1)
    domain = domain.lower()
    if domain.startswith('www.'):
        domain = domain[len('www.'):]
    domain = domain.strip('.')
    if is_domain(domain):
        return domain
