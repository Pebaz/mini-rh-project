"""
Movie dataset query functions.

`load_data` is the generic function used by the other query functions to
parse the CSV data into a Pandas DataFrame.

The functions starting with `get` all return customized data.
"""

from functools import lru_cache
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count
import pandas as pd


@lru_cache(maxsize=1)
def load_data():
    """
    It is assumed that the movie data is located in the `res` folder.

    Since this function is basically acting as a global variable and will
    always take no arguments, an LRU cache will ensure that the csv data is
    only loaded from disk once.

    Returns:
        A Pandas DataFrame containing the movie data from the given CSV file.
    """
    raw = pd.read_csv('res/moviedata.csv')
    raw['profit'] = raw['gross'] - raw['budget']
    return raw


def get_top_10_genres_by_profit():
    """
    Get the 10 most profitible genres within the movie dataset.

    Returns:
        A list of 10 tuples containing the genre name, followed by its profit.
    """
    DATA = load_data()

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
    )

    # Don't create extraneous DataFrames
    genres_by_profit.sort_values('profit', ascending=False, inplace=True)

    return [(i, float(p)) for i, p in genres_by_profit.head(10).iterrows()]


def __get_actor_profit(actor):
    """
    """
    DATA = load_data()
    raw = DATA.loc[
        (DATA.actor_1_name == actor) |
        (DATA.actor_2_name == actor) |
        (DATA.actor_3_name == actor)
    ].agg({'profit' : ['sum']})
    return float(raw.profit)


def get_top_10_actors_by_profit():
    """
    Get the 10 most profitible actors within the movie dataset.

    Returns:
        A list of 10 tuples containing the actor name, followed by its profit.
    """
    DATA = load_data()

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
    )

    # Don't create extraneous DataFrames
    actors_by_profit.sort_values('profit', ascending=False, inplace=True)

    return [(i, float(p)) for i, p in actors_by_profit.head(10).iterrows()]


def get_top_10_directors_by_profit():
    """
    Get the 10 most profitible directors within the movie dataset.

    Returns:
        A list of 10 tuples containing the director name, followed by their
        profit.
    """
    DATA = load_data()

    raw = DATA.groupby(
        'director_name'
    ).agg(
        {'profit' : ['sum']}
    )

    # Don't create extraneous DataFrames
    raw.sort_values(('profit', 'sum'), ascending=False, inplace=True)

    return [(i, float(p)) for i, p in raw.head(10).iterrows()]


def get_actor_info(name):
    """
    Get all movies that the given actor was in.
    Queries the `actor_1_name`, `actor_2_name`, and `actor_3_name` fields to
    check for presence within movie.

    Args:
        name(str): the name of the actor to query for.

    Returns:
        A list containing tuples with the data for each movie that the actor
        appeared in.
    """
    DATA = load_data()

    raw = DATA.loc[
        (DATA.actor_1_name == name) |
        (DATA.actor_2_name == name) |
        (DATA.actor_3_name == name)
    ]

    return [
        tuple(item for item in r) for _, r in raw.iterrows()
    ]
