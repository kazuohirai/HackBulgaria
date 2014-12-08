def nth_fibonacci(n):
    if n < 1:
        return -1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        first = 1
        second = 1
        for i in range(2, n):
            display = first + second
            first = second
            second = display
    return display
