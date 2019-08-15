"""
Usage: 

Help Screen
$ python main.py

Output Top 10 Genres, Actors, or Directors in Decreasing Order by Profitability
$ python main.py cli

Launch Web Server
$ python main.py web
"""

import sys  # Command Line Arguments & Program Exit Code


def main(args):
	categories = 'genres', 'actors', 'directors'

	if 'web' in args:
		from rh.routes import app
		app.run('0.0.0.0', 8000)

	elif 'cli' in args:

		# from rh.query import (
		# 	get_top_10_genres_by_profit,
		# 	get_top_10_actors_by_profit,
		# 	get_top_10_directors_by_profit
		# )

		from rh.data import (
			load_data,
			get_top_10_genres_by_profit,
			get_top_10_actors_by_profit,
			get_top_10_directors_by_profit,
		)

		# If no arguments are supplied to `cli`, show all categories
		print_all = not any([i in args for i in categories])

		if 'genres' in args or print_all:
			print('Top 10 Genres by Profitability:')
			for i in get_top_10_genres_by_profit():
				print('   ', i[0])

		if 'actors' in args or print_all:
			print('\nTop 10 Actors by Profitability:')
			for i in get_top_10_actors_by_profit():
				print('   ', i[0])

		if 'directors' in args or print_all:
			print('\nTop 10 Directors by Profitability:')
			for i in get_top_10_directors_by_profit():
				print('   ', i[0])

	else:
		print('Usage:')
		print('    python main.py web')
		print('    python main.py cli [genres | actors | directors]')

	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
