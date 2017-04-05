import unittest

from dalet import is_language_code


class LanguagesTest(unittest.TestCase):

    def test_language_codes(self):
        self.assertTrue(is_language_code('de'))
        self.assertTrue(is_language_code('en'))
        self.assertFalse(is_language_code('us'))
        self.assertFalse(is_language_code(None))
