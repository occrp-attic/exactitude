import unittest

from exactitude import languages


class LanguagesTest(unittest.TestCase):

    def test_language_codes(self):
        self.assertTrue(languages.validate('de'))
        self.assertTrue(languages.validate('en'))
        self.assertFalse(languages.validate('us'))
        self.assertFalse(languages.validate(None))
