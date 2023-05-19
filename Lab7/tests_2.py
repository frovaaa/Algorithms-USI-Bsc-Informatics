import unittest
from two import *

class TestTwo(unittest.TestCase):
    def test_1(self):
        A = [1, 0, 0, 1, 1, 0]
        self.assertEqual( BetterAlgoX(A), 3 )
        self.assertEqual( A, [1, 1, 1, 0, 0, 0] )

    def test_2(self):
        A = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual( BetterAlgoX(A), 5 )
        for i in A[:4]:
            self.assertEqual( i % 2, 1 )
        for i in A[5:]:
            self.assertEqual( i % 2, 0 )
    
    def test_3(self):
        A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual( BetterAlgoX(A), 10 )
        for i in A:
            self.assertEqual( i % 2, 1 )
    
    def test_4(self):
        A = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual( BetterAlgoX(A), 8 )
        for i in A[:8]:
            self.assertEqual( i % 2, 1 )
        for i in A[8:]:
            self.assertEqual( i % 2, 0 )
if __name__ == '__main__':
    unittest.main()