import unittest

from dalet import parse_phone


class PhonesTest(unittest.TestCase):

    def test_us_number(self):
        self.assertEqual(parse_phone('+1-800-784-2433'), '+1800-784-2433')
        self.assertEqual(parse_phone('+1 800 784 2433'), '+1800-784-2433')
        self.assertEqual(parse_phone('+18007842433'), '+1800-784-2433')
        self.assertEqual(parse_phone('+1 555 8379'), None)

    def test_de_number(self):
        self.assertEqual(parse_phone('017623423980'), None)
        self.assertEqual(parse_phone('017623423980', country='DE'),
                         '+4917623423980')
