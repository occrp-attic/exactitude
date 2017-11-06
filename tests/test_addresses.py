import unittest

from exactitude import addresses

UK = """43 Duke Street
Edinburgh
EH6 8HH"""


class AddressesTest(unittest.TestCase):

    def test_clean(self):
        self.assertEqual(addresses.clean(UK),
                         '43 Duke Street, Edinburgh, EH6 8HH')
        self.assertEqual(addresses.clean('huhu\n   haha'), 'huhu, haha')
        self.assertEqual(addresses.clean('huhu,\n haha'), 'huhu, haha')
