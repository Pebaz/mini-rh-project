"""
Test queries for:

 * Num rows returned
 * Row content
 * Row ordering
"""

from test_common import *


def test_get_top_10_genres_by_profit_length():
    assert len(top_10_genres_by_profit) == 10


def test_get_top_10_actors_by_profit_length():
    assert len(top_10_actors_by_profit) == 10


def test_get_top_10_directors_by_profit_length():
    assert len(top_10_directors_by_profit) == 10


def test_get_top_10_genres_by_profit_content():
    gold = [
        ('Comedy', 12401933708.0),
        ('Adventure', 10754333579.0),
        ('Family', 9725838150.0),
        ('Romance', 8802850372.0),
        ('Fantasy', 8739141427.0),
        ('Thriller', 5379318545.0),
        ('Action', 5166341649.0),
        ('Mystery', 4017680245.0),
        ('Music', 3901466892.0),
        ('Biography', 1924604134.0)
    ]

    data = top_10_genres_by_profit

    assert data == gold
    

def test_get_top_10_actors_by_profit_content():
    gold = [
        ('Harrison Ford', 2039816335.0),
        ('Scarlett Johansson', 1764843253.0),
        ('Robert Downey Jr.', 1755540754.0),
        ('Tom Hanks', 1728647243.0),
        ('Morgan Freeman', 1434558613.0),
        ('Bradley Cooper', 1230992553.0),
        ('Steve Carell', 1191617363.0),
        ('Jennifer Lawrence', 1185706024.0),
        ('John Ratzenberger', 1144861113.0),
        ('Tom Cruise', 1133488721.0)
    ]

    data = top_10_actors_by_profit

    assert data == gold
    

def test_get_top_10_directors_by_profit_content():
    gold = [
        ('Steven Spielberg', 2486332231.0),
        ('George Lucas', 1386641480.0),
        ('James Cameron', 1199625910.0),
        ('Joss Whedon', 1000886628.0),
        ('Chris Columbus', 941707624.0),
        ('Peter Jackson', 900969279.0),
        ('Tim Burton', 824275480.0),
        ('Christopher Nolan', 808227576.0),
        ('Jon Favreau', 769381547.0),
        ('Francis Lawrence', 755501971.0)
    ]

    data = top_10_directors_by_profit

    assert data == gold
    

def test_get_top_10_genres_by_profit_ordering():
    data = top_10_genres_by_profit
    assert sorted(data, key=lambda x: x[1], reverse=True) == data
    

def test_get_top_10_actors_by_profit_ordering():
    data = top_10_actors_by_profit
    assert sorted(data, key=lambda x: x[1], reverse=True) == data
    

def test_get_top_10_directors_by_profit_ordering():
    data = top_10_directors_by_profit
    assert sorted(data, key=lambda x: x[1], reverse=True) == data
