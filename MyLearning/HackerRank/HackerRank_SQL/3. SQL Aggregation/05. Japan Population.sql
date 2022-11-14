/*
OUTPUT:
sum or total population

countrycode = JPN
*/

SELECT SUM(population)
FROM city
WHERE countrycode = 'JPN'