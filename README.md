# mini-rh-project

Made by Samuel Wilder, 8/8/2019 for Red Hat.

### Installation

```bash
$ git clone https://github.com/Pebaz/mini-rh-project
$ cd mini-rh-project
$ pip install -r requirements.txt
```

### Usage

```bash
# Help Screen
$ python main.py

# Output Top 10 Genres, Actors, or Directors in Decreasing Order by Profitability
$ python main.py cli
$ python main.py cli genres
$ python main.py cli actors
$ python main.py cli directors

# Launch Web Server
$ python main.py web
```

### Run Tests

```bash
# Just test
$ pytest

# Test with Coverage
$ pytest --cov=rh tests

# Output Coverage Report
$ pytest --cov=rh tests --cov-report=html
```

### Example Routes

[`/`](http://localhost:8000)

[`/actor/Harrison%20Ford`](http://localhost:8000/actor/Harrison%20Ford)

[`/top10/directors`](http://localhost:8000/top10/directors)

[`/top10/actors`](http://localhost:8000/top10/actors)

[`/top10/genres`](http://localhost:8000/top10/genres)

### Libraries Used

* **Flask**: Web application framework.
* **Blinker**: Subscription to Signals in Flask.
* **PyTest**: Unit testing.
* **PyTest-Cov**: Test coverage.
* **Markdeep**: Convert plain text to formatted HTML automatically.

### Notes

* As per instructions, the `actors` API route returns a simple text output in Markdeep format.
* SQL queries were written using the `qmark` parameter style (obtained from `sqlite3.paramstyle`).
