select
    Name, sum(gross - budget) as Profit
from (
	select actor_1_name as Name, gross, budget from moviedata union
	select actor_2_name as Name, gross, budget from moviedata union
	select actor_3_name as Name, gross, budget from moviedata
)
group by
    Name
order by
    Profit desc
limit
    10;
