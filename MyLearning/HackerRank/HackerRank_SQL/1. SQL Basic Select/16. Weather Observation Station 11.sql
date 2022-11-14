/*
OUTPUT:
city names either do not start and do not end with vowel (a, e, i, o, u) and cannot contain duplicate
*/

SELECT DISTINCT(city)
FROM station
WHERE city NOT REGEXP '^[aeiou]' OR city NOT REGEXP '[aeiou]$'

/*
MS SQL can also use this:

SELECT DISTINCT(city)
FROM station
WHERE city NOT LIKE '[aeiou]%' OR city NOT LIKE '%[aeiou]'
*/
