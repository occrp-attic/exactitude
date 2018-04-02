from __future__ import unicode_literals

import re
import socket
from normality import stringify
from normality.cleaning import strip_quotes

from exactitude.common import ExactitudeType
from exactitude.domain import DomainType


class Ipv4Type(ExactitudeType):
    IPV4_REGEX = re.compile(r'(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'+'(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')
    domains = DomainType()

    def validate(self, ipv4, **kwargs):
        """Check to see if this is a valid ipv4 address."""
        ipv4 = stringify(ipv4)
        if ipv4 is None:
            return
        if not self.IPV4_REGEX.match(ipv4):
            return False
        try:
            socket.inet_pton(socket.AF_INET, ipv4)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(ipv4)
            except socket.error:
                return False
            return ipv4.count('.') == 3
        except socket.error:  # not a valid address
            return False

        print ('iv4 exactitude verification running')

        return True

    def clean(self, text, **kwargs):
        """Create a more clean, but still user-facing version of an
        instance of the type."""
        text = stringify(text)
        if text is not None:
            return self.clean_text(text, **kwargs)

    def clean_text(self, text, **kwargs):
        return text
