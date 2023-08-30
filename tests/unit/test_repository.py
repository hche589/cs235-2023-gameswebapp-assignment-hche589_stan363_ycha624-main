import pytest
from games.domainmodel.model import Game, Genre
from games.adapters.memory_repository import MemoryRepository
from games.adapters.datareader.csvdatareader import GameFileCSVReader
import os


@pytest.fixture
def sample_repo():
    repo = MemoryRepository()
    game1 = Game(1, "Game 1")
    game1.id = 1
    game1.title = "Game 1"
    game1.release_date = "Mar 12, 2018"
    game1.description = "Description for Game 1"
    game1.url = "https://example.com/game1"
    game1.price = 0.99

    game2 = Game(2, "Game 2")
    game2.id = 2
    game2.title = "Game 2"
    game2.release_date = "Aug 30, 2023"
    game2.description = "Description for Game 2"
    game2.url = "https://example.com/game2"
    game2.price = 1.99

    repo.add_game(game1)
    repo.add_game(game2)

    return repo


def test_add_and_retrieve_game(sample_repo):
    game = Game(3, "Game 3")
    sample_repo.add_game(game)
    retrieved_game = sample_repo.get_games()[2]
    assert retrieved_game == game

def test_get_number_of_games(sample_repo):
    assert sample_repo.get_number_of_games() == 2

def test_get_unique_genres(sample_repo):
    genres = sample_repo.get_all_genres()
    assert len(genres) == 0

def test_get_nonexistent_game_title_by_id(sample_repo):
    game_id = 1
    game_title = sample_repo.get_title_by_id(game_id)
    assert game_title is None

def test_get_nonexistent_date_by_id(sample_repo):
    game_id = 1
    game_date = sample_repo.get_date_by_id(game_id)
    assert game_date is None

def test_search_games_by_title(sample_repo):
    games_found = sample_repo.search_games("Game 1")
    assert len(games_found) == 1
    assert games_found[0].title == "Game 1"

def test_search_games_by_genre_name(sample_repo):
    genre_name = "Action"
    games_found = sample_repo.get_games_by_genre(genre_name)
    assert all(genre_name in game.genres for game in games_found)

def test_get_nonexistent_game_by_id(sample_repo):
    game_id = 999  # Assuming 999 doesn't correspond to any existing game
    game_title = sample_repo.get_title_by_id(game_id)
    assert game_title is None

def test_get_nonexistent_game_date_by_id(sample_repo):
    game_id = 999
    game_date = sample_repo.get_date_by_id(game_id)
    assert game_date is None

def test_get_nonexistent_game_description_by_id(sample_repo):
    game_id = 999
    game_description = sample_repo.get_description_by_id(game_id)
    assert game_description is None

def test_get_nonexistent_game_url_by_id(sample_repo):
    game_id = 999
    game_url = sample_repo.get_url_by_id(game_id)
    assert game_url is None

def test_get_nonexistent_game_price_by_id(sample_repo):
    game_id = 999
    game_price = sample_repo.get_price_by_id(game_id)
    assert game_price is None

def test_search_nonexistent_game_by_title(sample_repo):
    games_found = sample_repo.search_games("Nonexistent Game")
    assert len(games_found) == 0

def test_search_games_by_nonexistent_genre_name(sample_repo):
    genre_name = "Nonexistent Genre"
    games_found = sample_repo.get_games_by_genre(genre_name)
    assert len(games_found) == 0




