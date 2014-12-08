import unittest
from wordsCount import count_words
from wordsCount import unique_words_count


class TestWordsCount(unittest.TestCase):
    def test_unique_words_count(self):
        self.assertEqual(3, unique_words_count(["apple",
                                                "banana", "apple", "pie"]))
        self.assertEqual(1, unique_words_count(["HELLO!"] * 10))

    def test_words_counter(self):
        self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1},
                         count_words(["apple", "banana", "apple", "pie"]))
        self.assertEqual({'ruby': 1, 'python': 3},
                         count_words(["python", "python", "python", "ruby"]))

if __name__ == "__main__":
    unittest.main()
