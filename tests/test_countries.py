import unittest

from dalet import parse_country, is_country_code


class CountriesTest(unittest.TestCase):

    def test_country_codes(self):
        self.assertEqual(parse_country('DE'), 'de')
        self.assertTrue(is_country_code('DE'))
        self.assertFalse(is_country_code('DEU'))
        self.assertFalse(is_country_code('SU'))
        self.assertTrue(is_country_code('XK'))
        self.assertTrue(is_country_code('EU'))

    def test_country_names(self):
        self.assertEqual(parse_country(None), None)
        self.assertEqual(parse_country('Takatukaland', guess=False), None)
        self.assertEqual(parse_country('Germany'), 'de')
        self.assertEqual(parse_country('Germani'), 'de')
        self.assertEqual(parse_country('Soviet Union'), 'suhh')
