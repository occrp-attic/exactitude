# -*- coding: utf-8 -*-
import unittest
from datetime import datetime

from dalet import parse_date, is_partial_date
from dalet.dates import fuzzy_date_parser


class DatesTest(unittest.TestCase):

    def test_is_partial_date(self):
        self.assertTrue(is_partial_date('2017-04-04'))
        self.assertTrue(is_partial_date('2017-4-4'))
        self.assertTrue(is_partial_date('2017-4'))
        self.assertTrue(is_partial_date('2017'))
        self.assertFalse(is_partial_date('0017'))
        self.assertFalse(is_partial_date(None))
        self.assertFalse(is_partial_date(5))
        self.assertFalse(is_partial_date('2017-20-01'))

    def test_parse_date(self):
        self.assertEquals(parse_date('2017-04-04'), '2017-04-04')
        # self.assertEquals(parse_date('2017-4-4'), '2017-04-04')

        # TODO: make this yield an imprecise date somehow?
        self.assertEquals(parse_date('4/2017', date_format="%m/%Y"),
                          '2017-04-01')

    def test_guess_date(self):
        self.assertEquals(parse_date('12/4/2017'),
                          '2017-04-12')

    def test_fuzzy_date_parser_failure(self):
        with self.assertRaisesRegexp(Exception, 'Failed to parse the string.'):
            fuzzy_date_parser('nothing')

    def test_fuzzy_date_parser_success_english(self):
        result = fuzzy_date_parser('15 march, 1987')

        self.assertIsInstance(result, datetime)
        self.assertEqual(result.strftime('%x'), '03/15/87')

    def test_fuzzy_date_parser_success_german(self):
        result = fuzzy_date_parser(u'15. März 1987')

        self.assertIsInstance(result, datetime)
        self.assertEqual(result.strftime('%x'), '03/15/87')

    def test_fuzzy_date_parser_success_spanish(self):
        result = fuzzy_date_parser(u'15 Marzo 1987')

        self.assertIsInstance(result, datetime)
        self.assertEqual(result.strftime('%x'), '03/15/87')
