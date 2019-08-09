"""
Simple web application for viewing database data within a web browser.
"""

from flask import Flask, render_template
from rh.query import *


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    """
	For any other route, show custom 404 error page.

	Args:
		e(error): the error that occurred.

	Returns:
		A simple 404 page in the same style as the rest of the site.
	"""
    return render_template('not-found.j2'), 404


@app.route('/')
def root():
	"""
	Front page of the project.

	Shows some example routes to visit.

	Returns:
		Simple textual output of some example routes.
	"""
	return render_template('root.j2')


@app.route('/actor/<name>')
def actor(name):
	"""
	View relevant data about each movie that an actor appeared in.

	Entire column set is provided for easy future customizations of the columns
	shown.

	Args:
		name(str): the actor's name to lookup in the database.

	Returns:
		Simple textual output of each movie that the actor appeared in.
	"""
	actor = get_actor_info(name)
	
	column_names = [
		'color',
		'Director Name',
		'num_critic_for_reviews',
		'Duration',
		'director_facebook_likes',
		'actor_3_facebook_likes',
		'actor_2_name',
		'actor_1_facebook_likes',
		'Gross',
		'genres',
		'actor_1_name',
		'movie_title',
		'num_voted_users',
		'cast_total_facebook_likes',
		'actor_3_name',
		'facenumber_in_poster',
		'plot_keywords',
		'IMDB Link',
		'num_user_for_reviews',
		'language',
		'country',
		'content_rating',
		'Budget',
		'Title Year',
		'actor_2_facebook_likes',
		'IMDB Score',
		'aspect_ratio',
		'movie_facebook_likes'
	]

	columns = [
		23, 1, 3, 8, -6, -3
	]

	if not actor:
		return render_template('not-found.j2'), 404

	return render_template(
		'actor.j2',
		actor_name=name,
		actor=actor,
		column_names=column_names,
		columns=columns
	)


@app.route('/top10/<category>')
def top10(category):
	"""
	View the top 10 genres, actors, or directors by profitability.

	Profitability is calculated as: `gross` - `budget`.

	Acceptable URL parameters include:
	
	 * /genres
	 * /actors
	 * /directors

	Args:
		category(str): the category to query from the database.

	Returns:
		Simple textual output of the top 10 elements by profitability of the
		selected category.
	"""
	if category in ('genres', 'actors', 'directors'):
		if category == 'genres':
			data = get_top_10_genres_by_profit()
		elif category == 'actors':
			data = get_top_10_actors_by_profit()
		elif category == 'directors':
			data = get_top_10_directors_by_profit()

		return render_template(
			'top10.j2',
			category_name=category,
			category=data
		)

	else:
		return render_template('not-found.j2'), 404
