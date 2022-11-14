/*
OUTPUT:
smalest  lat_n
lat n > 38.7780
round to 4 decimal
*/

SELECT ROUND(MIN(lat_n), 4)
FROM station
WHERE lat_n > 38.7780