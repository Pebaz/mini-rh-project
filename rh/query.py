from pathlib import Path
import sqlite3 as sql


def query(sql_file, *args):
	"""
	Query the `res/moviedata.db` SQLite3 database using the given SQL file.

	Assumes SQL files are stored in the `res` directory.

	Args:
		sql_file(str): the code to execute.
	
	Returns:
		A list of rows containing tuples containing the result set's column
		data.
	"""
	db = sql.connect('res/moviedata.db')
	cursor = db.cursor()
	sql_code = (Path('res') / sql_file).read_text()
	cursor.execute(sql_code, args)
	all_rows = cursor.fetchall()
	db.close()
	return all_rows


def get_top_10_genres_by_profit():
	"""
	Query the `res/moviedata.db` SQLite3 database for the top 10 genres sorted
	by profitability.

	Returns:
		Up to 10 lists of rows containing tuples containing the result set's
		column data.
	"""
	return query('top_10_genres_by_profit.sql')


def get_top_10_actors_by_profit():
	"""
	Query the `res/moviedata.db` SQLite3 database for the top 10 actors sorted
	by profitability.

	Returns:
		Up to 10 lists of rows containing tuples containing the result set's
		column data.
	"""
	return query('top_10_actors_by_profit.sql')


def get_top_10_directors_by_profit():
	"""
	Query the `res/moviedata.db` SQLite3 database for the top 10 directors
	sorted by profitability.

	Returns:
		Up to 10 lists of rows containing tuples containing the result set's
		column data.
	"""
	return query('top_10_directors_by_profit.sql')


def get_actor_info(name):
	"""
	Get all movies that the given actor was in.

	Queries the `actor_1_name`, `actor_2_name`, and `actor_3_name` fields to
	check for presence within movie.

	Args:
		name(str): the name of the actor to query for.

	Returns:
		A list of rows containing tuples containing the result set's column
		data.
	"""
	return query('actor_info.sql', name, name, name)
