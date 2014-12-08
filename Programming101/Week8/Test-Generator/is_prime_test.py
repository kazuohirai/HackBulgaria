import unittest
from is_prime import is_prime


class IsPrimeTest(unittest.TestCase):
    "This is a test class for testing is_prime funciton"
    def TestCase1(self):
        self.assertTrue(is_prime(7), "7 should noot be prime")

    def TestCase2(self):
        self.assertFalse(is_prime(8), "8 should be prime")

    def TestCase3(self):
        self.assertEqual(sum(1, 2), 3, "sum should be 3")

if __name__ == '__main__':
    unittest.main()
