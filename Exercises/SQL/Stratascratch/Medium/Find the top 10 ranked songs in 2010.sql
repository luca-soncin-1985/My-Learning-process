select year_rank, group_name, song_name
from billboard_top_100_year_end
where year = 2010
group by 3
order by year_rank
limit 10;
