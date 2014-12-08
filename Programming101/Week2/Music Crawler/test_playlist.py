import unittest
from playlist import Playlist
from song import Song


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.testPlaylist = Playlist("My Playlist")
        self.testSong = Song("Title", "Artist", "Album", 5, 120, 512)
        self.testSong2 = Song("Title2", "Artist", "Album", 2, 120, 320)
        self.testPlaylist.add_song(self.testSong)

    def test_init(self):
        self.assertEqual(self.testPlaylist.name, "My Playlist")

    def test_add_song(self):
        self.assertEqual(self.testPlaylist.collection, [self.testSong])

    def test_remove_song(self):
        self.testPlaylist.add_song(self.testSong2)
        self.testSong3 = Song("Title2", "Artist", "Album", 1, 120, 320)
        self.testPlaylist.add_song(self.testSong3)
        self.testPlaylist.remove_song("Title2")
        self.assertEqual(self.testPlaylist.collection, [self.testSong])

    def test_total_length(self):
        self.testPlaylist.add_song(self.testSong2)
        result = self.testPlaylist.total_length()
        self.assertEqual(result, 240)

    def test_remove_disrated_with_value_error(self):
        with self.assertRaises(ValueError):
            self.testPlaylist.remove_disrated(6)
        with self.assertRaises(ValueError):
            self.testPlaylist.remove_disrated(0)

    def test_remove_disrated_with_correct_input(self):
        self.testPlaylist.add_song(self.testSong2)
        self.testSong3 = Song("Title2", "Artist", "Album", 1, 120, 320)
        self.testPlaylist.add_song(self.testSong3)
        self.testPlaylist.remove_disrated(3)
        self.assertEqual(self.testPlaylist.collection, [self.testSong])

    def test_remove_bad_quality(self):
        self.testPlaylist.add_song(self.testSong2)
        self.testSong3 = Song("Title2", "Artist", "Album", 1, 120, 192)
        self.testPlaylist.add_song(self.testSong3)
        self.testPlaylist.remove_bad_quality(340)
        self.assertEqual(self.testPlaylist.collection, [self.testSong])

    def test_show_artists(self):
        self.testPlaylist.add_song(self.testSong2)
        self.testSong3 = Song("Title2", "Artist", "Album", 1, 120, 192)
        self.testPlaylist.add_song(self.testSong3)
        result = self.testPlaylist.show_artists()
        self.assertEqual(result, {"Artist"})


if __name__ == "__main__":
    unittest.main()
