/*
OUTPUT:
greatest value lat_n
lat_n < 137.2345
truncate 4 decimal
*/

SELECT TRUNCATE(MAX(lat_n), 4)
FROM station
WHERE lat_n < 137.2345