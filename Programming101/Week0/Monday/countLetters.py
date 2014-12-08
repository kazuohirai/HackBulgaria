
def count_vowels(str):
    vowel = "AEIOUYaeiouy"
    count = 0
    for item in str:
        if item in vowel:
            count += 1
    return count


def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0
    str = str.lower()
    for item in str:
        if item in consonants:
            count += 1
    return count
