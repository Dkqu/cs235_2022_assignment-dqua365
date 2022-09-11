import abc
from typing import List
from datetime import date

from music.domainmodel.album import Album
from music.domainmodel.user import User
from music.domainmodel.track  import Track
from music.domainmodel.review  import Review
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre
from music.domainmodel.playlist import PlayList


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError
    @abc.abstractmethod
    def get_user(self, user_name) -> User:
       raise NotImplementedError
    @abc.abstractmethod
    def add_playlist(self, playlist: PlayList):
        raise NotImplementedError
    @abc.abstractmethod
    def get_playlist(self, playlist) -> PlayList:
        raise NotImplementedError
    @abc.abstractmethod
    def get_playlists_by_track(self, track: Track) -> List[PlayList]:
        raise NotImplementedError
    @abc.abstractmethod
    def add_album(self, album: Album):
        raise NotImplementedError
    @abc.abstractmethod
    def get_album(self, id: int) -> Album:
        raise NotImplementedError
    #Artists
    @abc.abstractmethod
    def add_artists(self, artist: Artist):
        raise NotImplementedError

    @abc.abstractmethod
    def get_artist(self, id: int) -> Artist:
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError
    @abc.abstractmethod
    def get_genre(self, id: int) -> Genre:
        raise NotImplementedError

    
    @abc.abstractmethod
    def add_track(self, track: Track):
        raise NotImplementedError

    @abc.abstractmethod
    def get_track(self, id: int) -> Track:
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_by_time(self, track: Track) -> List[PlayList]:
        raise NotImplementedError

    







