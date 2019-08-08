select
    director_name, sum(gross - budget) as Profit
from
    moviedata
group by
    director_name
order by
    Profit desc
limit
    10;