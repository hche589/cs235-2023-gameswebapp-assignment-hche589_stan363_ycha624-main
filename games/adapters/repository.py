import abc
from typing import List
from games.domainmodel.model import Game, Genre


repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        print(f'RepositoryException: {message}')


class AbstractRepository(abc.ABC):

    def __init__(self):
        self.repo_instance = None

    @abc.abstractmethod
    def add_game(self, game: Game):
        """ Add a game to the repository list of games. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_games(self) -> List[Game]:
        """ Returns the list of games. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_games(self):
        """ Returns a number of games exist in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def search_games(self, query: str) -> List[Game]:
        """ Returns a list of games that match the query. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_genres(self) -> List[Genre]:
        """ Returns a list of all unique genres in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_games_by_genre(self, genre_name: str) -> List[Game]:
        """ Returns a list of games associated with a genre. """
        raise NotImplementedError

    @abc.abstractmethod
    def set_genres(self, genres: List[str]):
        """ Sets the genres in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def set_games(self, games: List[Game]):
        """ Sets the games in the repository. """
        raise NotImplementedError


    @abc.abstractmethod
    def get_title_by_id(self, game_id):
        """ Returns the game with the given game_id. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_date_by_id(self, game_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_description_by_id(self, game_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_url_by_id(self, game_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_price_by_id(self, game_id):
        raise NotImplementedError




