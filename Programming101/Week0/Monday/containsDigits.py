from containsDigit import contains_digit


def contains_digits(number, digits):
    count = 0
    for digit in digits:
        if contains_digit(number, digit):
            count += 1
    if count == len(digits):
        return True
    return False
