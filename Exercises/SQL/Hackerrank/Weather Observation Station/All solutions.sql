# Weather Observation Station 1

SELECT city, state
from station;

# Weather Observation Station 2

SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) FROM STATION;

# Weather Observation Station 3

select city
from station
where ID % 2 = 0
group by city;

# Weather Observation Station 4

select COUNT(city) - COUNT(distinct city)
from station;

# Weather Observation Station 5

select city, length(city) from station
order by length(city),city asc
limit 1;
select city, length(city) from station
order by length(city) desc
limit 1;

# Weather Observation Station 6

SELECT DISTINCT city FROM station WHERE city REGEXP "^[aeiou].*";

# Weather Observation Station 7

SELECT DISTINCT city
from station
WHERE city regexp '[a,e,i,o,u]$';

# Weather Observation Station 8

SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[aeiou].*[aeiou]$';

# Weather Observation Station 9

select distinct city
from station
where city not regexp '^[aeiou]';

# Weather Observation Station 10

SELECT DISTINCT city
FROM station
where city NOT REGEXP '[aeiou]$';

# Weather Observation Station 11

select distinct(city)
from station where SUBSTRING(city,1,1) not in ('A','E','I','O','U') or 
SUBSTRING(city,-1,1) not in ('A','E','I','O','U');

# Weather Observation Station 12

SELECT DISTINCT(CITY) FROM STATION WHERE CITY NOT REGEXP '^[aeiou]' AND CITY NOT REGEXP '[aeiou]$';

# Weather Observation Station 13

SELECT CAST(SUM(LAT_N) as decimal(9, 4)) FROM station where LAT_N > 38.7880 and LAT_N < 137.2345;

# Weather Observation Station 14

SELECT CAST(MAX(lat_n) as DECIMAL (20,4))
from station
where lat_n < 137.2345;

# Weather Observation Station 15

SELECT round(long_w, 4)
FROM station
where lat_n = (
    SELECT MAX(lat_n)
    FROM station
    WHERE lat_n < 137.2345
    )
;

# Weather Observation Station 16

SELECT ROUND(MIN(lat_n), 4)
from station
where lat_n > 38.7780 ;

# Weather Observation Station 17

SELECT round(long_w, 4)
from station
where lat_n = (
    select MIN(lat_n)
    from station
    where lat_n > 38.7780)
;

# Weather Observation Station 18

SELECT ROUND(MAX(Lat_N) - MIN(Lat_N) + MAX(Long_W) - MIN(Long_W), 4)
FROM Station;

# Weather Observation Station 19

SELECT
    ROUND(SQRT(
        POWER(MAX(LAT_N)  - MIN(LAT_N),  2)
      + POWER(MAX(LONG_W) - MIN(LONG_W), 2)
    ), 4)
FROM 
    STATION;


