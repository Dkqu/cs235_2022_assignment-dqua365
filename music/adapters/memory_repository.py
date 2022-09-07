from music.adapters.repository import AbstractRepository, RepositoryException
from music.domainmodel.album import Album
from music.domainmodel.user import User
from music.domainmodel.track  import Track
from music.domainmodel.review  import Review

class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.
    def __init__(self):
        self.__albums = list()
        self.__artists = list()
        self.__genres = list()
        self.__users = list()
        self.__tracks = list()
        self.__playlists = list()
        self.__reviews = list()

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)

    def add_album(self, album: Article):
        insort_left(self.__articles, article)
        self.__articles_index[article.id] = article

    def get_article(self, id: int) -> Article:
        article = None

        try:
            article = self.__articles_index[id]
        except KeyError:
            pass  # Ignore exception and return None.

        return article
