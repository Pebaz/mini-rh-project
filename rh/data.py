import pandas as pd

def load_data():
	"""
	It is assumed that the movie data is located in the `res` folder.

	a.groupby('director_name').agg({'profit' : ['sum']}).sort_values(('profit', 'sum'), ascending=False)[:10]
	genres = {a for i in a.genres for a in i.split('|')}
	a.loc[a.genres.str.contains('Action')].agg({'profit' : ['sum']})
	profits = {i : float(a.loc[a.genres.str.contains(i)].agg({'profit' : ['sum']}).profit) for i in g }

	genres_by_profit = dict(sorted(profits.items(), key=lambda x: x[1], reverse=True))

	genres_by_profit = pd.DataFrame(profits.values(), index=profits.keys(), columns=['profit']).sort_values('profit', ascending=False)
	"""
	raw = pd.read_csv('res/moviedata.csv')
	raw['profit'] = raw['gross'] - raw['budget']
	return raw


DATA = load_data()


def get_top_10_genres_by_profit():
	"""
	"""
	global DATA

	genres = {a for i in DATA.genres for a in i.split('|')}

	profits = {
		i :
		float(DATA.loc[
			DATA.genres.str.contains(i)
		].agg({'profit' : ['sum']}).profit)
		for i in genres
	}

	genres_by_profit = pd.DataFrame(
		profits.values(),
		index=profits.keys(),
		columns=['profit']
	).sort_values('profit', ascending=False)

	return [(i, p) for i, p in genres_by_profit[:10].iterrows()]


def get_top_10_actors_by_profit():
	"""
	"""
	global DATA

	actors = {
		d for i in
		[DATA.actor_1_name, DATA.actor_2_name, DATA.actor_3_name]
		for d in i
	}

	profits = {
		actor :
		float(DATA.loc[
			(DATA.actor_1_name == actor) |
			(DATA.actor_2_name == actor) |
			(DATA.actor_3_name == actor)
		].agg({'profit' : ['sum']}).profit)
		for actor in actors
	}

	actors_by_profit = pd.DataFrame(
		profits.values(),
		index=profits.keys(),
		columns=['profit']
	).sort_values('profit', ascending=False)

	return [(i, p) for i, p in actors_by_profit[:10].iterrows()]


def get_top_10_directors_by_profit():
	"""
	"""
	global DATA

	raw = DATA.groupby(
		'director_name'
	).agg(
		{'profit' : ['sum']}
	).sort_values(
		('profit', 'sum'),
		ascending=False
	)

	return [(i, p) for i, p in raw[:10].iterrows()]
