import unittest
from sort_evens_odds import sort_evens_odds


class TestSortEvensOdds(unittest.TestCase):
    def test_1(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        sort_evens_odds(A)
        self.assertEqual(A, [2, 4, 6, 8, 1, 3, 5, 7])

    def test_2(self):
        A = [1, 3, 5, 7, 2, 4, 6, 8]
        sort_evens_odds(A)
        self.assertEqual(A, [2, 4, 6, 8, 1, 3, 5, 7])

    def test_3(self):
        A = []
        sort_evens_odds(A)
        self.assertEqual(A, [])

    def test_4(self):
        A = [1]
        sort_evens_odds(A)
        self.assertEqual(A, [1])

    def test_5(self):
        A = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        sort_evens_odds(A)
        self.assertEqual(A, [1, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_6(self):
        A = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        sort_evens_odds(A)
        self.assertEqual(A, [2, 2, 2, 2, 2, 1, 1, 1, 1, 1])

    def test_7(self):
        A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sort_evens_odds(A)
        self.assertEqual(A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_8(self):
        A = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sort_evens_odds(A)
        self.assertEqual(A, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    def test_9(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        sort_evens_odds(A)
        self.assertEqual(A, [-10, -8, -6, -4, -2, 2, 4, 6, 8, 10, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9])


if __name__ == '__main__':
    unittest.main()