/*
OUTPUT:
SUM LAT_N

lat_n > 38.7880
lat_n < 137.2345
round to 4 decimal
*/

SELECT TRUNCATE(SUM(lat_n), 4)      #TRUNCATE() same with ROUND() but without rounded up/down
FROM station
WHERE lat_n > 38.7880 AND lat_n < 137.2345