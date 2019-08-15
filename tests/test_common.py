"""
This needs to be imported on every test file so that the test files can import
modules from the `rh` package.
"""

import sys

sys.path.append('.')

from rh.data import *

top_10_genres_by_profit = get_top_10_genres_by_profit()
top_10_actors_by_profit = get_top_10_actors_by_profit()
top_10_directors_by_profit = get_top_10_directors_by_profit()
