/*
OUTPUT:
city names both start and end with vowel (a, e, i, o, u) and cannot contain duplicate
*/

SELECT DISTINCT(city)
FROM station
WHERE city REGEXP '^[aeiou]' AND city REGEXP '[aeiou]$'

/*
MS SQL can also use this:

SELECT DISTINCT(city)
FROM station
WHERE city LIKE '[aeiou]%' AND city LIKE '%[aeiou]'
*/
