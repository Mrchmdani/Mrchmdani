/*
OUTPUT:
sum population all cities
continent = Asia
*/

SELECT SUM(ci.population)
FROM city ci
INNER JOIN country co ON ci.countrycode = co.code
WHERE continent = 'Asia'