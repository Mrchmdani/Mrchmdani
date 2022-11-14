/*
OUTPUT:
names of all continent
average city population rounded down
*/

SELECT co.continent, FLOOR(AVG(ci.population))
FROM city ci
INNER JOIN country co ON ci.countrycode = co.code
GROUP BY 1