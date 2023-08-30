from typing import List
from games.domainmodel.model import Game, Genre
from games.adapters.repository import AbstractRepository
from games.adapters.datareader.csvdatareader import GameFileCSVReader
from bisect import insort_left

import os

GAMES_PER_PAGE = 15

class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__games = list()
        self.__dataset_of_genres = []
        self.__dataset_of_games = list()

    def add_game(self, game: Game):
        if isinstance(game, Game):
            # When inserting the game, keep the game list sorted alphabetically by the id.
            # Games will be sorted by game due to __lt__ method of the Game class.
            insort_left(self.__games, game)

    def get_games(self) -> List[Game]:
        return self.__games

    def get_number_of_games(self):
        return len(self.__games)

    def set_genres(self, genres):
        self.__dataset_of_genres = genres

    def set_games(self, games):
        self.__dataset_of_games = games

    def search_games(self, query: str) -> List[Game]:
        return [game for game in self.__games if query.lower() in game.title.lower()]

    def get_all_genres(self) -> List[Genre]:
        return list(self.__dataset_of_genres)

    def get_games_by_genre(self, genre_name: str) -> List[Game]:
        return [game for game in self.__dataset_of_games if genre_name in game.genres]

    def get_title_by_id(self, game_id):
        for game in self.__dataset_of_games:
            if game_id == game.game_id:
                return game.title

    def get_date_by_id(self, game_id):
        for game in self.__dataset_of_games:
            if game_id == game.game_id:
                return game.release_date

    def get_description_by_id(self, game_id):
        for game in self.__dataset_of_games:
            if game_id == game.game_id:
                return game.description

    def get_url_by_id(self, game_id):
        for game in self.__dataset_of_games:
            if game_id == game.game_id:
                return game.url
    def get_price_by_id(self, game_id):
        for game in self.__dataset_of_games:
            if game_id == game.game_id:
                if game.price is None:
                    return 0
                return game.price

def populate(repo: AbstractRepository):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    games_file_name = os.path.join(dir_name, "data/games.csv")
    reader = GameFileCSVReader(games_file_name)

    reader.read_csv_file()

    games = reader.dataset_of_games
    genres = reader.dataset_of_genres

    # Add games to the repo
    for game in games:
        repo.add_game(game)

    repo.__dataset_of_genres = genres
    repo.__dataset_of_games = games
    repo.set_genres(genres)
    repo.set_games(games)

