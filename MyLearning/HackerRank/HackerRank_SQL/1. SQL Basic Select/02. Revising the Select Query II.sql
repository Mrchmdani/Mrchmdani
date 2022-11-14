/*
OUTPUT:
name country
countrycode = 'USA'
population larger than 120000

TABLE city
*/

SELECT name
FROM city
WHERE countrycode = 'USA' AND population > 120000