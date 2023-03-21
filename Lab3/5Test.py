import unittest
from prime_factorize import prime_factorize

class TestPrimeFactorize(unittest.TestCase):
    def test_prime_factorize(self):
        self.assertEqual( prime_factorize(1), "" )
    def test_prime_factorize_2(self):
        self.assertEqual( prime_factorize(2), "2" )
    def test_prime_factorize_3(self):
        self.assertEqual( prime_factorize(3), "3" )
    def test_prime_factorize_4(self):
        self.assertEqual( prime_factorize(4), "2E2" )
    def test_prime_factorize_5(self):
        self.assertEqual( prime_factorize(5), "5" )
    def test_prime_factorize_6(self):
        self.assertEqual( prime_factorize(2312), "2E3 17E2" )
    def test_prime_factorize_7(self):
        self.assertEqual( prime_factorize(10242311), "19 701 769" )

if __name__ == "__main__":
    unittest.main()