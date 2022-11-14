/*
OUTPUT:
total population

district = California
*/

SELECT SUM(population)
FROM city
WHERE district = 'California'