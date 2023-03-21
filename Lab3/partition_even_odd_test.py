import unittest
from partition_even_odd import partition_even_odd

class TestPartitionEvenOdd(unittest.TestCase):
    def test_partition_even_odd(self):
        sequences = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [2,2,2],
            [0,0,0],
            [9,8,7,6,5,4,3,2,1],
        ]
        for A in sequences:
            partition_even_odd(A)
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    self.assertEqual( A[i]%2==1 and A[j]%2==0, False )
    def test_partition_even_odd_empty(self):
        A = []
        partition_even_odd(A)
        self.assertEqual(A, [])

    def test_partition_even_odd_one(self):
        A = [1]
        partition_even_odd(A)
        self.assertEqual(A, [1])
                
    def test_partition_even_odd_two(self):
        A = [1,2]
        partition_even_odd(A)
        self.assertEqual(A, [2,1])
        A = [2,1]
        partition_even_odd(A)
        self.assertEqual(A, [2,1])
        
if __name__ == '__main__':
    unittest.main()