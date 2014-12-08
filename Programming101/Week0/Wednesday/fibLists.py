def nth_fib_lists(A, B, n):
    nextf = []
    fib = []
    if len(A) == 0 and len(B) == 0:
        return fib
    if n == 1:
        return A
    elif n == 2:
        return B
    else:
        while n >= 3:
            fib += A + B
            A = B
            B = nextf
            n -= 1
    return fib


def member_of_nth_fib_lists(listA, listB, needle):
    haystack = listA + listB + listB + listA + listB
    count = 0
    for item in needle:
        for hay in haystack:
            if item == hay:
                count += 1
                break
    if count == len(needle):
        return True
    return False
