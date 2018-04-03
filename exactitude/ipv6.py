from __future__ import unicode_literals

import re
import socket
from normality import stringify
from normality.cleaning import strip_quotes

from exactitude.common import ExactitudeType
from exactitude.domain import DomainType


class Ipv6Type(ExactitudeType):
    domains = DomainType()

    def validate(self, ipv6, **kwargs):
        ipv6 = stringify(ipv6)
        if ipv6 is None:
            return False

        try:
            socket.inet_pton(socket.AF_INET6, ipv6)
        except socket.error:  # not a valid address
            return False
        return True
