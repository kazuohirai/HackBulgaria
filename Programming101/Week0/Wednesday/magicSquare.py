def magic_square(matrix):
    test = []
    transposed = zip(*matrix)
    for item in matrix:
        test.append(sum(item))
    if len(set(test)) != 1:
        return False
    else:
        test = []
        for item in transposed:
            test.append(sum(item))
        if len(set(test)) != 1:
            return False
        else:
            test = []
            sums1 = 0
            sums2 = 0
            for i in range(0, len(matrix)):
                sums1 += matrix[i][i]

            sums2 = sum([r[-i - 1] for i, r in enumerate(matrix)])

            if sums1 != sums2:
                return False
            return True
