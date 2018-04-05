from __future__ import unicode_literals

import socket
from normality import stringify

from exactitude.common import ExactitudeType


class Ipv4Type(ExactitudeType):

    def validate(self, ipv4, **kwargs):
        """Check to see if this is a valid ipv4 address."""
        ipv4 = stringify(ipv4)
        if ipv4 is None:
            return False
        try:
            socket.inet_pton(socket.AF_INET, ipv4)
            return True
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(ipv4)
            except socket.error:
                return False
            return ipv4.count('.') == 3
        except socket.error:  # not a valid address
            return False
