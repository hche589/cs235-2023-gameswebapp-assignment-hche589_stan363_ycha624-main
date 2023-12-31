from flask import Blueprint, render_template, request, flash, redirect, url_for

import games.adapters.repository as repo
import games.browse.services as services

# Configure Blueprint.
browse_blueprint = Blueprint('games_bp', __name__)

GAMES_PER_PAGE = 15  # Display 15 games per page

@browse_blueprint.route('/browse', methods=['GET'])
@browse_blueprint.route('/browse/page/<int:page_num>', methods=['GET'])
def browse_games(page_num=1):  # default to page 1
    num_games = services.get_number_of_games(repo.repo_instance)
    games_on_page = services.get_paginated_games(repo.repo_instance, page_num)
    all_genres = repo.repo_instance.get_all_genres()
    return render_template(
        'browse.html',
        title=f'Browse Games | CS235 Game Library',
        heading='Browse Games',
        games=games_on_page,
        num_games=num_games,
        current_page=page_num,
        genres=all_genres,
        context='all',
        current_genre='',
    )

@browse_blueprint.route('/browse/genre/<genre_name>', methods=['GET'])
@browse_blueprint.route('/browse/genre/<genre_name>/page/<int:page_num>', methods=['GET'])
def browse_games_by_genre(genre_name, page_num=1):
    games_by_genre = services.get_paginated_games_by_genre(repo.repo_instance, genre_name, page_num)
    num_games = len(repo.repo_instance.get_games_by_genre(genre_name))
    all_genres = repo.repo_instance.get_all_genres()
    return render_template(
        'browse.html',
        title=f'Browse Games by {genre_name} | CS235 Game Library',
        heading=f'Browse Games by {genre_name}',
        games=games_by_genre,
        num_games=num_games,
        current_page=page_num,
        genres=all_genres,
        context='genre',
        current_genre=genre_name
    )

@browse_blueprint.route('/search', methods=['GET'])
def search_games():
    search_type = request.args.get('search_type')
    query = request.args.get('query')

    try:
        if search_type == "title":
            games = services.search_games_by_title(repo.repo_instance, query)
        elif search_type == "id":
            games = services.search_games_by_id(repo.repo_instance, int(query))
        elif search_type == "price":
            games = services.search_games_by_price(repo.repo_instance, float(query))
        else:
            games = []
    except ValueError:
        games = []


    return render_template(
        'search_result.html',
        title=f'Search Results | CS235 Game Library',
        heading=f'Search Results for "{query}"',
        games=games,
        num_games=len(games),
        current_page=1  # or adjust if you want search results to be paginated
    )



@browse_blueprint.route('/game/<int:game_id>', methods=['GET'])
def show_game_detail(game_id):
    title = services.get_title_by_id(repo.repo_instance, game_id)
    url = services.get_url_by_id(repo.repo_instance, game_id)
    description = services.get_description_by_id(repo.repo_instance, game_id)
    release_date = services.get_date_by_id(repo.repo_instance, game_id)
    price = services.get_price_by_id(repo.repo_instance, game_id)
    return render_template(
        'gameDescription.html',
        title=title,
        game_id=game_id,
        description = description,
        url = url,
        release_date = release_date,
        price = price,
    )
