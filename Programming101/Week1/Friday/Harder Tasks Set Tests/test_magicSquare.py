import unittest
from magicSquare import magic_square


class TestMagicSquare(unittest.TestCase):

    def test_square_row_numbers_sum(self):
        result = magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertFalse(result)

    def test_square_col_numbers_sum(self):
        result = magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertFalse(result)

    def test_main_diagonal_of_matrix_numbers_sum(self):
        result = magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertFalse(result)

    def test_other_diagonal_of_matrix_numbers_sum(self):
        result = magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertFalse(result)

    def test_if_program_works_with_correct_input(self):
        result = magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]])
        result2 = magic_square([[7, 12, 1, 14], [2, 13, 8, 11],
                                [16, 3, 10, 5], [9, 6, 15, 4]])
        result3 = magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
        self.assertTrue(result)
        self.assertTrue(result2)
        self.assertTrue(result3)

if __name__ == "__main__":
    unittest.main()
