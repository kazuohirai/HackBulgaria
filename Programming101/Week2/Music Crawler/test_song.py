import unittest
from song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.testSong = Song("Title", "Artist", "Album", 5, 120, 320)

    def test_init(self):
        self.assertEqual(self.testSong.title, "Title")
        self.assertEqual(self.testSong.artist, "Artist")
        self.assertEqual(self.testSong.album, "Album")
        self.assertEqual(self.testSong.rating, 5)
        self.assertEqual(self.testSong.length, 120)
        self.assertEqual(self.testSong.bitrate, 320)

    def test_rate(self):
        with self.assertRaises(ValueError):
            self.testSong.rate(-1)
        with self.assertRaises(ValueError):
            self.testSong.rate(7)
        self.testSong.rate(4)
        self.assertEqual(4, self.testSong.rating)


if __name__ == "__main__":
    unittest.main()
