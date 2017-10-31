import unittest

from dalet import parse_url, is_url


class UrlsTest(unittest.TestCase):

    def test_is_url(self):
        self.assertTrue(is_url('http://foo.org'))
        self.assertFalse(is_url(None))
        self.assertFalse(is_url('hello'))

    def test_parse_url(self):
        self.assertEqual(parse_url('http://foo.com'), 'http://foo.com/')
        self.assertEqual(parse_url('http://foo.com/#lala'), 'http://foo.com/')

        self.assertEqual(parse_url('http://foo.com?b=1&a=2'),
                         'http://foo.com/?a=2&b=1')
        self.assertEqual(parse_url('http://FOO.com'), 'http://foo.com/')
        self.assertEqual(parse_url('http://FOO.com/A'), 'http://foo.com/A')
