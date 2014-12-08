def sum_of_digits(n):
    n = abs(n)
    temp = str(n)
    result = 0
    for i in range(0, len(temp)):
        result += n % 10
        n /= 10
    return result
