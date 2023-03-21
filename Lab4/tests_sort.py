import unittest
from sort import sort

class TestSort(unittest.TestCase):
    def tests_1(self):
        A = [2, 1, 3, 4, 5]
        sort( A, 1 )
        self.assertEqual(A, [1, 2, 3, 4, 5])
        sort( A, 0 )
        self.assertEqual(A, [5, 4, 3, 2, 1])
    def tests_2(self):
        A = []
        sort( A, 1 )
        self.assertEqual(A, [])
        sort( A, 0 )
        self.assertEqual(A, [])
    def tests_3(self):
        A = [1]
        sort( A, 1 )
        self.assertEqual(A, [1])
        sort( A, 0 )
        self.assertEqual(A, [1])
    def tests_4(self):
        A = [1, 2, 3, 4, 5]
        sort( A, 0 )
        sort( A, 1 )
        self.assertEqual(A, [1, 2, 3, 4, 5])
    def tests_5(self):
        A = [x for x in range(100, 0 , -1)]
        sort( A, 1 )
        self.assertEqual(A, [x for x in range(1, 101)])
    def tests_6(self):
        self.assertEqual(sort([1, 2, 3, 4, 5], 1), None)

if __name__ == '__main__':
    unittest.main()