import unittest

from fibLists import nth_fib_lists
from fibLists import member_of_nth_fib_lists


class Test_Fib_Lists(unittest.TestCase):

    def test_if_function_returns_length_of_list(self):
        self.assertEqual([], nth_fib_lists([], [], 4))

    def test_if_function_returns_A_when_n_equals_one(self):
        result = nth_fib_lists([1, 2], [3, 4], 1)
        self.assertEqual([1, 2], result)

    def test_if_function_returns_B_when_n_equals_two(self):
        result = nth_fib_lists([1, 2], [3, 4], 2)
        self.assertEqual([3, 4], result)

    def test_function_when_n_bigger_than_three(self):
        result = nth_fib_lists([1, 2], [3, 4], 4)
        self.assertEqual([1, 2, 3, 4, 3, 4], result)

    def test_member_of_nth_fib_lists(self):
        result = member_of_nth_fib_lists([1, 2], [3, 4], [5, 6])
        result2 = member_of_nth_fib_lists(
            [7, 11], [2], [7, 11, 2, 2, 7, 11, 2])
        self.assertFalse(result)
        self.assertTrue(result2)

if __name__ == '__main__':
    unittest.main()
