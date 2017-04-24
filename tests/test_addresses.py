import unittest

from dalet import clean_address

UK = """43 Duke Street
Edinburgh
EH6 8HH"""


class AddressesTest(unittest.TestCase):

    def test_clean(self):
        self.assertEqual(clean_address(UK),
                         '43 DUKE STREET, EDINBURGH, EH6 8HH')
        self.assertEqual(clean_address('huhu\n   haha'), 'HUHU, HAHA')
        self.assertEqual(clean_address('huhu,\n haha'), 'HUHU, HAHA')

    def test_clean_fail_country(self):
        self.assertEqual(clean_address('Germany'), None)
        self.assertEqual(clean_address('New York'), None)
