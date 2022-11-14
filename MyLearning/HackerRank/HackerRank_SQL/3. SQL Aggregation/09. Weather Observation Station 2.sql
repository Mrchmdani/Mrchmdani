/*
OUTPUT:
SUM LAT_N values, rounded to scale 2 decimal
SUM LONG_W values, rounded to scale 2 decimal
*/

SELECT ROUND(SUM(lat_n), 2), ROUND(SUM(long_w), 2)
FROM station