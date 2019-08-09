import test_common
from rh.query import *


def test_get_top_10_genres_by_profit_length():
    assert len(get_top_10_genres_by_profit()) == 10


def test_get_top_10_actors_by_profit_length():
    assert len(get_top_10_actors_by_profit()) == 10


def test_get_top_10_directors_by_profit_length():
    assert len(get_top_10_directors_by_profit()) == 10


def test_get_top_10_genres_by_profit_content():
    gold = [
        ('Comedy', 12832689231),
        ('Family', 9770609611),
        ('Adventure', 9756087677),
        ('Romance', 8262484517),
        ('Fantasy', 8186508252),
        ('Thriller', 4385951879),
        ('Action', 4157220813),
        ('Music', 4108048753),
        ('Mystery', 3855634936),
        ('Sport', 1969231354)
    ]

    data = get_top_10_genres_by_profit()

    assert data == gold
    

def test_get_top_10_actors_by_profit_content():
    gold = [
        ('Harrison Ford', 2033216335),
        ('Tom Hanks', 1728647243),
        ('Scarlett Johansson', 1353980855),
        ('Robert Downey Jr.', 1352261207),
        ('Morgan Freeman', 1330234126),
        ('Steve Carell', 1264597471),
        ('Bradley Cooper', 1247001056),
        ('Jennifer Lawrence', 1185706024),
        ('John Ratzenberger', 1144861113),
        ('Tom Cruise', 1106455078)
    ]

    data = get_top_10_actors_by_profit()

    assert data == gold
    

def test_get_top_10_directors_by_profit_content():
    gold = [
        ('Steven Spielberg', 2451332231),
        ('George Lucas', 1386641480),
        ('James Cameron', 1199625910),
        ('Joss Whedon', 1000886628),
        ('Chris Columbus', 941707624),
        ('Peter Jackson', 900969279),
        ('Tim Burton', 824275480),
        ('Christopher Nolan', 808227576),
        ('Jon Favreau', 769381547),
        ('Francis Lawrence', 755501971)
    ]

    data = get_top_10_directors_by_profit()

    assert data == gold
    

def test_get_top_10_genres_by_profit_ordering():
    data = get_top_10_genres_by_profit()
    assert sorted(data, key=lambda x: x[1], reverse=True) == data
    

def test_get_top_10_actors_by_profit_ordering():
    data = get_top_10_actors_by_profit()
    assert sorted(data, key=lambda x: x[1], reverse=True) == data
    

def test_get_top_10_directors_by_profit_ordering():
    data = get_top_10_directors_by_profit()
    assert sorted(data, key=lambda x: x[1], reverse=True) == data
