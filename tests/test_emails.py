import unittest

from exactitude import emails


class EmailsTest(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(emails.clean('foo@pudo.org'), 'foo@pudo.org')
        self.assertEqual(emails.clean('pudo.org'), None)
        self.assertEqual(emails.clean(None), None)
        self.assertEqual(emails.clean(5), None)

        # self.assertEqual(parse_email('foo@PUDO.org'), 'foo@pudo.org')
        # self.assertEqual(parse_email('FOO@PUDO.org'), 'foo@pudo.org')
