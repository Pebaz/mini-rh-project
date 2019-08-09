# mini-rh-project

Made by Samuel Wilder, 8/8/2019 for Red Hat.

### Installation

```bash
$ pip install -r requirements.txt
```

### Usage

```bash
# Help Screen
$ python main.py

# Output Top 10 Genres, Actors, and Directors in Decreasing Order by Profitability
$ python main.py cli

# Launch Web Server
$ python main.py web
```

### Run Tests

```bash
$ pytest
```

### Example Routes

[`/actor/Harrison%20Ford`](http://localhost:8000/actor/Harrison%20Ford)

[`/top10/directors`](http://localhost:8000/top10/directors)

[`/top10/actors`](http://localhost:8000/top10/actors)

[`/top10/genres`](http://localhost:8000/top10/genres)

### Notes

* As per instructions, the `actors` API route returns a simple text output in Markdeep format.

