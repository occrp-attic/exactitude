import unittest

from exactitude import ibans


class IbansTest(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(ibans.clean('GB29 NWBK 6016 1331 9268 19'),
                         'GB29NWBK60161331926819')

    def test_domain_validity(self):
        self.assertTrue(ibans.validate('GB29 NWBK 6016 1331 9268 19'))
        self.assertTrue(ibans.validate('GB29NWBK60161331926819'))
        self.assertFalse(ibans.validate('GB28 NWBK 6016 1331 9268 19'))
        self.assertFalse(ibans.validate('GB29NWBKN0161331926819'))
        self.assertFalse(ibans.validate(None))
