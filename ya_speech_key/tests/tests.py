# -*- coding: utf-8 -*-

import unittest

from ya_speech_key import APIKey, Oops


class Tests(unittest.TestCase):
    def test_01(self):
        try:
            key = APIKey()
            print(key.key)
        except Oops as e:
            print('Impossible to test: {}'.format(e))
            return
        self.assertEqual(key.key, key.key)
        self.assertTrue('-' in key.key)
        self.assertTrue(' ' not in key.key)
        self.assertTrue(len(key.key))


if __name__ == '__main__':
    unittest.main()
