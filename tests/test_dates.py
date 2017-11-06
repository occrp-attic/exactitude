# -*- coding: utf-8 -*-
import unittest
from datetime import datetime

from exactitude import dates


class DatesTest(unittest.TestCase):

    def test_is_partial_date(self):
        self.assertTrue(dates.validate('2017-04-04'))
        self.assertTrue(dates.validate('2017-4-4'))
        self.assertTrue(dates.validate('2017-4'))
        self.assertTrue(dates.validate('2017'))
        self.assertFalse(dates.validate('0017'))
        self.assertFalse(dates.validate(None))
        self.assertFalse(dates.validate(5))
        self.assertFalse(dates.validate('2017-20-01'))

    def test_parse_date(self):
        self.assertEquals(dates.clean('2017-04-04'), '2017-04-04')
        # self.assertEquals(parse_date('2017-4-4'), '2017-04-04')

        # TODO: make this yield an imprecise date somehow?
        self.assertEquals(dates.clean('4/2017', format="%m/%Y"),
                          '2017-04-01')

    def test_guess_date(self):
        self.assertEquals(dates.clean('12.4.2017'), '2017-04-12')

    def test_fuzzy_date_parser_failure(self):
        with self.assertRaisesRegexp(Exception, 'Failed to parse the string.'):
            dates.fuzzy_date_parser('nothing')

    def test_fuzzy_date_parser_success_english(self):
        result = dates.fuzzy_date_parser('15 march, 1987')

        self.assertIsInstance(result, datetime)
        self.assertEqual(result.strftime('%x'), '03/15/87')

    def test_fuzzy_date_parser_success_german(self):
        result = dates.fuzzy_date_parser(u'15. März 1987')

        self.assertIsInstance(result, datetime)
        self.assertEqual(result.strftime('%x'), '03/15/87')

    def test_fuzzy_date_parser_success_spanish(self):
        result = dates.fuzzy_date_parser(u'15 Marzo 1987')

        self.assertIsInstance(result, datetime)
        self.assertEqual(result.strftime('%x'), '03/15/87')
