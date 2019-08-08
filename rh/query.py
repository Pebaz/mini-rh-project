from pathlib import Path
import sqlite3 as sql


def query(sql_file):
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
	cursor.execute((Path('res') / sql_file).read_text())
	all_rows = cursor.fetchall()
	db.close()
	return all_rows
