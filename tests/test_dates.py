import unittest

from dalet import parse_date, is_partial_date


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
