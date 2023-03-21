import unittest
from palindrome import lps

class TestLPS(unittest.TestCase):
    def test_lps_1(self):
        self.assertEqual(lps('babad'), 'bab')
    def test_lps_2(self):
        self.assertEqual(lps('cbbd'), 'bb')
    def test_lps_3(self):
        self.assertEqual(lps('a'), None)
    def test_lps_4(self):
        self.assertEqual(lps('ac'), None)
    def test_lps_5(self):
        self.assertEqual(lps('bb'), 'bb')
    def test_lps_6(self):
        self.assertEqual(lps('ccc'), 'ccc')
    def test_lps_7(self):
        self.assertEqual(lps(''), None)
    def test_lps_8(self):
        self.assertEqual(lps('racecar'), 'racecar')


if __name__ == '__main__':
    unittest.main()