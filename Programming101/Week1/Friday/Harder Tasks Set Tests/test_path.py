import unittest
from path import reduce_file_path


class TestPath(unittest.TestCase):
    def test_reduced(self):
        self.assertEqual("/srv/www/htdocs/wtf",
                         reduce_file_path("/srv/www/htdocs/wtf/"))
        self.assertEqual("/", reduce_file_path("//////////////"))
        self.assertEqual("/", reduce_file_path("/etc/../etc/../etc/../"))


if __name__ == "__main__":
    unittest.main()
