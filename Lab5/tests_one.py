import unittest
from one import *

class Test(unittest.TestCase):
    def test_1(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],1), [2,3,4,5,6,7,8,9,1])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],1), [2,3,4,5,6,7,8,9,1])

    def test_2(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],2), [3,4,5,6,7,8,9,1,2])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],2), [3,4,5,6,7,8,9,1,2])

    def test_3(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],3), [4,5,6,7,8,9,1,2,3])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],3), [4,5,6,7,8,9,1,2,3])

    def test_4(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],4), [5,6,7,8,9,1,2,3,4])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],4), [5,6,7,8,9,1,2,3,4])
    
    def test_5(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],5), [6,7,8,9,1,2,3,4,5])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],5), [6,7,8,9,1,2,3,4,5])

    def test_6(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],6), [7,8,9,1,2,3,4,5,6])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],6), [7,8,9,1,2,3,4,5,6])

    def test_7(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],7), [8,9,1,2,3,4,5,6,7])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],7), [8,9,1,2,3,4,5,6,7])

    def test_8(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],8), [9,1,2,3,4,5,6,7,8])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],8), [9,1,2,3,4,5,6,7,8])
    
    def test_9(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],9), [1,2,3,4,5,6,7,8,9])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],9), [1,2,3,4,5,6,7,8,9])

    def test_10(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],10), [2,3,4,5,6,7,8,9,1])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],10), [2,3,4,5,6,7,8,9,1])

    def test_11(self):
        #self.assertEqual(rotate([1,2,3,4,5,6,7,8,9],11), [3,4,5,6,7,8,9,1,2])
        self.assertEqual(rotate_in_place([1,2,3,4,5,6,7,8,9],11), [3,4,5,6,7,8,9,1,2])

    def test_12(self):
        #self.assertEqual(rotate([],1), [])
        self.assertEqual(rotate_in_place([],1), [])

    def test_13(self):
        #self.assertEqual(rotate([],10), [])
        self.assertEqual(rotate_in_place([],10), [])

    def test_14(self):
        #self.assertEqual(rotate([1,2,3],-1), [3,1,2])
        self.assertEqual(rotate_in_place([1,2,3],-1), [3,1,2])


if __name__ == '__main__':
    unittest.main()