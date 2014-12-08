import unittest
from os import remove
from sumIntsFromFile import sumIntsFromFile


class FileSumTests(unittest.TestCase):

    def setUp(self):
        self.filename = "integers.txt"
        self.contents = """48361"""
        with open(self.filename, 'w+') as f:
            f.write(self.contents)

    def tearDown(self):
        remove(self.filename)

    def test_sum_from_file(self):
        correct = sumIntsFromFile("numbers.txt")
        self.assertEqual(int(self.contents), correct)

if __name__ == "__main__":
    unittest.main()
