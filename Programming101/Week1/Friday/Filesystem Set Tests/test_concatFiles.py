import unittest
from os import remove
from cat import cat


class MultipleFileConcat(unittest.TestCase):
    def setUp(self):
        self.name = "Voltron.txt"
        self.contents = """This is some file
And cat is printing it's contents

Python is an awesome language!
You should try it.

Also, you can use Python at a lot of different places!

"""
        with open(self.name, "w+") as f:
            f.write(self.contents)

    def tearDown(self):
        remove(self.name)

    def test_multiple_concat(self):
        correct = cat("Megatron.txt")
        self.assertEqual(self.contents, correct)

if __name__ == "__main__":
    unittest.main()
