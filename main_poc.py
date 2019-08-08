'''
select sum(gross - budget) from moviedata where genres like '%Mystery%';
'''

import sys, csv
from collections import OrderedDict

class Movie:
	ALL_GENRES = set()
	ALL_DIRECTORS = set()
	ALL_ACTORS = set()

	def __init__(self, **kwargs):
		# Automatically map keys to object attributes
		self.__dict__ = kwargs

		# Map text to Python objects
		self.genres = self.genres.split('|')
		self.plot_keywords = self.plot_keywords.split('|')

		self.movie_facebook_likes = int(self.movie_facebook_likes or 0)
		self.director_facebook_likes = int(self.director_facebook_likes or 0)
		self.actor_1_facebook_likes = int(self.actor_1_facebook_likes or 0)
		self.actor_2_facebook_likes = int(self.actor_2_facebook_likes or 0)
		self.actor_3_facebook_likes = int(self.actor_3_facebook_likes or 0)
		self.cast_total_facebook_likes = int(self.cast_total_facebook_likes or 0)

		self.gross = int(self.gross or 0)
		self.budget = int(self.budget or 0)
		self.num_voted_users = int(self.num_voted_users)
		self.facenumber_in_poster = int(self.facenumber_in_poster or 0)
		self.imdb_score = float(self.imdb_score)
		self.aspect_ratio = float(self.aspect_ratio or 0)

		actors = [self.actor_1_name, self.actor_2_name, self.actor_3_name]
		self.actors = [i for i in actors if i]

		# Precalculate profitibility
		self.profitibility = self.gross - self.budget

		# Contribute to set of all genres
		for genre in self.genres:
			Movie.ALL_GENRES.add(genre)

		# Contribute to set of all directors
		Movie.ALL_DIRECTORS.add(self.director_name)

		# Contribute to set of all actors
		for name in actors:
			if name:
				Movie.ALL_ACTORS.add(name)


# Load data into memory
print('Loading data...', end='')
sys.stdout.flush()


director_profits = dict()
actor_profits = dict()
genre_profits = dict()
data = []
with open('res/movie_metadata.csv', encoding='utf8') as file:
	reader = iter(csv.reader(file, delimiter=',', quotechar='"'))
	header = next(reader)
	for row in reader:
		movie = Movie(**dict(zip(header, row)))
		data.append(movie)

		director_profits.setdefault(movie.director_name, 0)
		director_profits[movie.director_name] += movie.profitibility

		for name in movie.actors:
			actor_profits.setdefault(name, 0)
			actor_profits[name] += movie.profitibility  # * actor_likes (a1 + a2 + a3)

		for genre in movie.genres:
			genre_profits.setdefault(genre, 0)
			genre_profits[genre] += movie.profitibility

sys.stdout.write('Done\n')

if False:
	foo = dict(sorted(director_profits.items(), key=lambda x: x[1], reverse=True))
	bar = dict(sorted(actor_profits.items(), key=lambda x: x[1], reverse=True))
	baz = dict(sorted(genre_profits.items(), key=lambda x: x[1], reverse=True))
	for i in list(foo.keys())[:10]:
		print(i, foo[i])
	print('-----------\n')
	for i in list(bar.keys())[:10]:
		print(i, bar[i])
	print('-----------\n')
	for i in list(baz.keys())[:10]:
		print(i, baz[i])
	exit()


# -----------------------------------------------------------------------------
'''
select director_name, sum(gross - budget) as profit from moviedata group by director_name order by profit desc limit 10
'''
def director_total_profit(director):
	return sum([i.profitibility for i in data if i.director_name == director])

sys.stdout.write('Collecting director profit...')
sys.stdout.flush()
directors_by_profit = {
	director : director_total_profit(director)
	for director in Movie.ALL_DIRECTORS
}
sys.stdout.write('Done\n')

sys.stdout.write('Sorting directors by profit...')
sys.stdout.flush()
top_directors_by_profit = dict(sorted(directors_by_profit.items(), key=lambda x: x[1], reverse=True))
sys.stdout.write('Done\n')


for director in list(top_directors_by_profit.keys())[:10]:
	sys.stdout.write(f'{director:<30}: {top_directors_by_profit[director]}\n')


# -----------------------------------------------------------------------------
'''
-- Select all Genres
with split(word, str) as (
	select
		'', genres || '|'
	from
		moviedata
	union all
	select
		substr(str, 0, instr(str, '|')),
		substr(str, instr(str, '|') + 1)
	from split where str != ''
) select word from split where word != '' group by word;


-- Profitibility by Genre:
select 'Action', sum(gross - budget) as Profit from moviedata where instr(genres, 'Action') > 0;
select 'Documentary', sum(gross - budget) as Profit from moviedata where instr(genres, 'Documentary') > 0;

-- This may be it:
select 'Action' as foo, * from moviedata where genres like foo;



-- WORKS
-- THIS IS IT!
with all_genres (genre) as (
	with split(word, str) as (
		select
			'', genres || '|'
		from
			moviedata
		union all
		select
			substr(str, 0, instr(str, '|')),
			substr(str, instr(str, '|') + 1)
		from split where str != ''
	) select word from split where word != '' group by word
) select genre, sum(gross - budget) as Profit from all_genres join moviedata on instr(genres, genre) > 0
group by genre
order by Profit desc
limit 10;
'''
# Top 10 Directors by profit

def genre_total_profit(genre):
	return sum([i.profitibility for i in data if genre in i.genres])

sys.stdout.write('Collecting genre profit...')
sys.stdout.flush()
genres_by_profit = {
	genre : genre_total_profit(genre)
	for genre in Movie.ALL_GENRES
}
sys.stdout.write('Done\n')

sys.stdout.write('Sorting genres by profit...')
sys.stdout.flush()
top_genres_by_profit = dict(sorted(genres_by_profit.items(), key=lambda x: x[1], reverse=True))
sys.stdout.write('Done\n')

for genre in list(top_genres_by_profit.keys())[:10]:
	sys.stdout.write(f'{genre:<30}: {top_genres_by_profit[genre]}\n')


# -----------------------------------------------------------------------------
'''
-- Actor Profitibility
select Name, sum(gross - budget) as profit from (
	select actor_1_name as Name, gross, budget from moviedata union
	select actor_2_name as Name, gross, budget from moviedata union
	select actor_3_name as Name, gross, budget from moviedata
) group by Name order by profit desc limit 10
'''
# Top 10 Actors by profit
def actor_total_profit(actor):
	return sum([i.profitibility for i in data if actor in i.actors])

sys.stdout.write('Collecting actor profit...')
sys.stdout.flush()
actors_by_profit = {
	actor : actor_total_profit(actor)
	for actor in Movie.ALL_ACTORS
}
sys.stdout.write('Done\n')

sys.stdout.write('Sorting actor by profit...')
sys.stdout.flush()
top_actors_by_profit = dict(sorted(actors_by_profit.items(), key=lambda x: x[1], reverse=True))
sys.stdout.write('Done\n')

for actor in list(top_actors_by_profit.keys())[:10]:
	sys.stdout.write(f'{actor:<30}: {top_actors_by_profit[actor]}\n')
