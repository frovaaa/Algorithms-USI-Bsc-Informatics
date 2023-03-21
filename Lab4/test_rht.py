import unittest
from rht import rht
import random

class TestRHT(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rht([1, 2, 3, 4, 5], 2), [1, 2, 3, 4, 5])
    def test_2(self):
        self.assertEqual(rht([1, 2, 3, 4, 5], 2), [1, 2, 3, 4, 5])
    def test_3(self):
        self.assertEqual(rht([1, 1, 2, 3, 4, 5], 1), [2, 3, 4, 5])
    def test_4(self):
        self.assertEqual(rht([1, 1, 2, 2, 3, 4, 5],1), [3, 4, 5])
    def test_5(self):
        self.assertEqual(rht([], 255), [])
    def test_6(self):
        self.assertEqual(rht([1], 1), [1])
    def test_7(self):
        A = [random.randint(0, 100) for i in range(100)]
        self.assertEqual(rht(A, 0), [])
        self.assertEqual(rht(A, 250), A)

if __name__ == '__main__':
    unittest.main()