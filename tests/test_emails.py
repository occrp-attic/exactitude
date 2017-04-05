import unittest

from dalet import parse_email


class EmailsTest(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(parse_email('foo@pudo.org'), 'foo@pudo.org')
        self.assertEqual(parse_email('pudo.org'), None)
        self.assertEqual(parse_email(None), None)
        self.assertEqual(parse_email(5), None)

        self.assertEqual(parse_email('foo@PUDO.org'), 'foo@pudo.org')
        self.assertEqual(parse_email('FOO@PUDO.org'), 'foo@pudo.org')
