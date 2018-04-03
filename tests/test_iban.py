import unittest

from exactitude import ibans



class IbansTest(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(ibans.clean('GB29 NWBK 6016 1331 9268 19'), 'GB29NWBK60161331926819')
        # self.assertEqual(ibans.clean('"foo@pudo.org"'), 'foo@pudo.org')
        # self.assertEqual(ibans.clean('pudo.org'), None)
        # self.assertEqual(ibans.clean(None), None)
        # self.assertEqual(ibans.clean(5), None)
        # self.assertEqual(ibans.clean('foo@PUDO.org'), 'foo@pudo.org')
        # self.assertEqual(ibans.clean('FOO@PUDO.org'), 'FOO@pudo.org')

    # def test_normalize(self):
    #     self.assertEqual(emails.normalize('FOO@PUDO'), [])
    #     self.assertEqual(emails.normalize('FOO@PUDO.org'), ['foo@pudo.org'])

    def test_domain_validity(self):
        self.assertTrue(ibans.validate('GB29 NWBK 6016 1331 9268 19'))
        self.assertTrue(ibans.validate('GB29NWBK60161331926819'))
        self.assertFalse(ibans.validate('GB28 NWBK 6016 1331 9268 19'))
        self.assertFalse(ibans.validate('GB29NWBKN0161331926819'))
        self.assertFalse(ibans.validate(None))
        # self.assertTrue(ibans.validate('2001:db8:0:1234:0:567:8:1'))
        # self.assertFalse(ibans.validate('2001:zz8:0:1234:0:567:8:1'))
        # self.assertFalse(ibans.validate('20001:db8:0:1234:0:567:8:1'))
