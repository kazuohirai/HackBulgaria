theater = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

max_free_spots = 100
max_cinema_rows = 10
max_cinema_cols = 10
min_cinema_rows = 0
min_cinema_cols = 0


helper = """show-movies - Displays all movies.
show-reservations <movie_id> <date> - Displays projections of <movie_id> for <date>
make-reservation - Creates a new reservation for a movie
cancel-reservation - Discards a reservation
exit - Closes the cinema manager
help - Displays this message"""


def print_matrix(matrix):
    first_row = " "
    for col in range(0, len(matrix)):
        first_row += " " + str(col)
    print (first_row)
    next_line = ""
    row_count = 0
    for row in matrix:
        next_line += str(row_count) + " "
        row_count += 1
        for col in row:
            next_line += col + " "
        print (next_line)
        next_line = ""
