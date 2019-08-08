from rh.query import query


print('Top 10 Genres by Profitability:')
for i in query('top_10_genres_by_profit.sql'):
	print(i[0])

print('\nTop 10 Actors by Profitability:')
for i in query('top_10_actors_by_profit.sql'):
	print(i[0])

print('\nTop 10 Directors by Profitability:')
for i in query('top_10_directors_by_profit.sql'):
	print(i[0])

if __name__ == '__main__':
	pass
