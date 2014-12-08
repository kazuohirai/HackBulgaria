import unittest
from groupBy import groupby


class test_groupBy(unittest.TestCase):

    def test_if_function_groups_properly(self):
        result = groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7])
        result2 = groupby(lambda x: 'odd' if x %
                          2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])
        result3 = groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(result, {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})
        self.assertEqual(result2, {'even': [2, 8, 10, 12],
                                   'odd': [1, 3, 5, 9]})
        self.assertEqual(result3, {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]})
if __name__ == "__main__":
    unittest.main()
