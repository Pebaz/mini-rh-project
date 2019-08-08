with all_genres (genre) as (
	with split(word, str) as (
		select
			'', genres || '|'
		from
			moviedata
		union all
		select
			substr(str, 0, instr(str, '|')),
			substr(str, instr(str, '|') + 1)
		from
            split
        where
            str != ''
	) select
        word
    from
        split
    where
        word != ''
    group by
        word
) select
    genre, sum(gross - budget) as Profit
from
    all_genres join moviedata on instr(genres, genre) > 0
group by
    genre
order by
    Profit desc
limit
    10;