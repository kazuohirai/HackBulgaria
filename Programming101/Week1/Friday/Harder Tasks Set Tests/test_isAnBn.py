import unittest
from isAnBn import is_an_bn


class testIsAnBn(unittest.TestCase):
    def test_word_length(self):
        self.assertTrue(is_an_bn(""))

    def test_if_a_is_after_b(self):
        self.assertFalse(is_an_bn("aabbaabb"))
        self.assertFalse(is_an_bn("aabbaabbaabb"))

    def test_if_there_are_equal_As_and_Bs(self):
        self.assertFalse(is_an_bn("aaabb"))
        self.assertTrue(is_an_bn("aaabbb"))

if __name__ == "__main__":
    unittest.main()
