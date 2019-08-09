"""
"""

import sys  # Command Line Arguments & Program Exit Code


def main(args):
	if 'web' in args:
		from rh.routes import app
		app.run('0.0.0.0', 8000)

	elif 'cli' in args:
		from rh.query import (
			get_top_10_genres_by_profit,
			get_top_10_actors_by_profit,
			get_top_10_directors_by_profit
		)

		print('Top 10 Genres by Profitability:')
		for i in get_top_10_genres_by_profit():
			print('   ', i[0], i[1])

		print('\nTop 10 Actors by Profitability:')
		for i in get_top_10_actors_by_profit():
			print('   ', i[0], i[1])

		print('\nTop 10 Directors by Profitability:')
		for i in get_top_10_directors_by_profit():
			print('   ', i[0], i[1])

	else:
		print('Usage:\n    python main.py [web | cli]')

	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
