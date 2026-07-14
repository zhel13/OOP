from typing import List

from Spoopify.project.song import Song

class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.songs: List[Song] = list(args)
        self.published: bool = False


    def add_song(self, song: Song) -> str:
        if song.name not in self.songs:
            if song.single:
                return f'Cannot add {song.name}. It\'s a single'
            elif self.published:
                return f'Cannot add songs. Album is published.'
            self.songs.append(song)
            return f'Song {song.name} has been added to the album {self.name}.'

        return f'Song is already in the album.'

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return f'Cannot remove songs. Album is published.'
        try:
            song = [s for s in self.songs if s == song_name][0]
            self.songs.remove(song)
            return f'Removed song {song_name} from album {self.name}.'
        except IndexError:
            return f"Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self) -> str:
        result = f'Album {self.name}\n'
        songs = [f'== {s.get_info()}' for s in self.songs]

        result += '\n'.join(songs)
        return result + '\n'