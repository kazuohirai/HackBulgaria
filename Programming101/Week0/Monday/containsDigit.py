
def contains_digit(number, digit):
    temp = str(number)
    for i in range(0, len(temp)):
        if number % 10 == digit:
            return True
        number /= 10
    return False
