import unittest
from three import *

class TestThree(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_vertical([1,2,1,3]), 1)
        self.assertEqual(count_horizontal([1,1,3,1]), 1)

    def test_2(self):
        self.assertEqual(count_vertical([1,2,1,3,2,1,2,2]), 2)
        self.assertEqual(count_horizontal([1,1,3,1,2,1,4,1]), 2)

    def test_3(self):
        self.assertEqual(count_vertical([1,2]), 0)
        self.assertEqual(count_horizontal([1,1]), 0)

    def test_4(self):
        self.assertEqual(count_vertical([1,2,1,3,2,1,2,2,1,2,1,3,2,1,2,2]), 4)
        self.assertEqual(count_horizontal([1,1,3,1,2,1,4,1,1,1,3,1,2,1,4,1]), 4)

    def test_5(self):
        self.assertEqual(count_vertical([1,2,1,3,2,1,2,2,1,2,1,3,2,1,2,2,1,2,1,3,2,1,2,2]), 6)
        self.assertEqual(count_horizontal([1,1,3,1,2,1,4,1,1,1,3,1,2,1,4,1,1,1,3,1,2,1,4,1]), 6)

    def test_6(self):
        self.assertEqual(count_vertical([]), 0)
        self.assertEqual(count_horizontal([]), 0)

    #Test intersection
    def test_7(self):
        self.assertEqual(intersection([1,2,1,3,2,1,2,2]), False)

    def test_8(self):
        self.assertEqual(intersection([1,1,3,1,2,0,2,4]), True)

    def test_9(self):
        self.assertEqual(intersection([1,1,3,1,2,0,2,4,1,1,3,1,2,0,2,4]), True)

    def test_10(self):
        self.assertEqual(intersection([1,1,1,10,0,5,10, 5]), True)

    #parallel lines
    def test_11(self):
        self.assertEqual(intersection([1,1,1,10,2,1,2,10]), False)
   
    def test_12(self):
        self.assertEqual(intersection([1,1,1,10,2,1,10,1]), False)
if __name__ == "__main__":
    unittest.main()