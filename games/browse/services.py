from games.adapters.repository import AbstractRepository
from games.domainmodel.model import Game, Genre
from typing import List
from games.adapters.memory_repository import MemoryRepository


def get_number_of_games(repo: AbstractRepository):
    return repo.get_number_of_games()


GAMES_PER_PAGE = 15

def get_paginated_games(repo: AbstractRepository, page_num: int) -> List[dict]:
    all_games = repo.get_games()
    sorted_games = sorted(all_games, key=lambda x: x.title)
    start_index = (page_num - 1) * GAMES_PER_PAGE
    end_index = start_index + GAMES_PER_PAGE
    games = sorted_games[start_index:end_index]

    game_dicts = []
    for game in games:
        game_dict = {
            'game_id': game.game_id,
            'title': game.title,
            'release_date': game.release_date,
            'price': game.price,
            'publisher': game.publisher,
            'genres': game.genres,
            'image': game.image_url,
        }
        game_dicts.append(game_dict)

    return game_dicts

def get_paginated_games_by_genre(repo: AbstractRepository, genre_name: str, page_num: int) -> List[dict]:
    all_games = repo.get_games_by_genre(genre_name)
    sorted_games = sorted(all_games, key=lambda x: x.title)
    start_index = (page_num - 1) * GAMES_PER_PAGE
    end_index = start_index + GAMES_PER_PAGE
    games = sorted_games[start_index:end_index]

    game_dicts = []
    for game in games:
        game_dict = {
            'game_id': game.game_id,
            'title': game.title,
            'release_date': game.release_date,
            'price': game.price,
            'publisher': game.publisher,
            'genres': game.genres,
            'image': game.image_url,
        }
        game_dicts.append(game_dict)
    return game_dicts

def search_games_by_title(repo: AbstractRepository, title_query: str):
    all_games = repo.get_games()
    return [game for game in all_games if title_query.lower() in game.title.lower()]

def search_games_by_id(repo: AbstractRepository, id_query: int):
    all_games = repo.get_games()
    return [game for game in all_games if game.game_id == id_query]

def search_games_by_price(repo: AbstractRepository, id_query: float):
    all_games = repo.get_games()
    return [game for game in all_games if game.price == id_query]

def get_all_genres(repo: AbstractRepository) -> List[Genre]:
    return repo.get_all_genres()

def get_games_by_genre(repo: AbstractRepository, genre_name: str, page_num: int) -> List[Game]:
    return repo.get_games_by_genre(genre_name)

'hello world'

def get_title_by_id(repo: AbstractRepository, game_id):
    title = repo.get_title_by_id(game_id)
    if title:
        return title
    else:
        return None 

def get_date_by_id(repo: AbstractRepository, game_id):
    release_date = repo.get_date_by_id(game_id)
    if release_date:
        return release_date
    else:
        return None


def get_description_by_id(repo: AbstractRepository, game_id) :
    description = repo.get_description_by_id(game_id)
    if description:
        return description
    else:
        return "No description available"

def get_url_by_id(repo: AbstractRepository, game_id):
    url = repo.get_url_by_id(game_id)
    if url:
        return url
    else:
        return None

def get_price_by_id(repo: AbstractRepository, game_id):
    price = repo.get_price_by_id(game_id)
    if price:
        return price
    else:
        return 0
