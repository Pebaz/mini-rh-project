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
	return render_template('actor.j2', actor_name=name, actor=actor)


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
		return render_template('top10.j2', category_name='Not Found')
