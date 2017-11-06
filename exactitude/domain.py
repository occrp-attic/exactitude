# import socket
from six.moves.urllib.parse import urlparse

from exactitude.common import ExactitudeType


class DomainType(ExactitudeType):
    # TODO: https://pypi.python.org/pypi/publicsuffix/

    # def _check_exists(self, domain):
    #     """Actually try to resolve a domain name."""
    #     try:
    #         domain = domain.encode('idna').lower()
    #         socket.getaddrinfo(domain, None)
    #         return True
    #     except:
    #         return False

    def clean_text(self, domain, **kwargs):
        """Try to extract only the domain bit from the """
        try:
            # handle URLs by extracting the domain name
            domain = urlparse(domain).hostname or domain
            domain = domain.lower()
            # get rid of port specs
            domain = domain.rsplit(':', 1)[0]
            domain = domain.rstrip('.')
            # handle unicode
            domain = domain.encode("idna")
        except ValueError:
            return None
        return domain
