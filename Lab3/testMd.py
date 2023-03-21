import unittest
from md import md


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(md([1, 2, 3]), 2)

    def test_2(self):
        self.assertEqual(md([1, 10, 20, 30, 50, -1]), 51)

    def test_3(self):
        self.assertEqual(md([1, 2, 1, 2, 1, 2]), 1)

    def test_4(self):
        self.assertEqual(md([-1, -2, 3]), 5)

    def test_5(self):
        self.assertEqual(md([1, 10, 20, 30, -50, -1]), 80)

    def test_6(self):
        self.assertEqual(md([-1, -2, -1, -2, -1, -2]), 1)


if __name__ == "__main__":
    unittest.main()