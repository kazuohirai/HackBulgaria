import unittest
from fractions import sort_fractions


class testFractions(unittest.TestCase):

    def test_sort_fractions(self):
        result = sort_fractions(
            [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])
        self.assertEqual(
            [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)], result)

if __name__ == "__main__":
    unittest.main()
