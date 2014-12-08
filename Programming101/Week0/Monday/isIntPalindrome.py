
def is_int_palindrome(n):
    reg = str(n)
    rev = reg[::-1]
    if reg == rev:
        return True
    return False
