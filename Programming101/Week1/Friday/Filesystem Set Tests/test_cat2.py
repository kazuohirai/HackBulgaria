from os import remove
import unittest
from cat2 import cat2


class MultipleFileOutput(unittest.TestCase):
    def setUp(self):
        self.single = "output.txt"
        self.multiple = "multipleOutput.txt"
        self.multipleContents = """This is some file
And cat is printing it's contents
Python is an awesome language!
You should try it.
Also, you can use Python at a lot of different places!
"""
        self.singleContents = """Also, you can use Python at a lot of different places!
"""
        with open(self.multiple, 'w+') as f:
            f.write(self.multipleContents)

        with open(self.single, "w+") as f:
            f.write(self.singleContents)

    def tearDown(self):
        remove(self.multiple)

    def test_cat2_with_multiple_files(self):
        correct = cat2(["catfile.txt", "file1.txt", "file2.txt"])
        self.assertEqual(self.multipleContents, correct)

    def test_cat2_with_single_file(self):
        correct = cat2(["file2.txt"])
        self.assertEqual(self.singleContents, correct)

if __name__ == '__main__':
    unittest.main()
