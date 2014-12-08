import os
from playlist import Playlist
from song import Song
from mutagen.mp3 import MP3


class MusicCrawler:
    FORMATS = ('.mp3', '.ogg', '.flac')
    DEF_TIT = 'Unknown Title'
    DEF_ART = 'Unknown Artist'
    DEF_ALB = 'Unknown Album'
    DEF_RAT = 0

    AUD_TIT = 'TIT2'
    AUD_ART = 'TPE1'
    AUD_ALB = 'TALB'

    def __init__(self, crawlDir):
        self.__crawlDir = crawlDir

    def _get_mp3_files(self, crawlDir):
        files = os.listdir(self.__crawlDir)
        files = [file for file in files if file.endswith(self.FORMATS)]
        return files

    def _get_tags(self, audio):
        tags = {}
        tags['title'] = audio.get(self.AUD_TIT, self.DEF_TIT)
        tags['artist'] = audio.get(self.AUD_ART, self.DEF_ART)
        tags['album'] = audio.get(self.AUD_ALB, self.DEF_ALB)
        return tags

    def _get_length(self, audio):
        return int(audio.info.length)

    def _get_bitrate(self, audio):
        return audio.info.bitrate

    def _get_rating(self, audio):
        return audio.get(self.DEF_RAT)

    def _create_song(self, obj):
        song_tags = self._get_tags(obj)
        song_length = self._get_length(obj)
        song_bitrate = self._get_bitrate(obj)

        song = Song(str(song_tags['title']), str(song_tags['artist']),
                    str(song_tags['album']), str(self.DEF_RAT),
                    str(song_length), str(song_bitrate))
        return song

    def generate_playlist(self, name):
        output_playlist = Playlist(name)
        files = self._get_mp3_files(self.__crawlDir)
        for filename in files:
            filename = self.__crawlDir + filename
            audio_obj = MP3(filename)
            song = self._create_song(audio_obj)
            output_playlist.add_song(song)
        return output_playlist
