import unittest

from exactitude import ipv4s
from exactitude import ipv6s



class IPsTest(unittest.TestCase):

    # def test_parse(self):
    #     self.assertEqual(emails.clean('foo@pudo.org'), 'foo@pudo.org')
    #     self.assertEqual(emails.clean('"foo@pudo.org"'), 'foo@pudo.org')
    #     self.assertEqual(emails.clean('pudo.org'), None)
    #     self.assertEqual(emails.clean(None), None)
    #     self.assertEqual(emails.clean(5), None)
    #     self.assertEqual(emails.clean('foo@PUDO.org'), 'foo@pudo.org')
    #     self.assertEqual(emails.clean('FOO@PUDO.org'), 'FOO@pudo.org')
    #
    # def test_normalize(self):
    #     self.assertEqual(emails.normalize('FOO@PUDO'), [])
    #     self.assertEqual(emails.normalize('FOO@PUDO.org'), ['foo@pudo.org'])

    def test_domain_validity(self):
        self.assertTrue(ipv4s.validate('172.16.254.1'))
        self.assertFalse(ipv4s.validate('355.16.254.1'))
        self.assertFalse(ipv4s.validate('16.254.1'))
        self.assertFalse(ipv4s.validate('172.162541'))
        self.assertFalse(ipv4s.validate(None))
        self.assertTrue(ipv6s.validate('2001:db8:0:1234:0:567:8:1'))
        self.assertFalse(ipv6s.validate('2001:zz8:0:1234:0:567:8:1'))
        self.assertFalse(ipv6s.validate('20001:db8:0:1234:0:567:8:1'))
        self.assertFalse(ipv6s.validate(None))
