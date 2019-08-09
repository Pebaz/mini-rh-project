"""
"""

from flask import Flask, render_template
from rh.query import *

app = Flask(__name__)

@app.route('/actor/<name>')
def actor(name):
	"""
	Test http://localhost:8000/actor/Harrison%20Ford
	"""
	actor = get_actor_info(name)
	column_names = [
		'color',
		'director_name',
		'num_critic_for_reviews',
		'duration',
		'director_facebook_likes',
		'actor_3_facebook_likes',
		'actor_2_name',
		'actor_1_facebook_likes',
		'gross',
		'genres',
		'actor_1_name',
		'movie_title',
		'num_voted_users',
		'cast_total_facebook_likes',
		'actor_3_name',
		'facenumber_in_poster',
		'plot_keywords',
		'movie_imdb_link',
		'num_user_for_reviews',
		'language',
		'country',
		'content_rating',
		'budget',
		'title_year',
		'actor_2_facebook_likes',
		'imdb_score',
		'aspect_ratio',
		'movie_facebook_likes'
	]

	columns = [
		0, 1, 2, 3
	]

	if not actor:
		return render_template('not-found.j2')

	return render_template(
		'actor.j2',
		actor_name=name,
		actor=actor,
		column_names=column_names,
		columns=columns
	)


@app.route('/top10/<category>')
def top10(category):
	if category == 'genres':
		return render_template(
			'top10.j2',
			category_name=category,
			category=get_top_10_genres_by_profit()
		)

	elif category == 'actors':
		return render_template(
			'top10.j2',
			category_name=category,
			category=get_top_10_actors_by_profit()
		)

	elif category == 'directors':
		return render_template(
			'top10.j2',
			category_name=category,
			category=get_top_10_directors_by_profit()
		)

	else:
		return render_template('not-found.j2')
