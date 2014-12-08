from song import Song
import json


class Playlist:

    def __init__(self, name):
        self.name = name
        self.collection = []

    def add_song(self, song):
        self.collection.append(song)

    def remove_song(self, name):
        self.collection = [item for item in self.collection
                           if item.title != name]

    def total_length(self):
        length = 0
        for item in self.collection:
            length += item.length
        return length

    def remove_disrated(self, rating):
        if rating < Song.MIN_RATE or rating > Song.MAX_RATE:
            raise ValueError
        self.collection = [item for item in self.collection
                           if item.rating > rating]

    def remove_bad_quality(self, bitrate):
        self.collection = [item for item in self.collection
                           if item.bitrate > bitrate]

    def show_artists(self):
        artists = [song.artist for song in self.collection]
        return set(artists)

    def save(self, jsonfile):
        songsdict = []
        for item in self.collection:
            songsdict.append(item.__dict__)
        with open(jsonfile, "w") as f:
            json.dump({"Name": self.name, "Songs": songsdict}, f,
                      sort_keys=True, indent=4, separators=(',', ': '))

    @staticmethod
    def load(jsonfile):
        with open(jsonfile) as f:
            plst = json.loads(f.read())

        newPlaylist = Playlist(plst["Name"])
        for item in plst["Songs"]:
            newSong = Song(item["title"], item["artist"], item["album"],
                           item["rating"], item["length"], item["bitrate"])
            newPlaylist.add_song(newSong)
        return newPlaylist
