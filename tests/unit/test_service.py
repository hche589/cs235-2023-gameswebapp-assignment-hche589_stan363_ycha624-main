import pytest
from games.adapters.memory_repository import MemoryRepository
import games.browse.services as services
from games.domainmodel.model import Genre, Publisher, Game


@pytest.fixture
def empty_repo():
    return MemoryRepository()


@pytest.fixture
def sample_repo():
    repo = MemoryRepository()
    game1 = Game(1, "Game 1")
    game1.release_date = "Mar 12, 2018"
    game1.description = "Description for Game 1"
    game1.url = "https://example.com/game1"
    game1.price = 0.99
    game1.genre = ["Action", "Adventure"]

    game2 = Game(2, "Game 2")
    game2.release_date = "Aug 30, 2023"
    game2.description = "Description for Game 2"
    game2.url = "https://example.com/game2"
    game2.price = 1.99
    game2.genre = ["Adventure"]

    repo.add_game(game1)
    repo.add_game(game2)

    return repo



def test_get_correct_number_of_games(sample_repo):
    num_games = services.get_number_of_games(sample_repo)
    assert num_games == 2


def test_get_paginated_games(sample_repo):
    games = services.get_paginated_games(sample_repo, page_num=1)
    assert len(games) == 2


def test_get_paginated_games_for_pagination2(sample_repo):
    games = services.get_paginated_games(sample_repo, page_num=2)
    assert games == []


def test_get_games_by_nonexistent_genre(sample_repo):
    games = services.get_paginated_games_by_genre(sample_repo, genre_name="Nonexistent Genre", page_num=1)
    assert games == []


def test_search_games_by_genre(sample_repo):
    games = services.get_games_by_genre(sample_repo, genre_name="Action", page_num=10)
    assert len(games) == 0


def test_get_nonexistent_game(sample_repo):
    game = services.get_title_by_id(sample_repo, game_id=999)
    assert game is None


def test_get_date_by_id_nonexistent_game(sample_repo):
    release_date = services.get_date_by_id(sample_repo, game_id=999)
    assert release_date is None


def test_get_description_by_id_nonexistent_game(sample_repo):
    description = services.get_description_by_id(sample_repo, game_id=999)
    assert description is None


def test_get_url_by_id_nonexistent_game(sample_repo):
    url = services.get_url_by_id(sample_repo, game_id=999)
    assert url is None


def test_get_price_by_id_nonexistent_game(sample_repo):
    price = services.get_price_by_id(sample_repo, game_id=999)
    assert price is None


def test_get_games_by_genre_pagination(sample_repo):
    games = services.get_games_by_genre(sample_repo, genre_name="Action", page_num=2)
    assert games == []


def test_search_games_by_title_existing_game(sample_repo):
    games = services.search_games_by_title(sample_repo, "Game")
    assert len(games) == 2
    assert games[0].title == "Game 1"


def test_search_games_by_title_existing_game2(sample_repo):
    games = services.search_games_by_title(sample_repo, "Game 1")
    assert len(games) == 1
    assert games[0].title == "Game 1"


def test_search_games_by_title_nonexistent_game(sample_repo):
    games = services.search_games_by_title(sample_repo, "Nonexistent Game")
    assert len(games) == 0

