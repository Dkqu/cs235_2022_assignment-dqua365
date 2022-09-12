from pathlib import Path
from typing import List
from music.adapters.repository import AbstractRepository, RepositoryException
from music.domainmodel.album import Album
from music.domainmodel.user import User
from music.domainmodel.track  import Track
from music.domainmodel.review  import Review
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre
from music.domainmodel.playlist import PlayList
from music.adapters.csvdatareader import TrackCSVReader
from werkzeug.security import generate_password_hash
from bisect import bisect, bisect_left, insort_left


class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.
    def __init__(self):
        #The following lists will be used to filter and access via ID
        self.__albums = list()
        self.__artists = list()
        self.__genres = list()
        self.__tracks = list()


        #Normal Data
        self.__users = list()
        self.__playlists = list()
        self.__reviews = list()

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)

    def add_playlist(self, playlist: PlayList):
        self.__playlists.append(playlist)
    def get_playlist(self, playlist) -> PlayList:
        return next((pl for pl in self.__playlists if pl.list_of_tracks == playlist), None)

    def get_playlists_by_track(self, track: Track) -> List[PlayList]:
        matching_playlists = list()

        try:
            for p in self.__playlists:
                for t in p.list_of_tracks:
                    if t.id == track.id:
                        matching_playlists.append(p)
                        break
        except ValueError:
            # No articles for specified date. Simply return an empty list.
            pass

        return matching_playlists
    

    #Albums
    def add_album(self, album: Album):
        self.__albums.append(album)
        self.__articles_index[album.id] = album

    def get_album(self, id: int) -> Album:
        album = None

        try:
            album = self.__albums_index[id]
        except KeyError:
            pass  # Ignore exception and return None.

        return album
    #Artists
    def add_artists(self, artist: Artist):
        self.__artists.append(artist)
        self.__artists_index[artist.id] = artist


    def get_artist(self, id: int) -> Artist:
        artist = None

        try:
            artist= self.__artists_index[id]
        except KeyError:
            pass  # Ignore exception and return None.

        return artist


    def add_genre(self, genre: Genre):
        self.__genres.append(genre)
        self.__genres_index[genre.id] = genre

    def get_genre(self, id: int) -> Genre:
        genre = None

        try:
           genre = self.__genres_index[id]
        except KeyError:
            pass  # Ignore exception and return None.

        return genre

    def add_track(self, track: Track):
        self.__tracks.append(track)
        self.__tracks_index[track.id] = track


    def get_track(self, id: int) -> Track:
        track = None

        try:
            track = self.__tracks_index[id]
        except KeyError:
            pass  # Ignore exception and return None.

        return track

    def get_tracks_by_time(self, track: Track) -> List[PlayList]:
        matching_playlists = list()

        try:
            for p in self.__playlists:
                for t in p.list_of_tracks:
                    if t.id == track.id:
                        matching_playlists.append(p)
                        break
        except ValueError:
            # No articles for specified date. Simply return an empty list.
            pass


def populate(data_path: Path, repo: MemoryRepository):
    albums_filename = str(Path(data_path) / "comments.csv")
    reader = TrackCSVReader(str(Path(data_path) / "raw_albums_excerpt.csv"), str(Path(data_path) / "raw_tracks_excerpt.csv"))
    repo.__tracks = reader.read_csv_files()
    repo.__albums = list(reader.dataset_of_albums)
    repo.__artists = list(reader.dataset_of_artists)
    repo.__genres = list(reader.dataset_of_genres)

    