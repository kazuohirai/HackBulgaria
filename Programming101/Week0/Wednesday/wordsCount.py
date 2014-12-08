from collections import Counter


def count_words(arr):
    return dict(Counter(arr))


def unique_words_count(arr):
    return len(set(arr))
