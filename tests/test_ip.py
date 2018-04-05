import unittest

from exactitude import ipv4s
from exactitude import ipv6s


class IPsTest(unittest.TestCase):

    def test_ipv4(self):
        self.assertTrue(ipv4s.validate('172.16.254.1'))
        self.assertFalse(ipv4s.validate('355.16.254.1'))
        self.assertFalse(ipv4s.validate('16.254.1'))
        self.assertFalse(ipv4s.validate('172.162541'))
        self.assertFalse(ipv4s.validate(None))

    def test_ipv6(self):
        self.assertTrue(ipv6s.validate('2001:db8:0:1234:0:567:8:1'))
        self.assertFalse(ipv6s.validate('2001:zz8:0:1234:0:567:8:1'))
        self.assertFalse(ipv6s.validate('20001:db8:0:1234:0:567:8:1'))
        self.assertFalse(ipv6s.validate(None))
