/*
OUTPUT:
Shortest and 
Longest city names
length names

names asc
*/

SELECT city, LENGTH(city)
FROM station
ORDER BY 2, 1
LIMIT 1;
SELECT city, LENGTH(city)
FROM station
ORDER BY 2 DESC, 1
LIMIT 1;