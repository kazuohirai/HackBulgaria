from isIntPalindrome import is_int_palindrome


def next_hack(n):
    n += 1
    chars = "{0:b}".format(n)
    if chars.count("1") % 2 == 1 and is_int_palindrome(chars):
        return n
    return next_hack(n)
