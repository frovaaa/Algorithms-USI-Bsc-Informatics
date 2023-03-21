import unittest
from two import *

class TestTwo(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_sorted([1,2,3,4,5,6,7,8,9]), True)

    def test_2(self):
        self.assertEqual(is_sorted([1,2]), True)

    def test_3(self):
        self.assertEqual(is_sorted([1]), True)

    def test_4(self):
        self.assertEqual(is_sorted([]), True)

    def test_5(self):
        self.assertEqual(is_sorted([1,2,3,4,5,6,7,8,9,8]), False)

    def test_6(self):
        self.assertEqual(is_sorted([1,1,1]), True)

    def test_7(self):
        self.assertEqual(is_sorted([1,1,1,2,3]), True)

    def test_8(self):
        self.assertEqual(is_sorted([1,2,3,2,3]), False)
        
if __name__ == '__main__':
    unittest.main()