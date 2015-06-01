def rotate(word):
    return word[1:] + word[0]


def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False


def all_palindromes(word):
    rotations = [word]
    rot = word
    for i in range(0, len(word) - 1):
        rot = rotate(rot)
        rotations.append(rot)
    for item in rotations:
        if is_palindrome(item):
            print (item)
