/*
OUTPUT:
average population

district = California
*/

SELECT AVG(population)
FROM city
WHERE district = 'California'