class Song:
    MAX_RATE = 5
    MIN_RATE = 1

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def human_time(self, secs):
        mins, secs = divmod(secs, 60)
        hours, mins = divmod(mins, 60)
        return "%02d:%02d:%02d" % (hours, mins, secs)

    def __str__(self):
        return "{} - {} / {}".format(self.artist, self.title,
                                     self.human_time(self.length))

    def rate(self, rating):
        if rating > Song.MAX_RATE or rating < Song.MIN_RATE:
            raise ValueError
        else:
            self.rating = rating
