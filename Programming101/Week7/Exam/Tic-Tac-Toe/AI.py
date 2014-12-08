from random import randint

MAX_BOARD_LENGTH = 3
MAX_BOARD_HEIGHT = 3


class AI():
    def __init__(self, board, coordinates):
        self.board = board
        self.coordinates = coordinates
        self.available_spots = []
        self.AIrow = 0
        self.AIcol = 0

    def print_board(self):
        for row in self.board:
            for col in row:
                print ('|'+col, end='|')
            print ('\n')

    def get_free_spots(self):
        self.available_spots = []
        for row in range(0, MAX_BOARD_LENGTH):
            for col in range(0, MAX_BOARD_HEIGHT):
                if self.board[row][col] == ".":
                    self.available_spots.append((row, col))
        return self.available_spots

    def determine_pattern_for_row(self, row):
        if row[0] == "X" and row[1] == "X" and row[2] == ".":
            self.AIcol = 2
            return True
        elif row[1] == "X" and row[2] == "X" and row[0] == ".":
            self.AIcol = 0
            return True
        elif row[2] == "X" and row[0] == "X" and row[1] == ".":
            self.AIcol = 1
            return True
        return False

    def determine_pattern_for_col(self, matrix):
        column = []
        count = 0
        for col in range(0, len(matrix)):
            for row in range(0, len(matrix)):
                column.append(matrix[row][col])
            if self.determine_pattern_for_row(column):
                self.AIrow = self.AIcol
                self.AIcol = count
                return True
            column = []
            count += 1
        return False

    def calculate_coordinates_of_opposite_diagonal(self, index):
        if index == 0:
            self.AIrow = 2
        elif index == 1:
            self.AIrow = 1
        elif index == 2:
            self.AIrow = 0

    def determine_pattern_for_diagonals(self, matrix):
        main_diag = [row[item] for item, row in enumerate(matrix)]
        other_diag = [row[-item-1] for item, row in enumerate(matrix)]
        if self.determine_pattern_for_row(main_diag):
            self.AIrow = self.AIcol
            return True
        elif self.determine_pattern_for_row(other_diag):
            self.calculate_coordinates_of_opposite_diagonal(self.AIcol)
            self.AIcol, self.AIrow = self.AIrow, self.AIcol
            return True
        return False

    def determine_pattern(self):
        for row in self.board:
            if self.determine_pattern_for_row(row):
                self.AIrow = self.board.index(row)
                return True
        if self.determine_pattern_for_col(self.board):
            return True
        if self.determine_pattern_for_diagonals(self.board):
            return True
        return False

    def move(self):
        self.get_free_spots()
        if len(self.available_spots) == 1:
            GPS = self.available_spots[0]
            self.board[GPS[0]][GPS[1]] = "O"

        if len(self.available_spots) > 1:
            if self.determine_pattern():
                print ("Not so fast...")
                self.board[self.AIrow][self.AIcol] = "O"
            else:
                move = randint(0, len(self.available_spots)-1)
                GPS = self.available_spots[move]
                self.board[GPS[0]][GPS[1]] = "O"

    def check_rows_of_matrix(self, matrix):
        for row in matrix:
            if len(set(row)) == 1 and "." not in row:
                print ("{} wins!".format(row[0]))
                return True
        return False

    def check_diagonals(self, matrix):
        main_diag = [row[item] for item, row in enumerate(matrix)]
        other_diag = [row[-item-1] for item, row in enumerate(matrix)]
        if len(set(main_diag)) == 1 and "." not in main_diag:
            print ("{} wins!".format(main_diag[0]))
            return True
        elif len(set(other_diag)) == 1 and "." not in other_diag:
            print ("{} wins!".format(other_diag[0]))
            return True

    def check_board_for_winner(self):
        transposed = zip(*self.board)
        if (self.check_rows_of_matrix(self.board) or
                self.check_rows_of_matrix(transposed) or
                self.check_diagonals(self.board)):
            print("Game Over.")
            return True
        return False
