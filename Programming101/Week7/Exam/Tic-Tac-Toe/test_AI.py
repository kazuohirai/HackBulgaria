import unittest
from AI import AI


class TestAI(unittest.TestCase):

    def setUp(self):
        self.testAI = AI([[".", ".", "."], [".", ".", "."], [".", ".", "."]],
                         {1: (0, 0), 2: (0, 1), 3: (0, 2),
                          4: (1, 0), 5: (1, 1), 6: (1, 2),
                          7: (2, 0), 8: (2, 1), 9: (2, 2)})

    def test_init(self):
        self.assertEqual(self.testAI.board, [[".", ".", "."],
                                             [".", ".", "."],
                                             [".", ".", "."]])

        self.assertEqual(self.testAI.coordinates, {1: (0, 0), 2: (0, 1), 3: (0, 2),
                                                   4: (1, 0), 5: (1, 1), 6: (1, 2),
                                                   7: (2, 0), 8: (2, 1), 9: (2, 2)})

    def test_free_spots(self):
        self.testAI.board = [["X", "X", "."], ["X", ".", "O"], ["O", ".", "O"]]
        result = self.testAI.get_free_spots()
        self.assertEqual(result, [(0, 2), (1, 1), (2, 1)])

    def test_move_with_one_spot_available(self):
        self.testAI.board = [["X", "X", "O"], ["O", ".", "X"], ["O", "X", "O"]]
        self.testAI.move()
        self.assertEqual(self.testAI.board, [["X", "X", "O"], ["O", "O", "X"], ["O", "X", "O"]])
        self.assertEqual(self.testAI.get_free_spots(), [])

    def test_check_rows_of_matrix_correct(self):
        self.testAI.board = [["X", "X", "X"], ["O", ".", "X"], ["O", "X", "O"]]
        result = self.testAI.check_rows_of_matrix(self.testAI.board)
        self.assertTrue(result)

    def test_check_cols_of_matrix_correct(self):
        self.testAI.board = [["X", "O", "X"], ["X", ".", "X"], ["X", "X", "O"]]
        transposed = zip(*self.testAI.board)
        result = self.testAI.check_rows_of_matrix(transposed)
        self.assertTrue(result)

    def test_check_cols_of_matrix_incorrect(self):
        self.testAI.board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
        result = self.testAI.check_rows_of_matrix(self.testAI.board)
        self.assertFalse(result)

    def test_diagonals_correct(self):
        self.testAI.board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
        result = self.testAI.check_diagonals(self.testAI.board)
        self.assertTrue(result)

    def test_diagonals_incorrect(self):
        self.testAI.board = [["X", "X", "X"], ["X", "O", "O"], ["X", "O", "O"]]
        result = self.testAI.check_diagonals(self.testAI.board)
        self.assertFalse(result)

    def test_check_board_fully_correct(self):
        self.testAI.board = [["X", "O", "X"], ["X", ".", "X"], ["X", "X", "O"]]
        result = self.testAI.check_board_for_winner()
        self.assertTrue(result)

    def test_check_board_fully_incorrect(self):
        self.testAI.board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        result = self.testAI.check_board_for_winner()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
