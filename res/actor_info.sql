select
	*
from
	moviedata
where
	actor_1_name like ? or
	actor_2_name like ? or
	actor_3_name like ?;
