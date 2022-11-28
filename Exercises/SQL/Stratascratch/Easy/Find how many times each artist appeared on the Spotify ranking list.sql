select artist, count(artist) as times 
from spotify_worldwide_daily_song_ranking 
group by artist
order by times desc;
