from os import remove
import unittest

from cat import cat


class FileInputOutputTests(unittest.TestCase):
    def setUp(self):
        self.filename = 'blah.txt'
        self.file_contents = """This is some file
And cat is printing it's contents"""
        with open(self.filename, 'w+') as f:
            f.write(self.file_contents)

    def tearDown(self):
        remove(self.filename)

    def test_cat_with_existing_file(self):
        actual = cat(self.filename)
        self.assertEqual(self.file_contents, actual)


if __name__ == '__main__':
    unittest.main()
