# factor out the big 'if' thingy
def inputCheck(matrix):
    for item in matrix:
        if len(item) != 9:
            return False
        if len(set(item)) != 9:
            return False


def sudoku_solved(sudoku):
    transposed = zip(*sudoku)
    if len(sudoku) != 9:
        return False

    inputCheck(sudoku)
    inputCheck(transposed)
    one = two = three = four = five = six = seven = eight = nine = []
    order = [[one, two, three], [four, five, six], [seven, eight, nine]]
    boxes = [one, two, three, four, five, six, seven, eight, nine]

    for i in range(0, 9):
        for j in range(0, 9):
            square = order[i / 3][j / 3]
            square.append(sudoku[i][j])

    for item in boxes:
        if len(set(item)) != 9:
            return False
    return True
