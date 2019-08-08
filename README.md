# mini-rh-project


The following is an [IMDB movie dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset/data) available via Kaggle:
https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset/data

The column names in this dataset should be more or less self-descriptive. Some of the key
columns that pertain to this mini-project are: ‘actor_1_name’, ‘actor_2_name’, ‘actor_3_name’,
‘director_name’, ‘budget’ and ‘gross’. You can make assumptions about these names as you
see fit in case they do not seem descriptive enough.

The task requires the following (Note: please use any libraries that you see fit, if applicable, for
the following steps):

    1. Import the file into a local db
    2. Then write functions in Python to perform the following:
         1. Load the relevant data from the db in Step 1 into your program :
         2. For this data, compute the top 10 genres in decreasing order by their profitability. Note: You could (but are not required to) compute profitability as simply as:
              1. ‘gross’ - ’budget’ or
              2. (‘gross’ - ‘budget’)/’budget’
              3. Anything advanced that you can think of
         3. Return the top 10 actors or directors in decreasing order by their profitability (use any definition you choose for profitability using the above guidance).
         4. Bonus questions (Note: If you choose to do any of the bonus questions below, any one question is more than adequate):
              1. Choice 1: Find the best actor, director pairs (up to 10) that have the highest IMDB_ratings, if there are indeed any such pairs.
              2. Choice 2: Any interesting questions that you would like to work on if you would (for e.g. imdb_score, actor facebook_likes
              3. Choice 3: Build a REST API to return an actor’s information (simple text output)
    3. Write tests for your functions. Note: This is an important step for this project.
    4. Commit code to a git repo (gitlab or github) and send us a link to it.
    5. Also document your steps, libraries used and any instructions.

**Note**: Please feel free to make assumptions as you see fit. If you are unable to finish the
mini-project for any reason (for instance if there were time constraints or personal reasons why),
please document the methodology you would take.