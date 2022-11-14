/*
OUTPUT:
city names do not start and end with vowel (a, e, i, o, u) and cannot contain duplicate
*/

SELECT DISTINCT(city)
FROM station
WHERE city NOT REGEXP '^[aeiou]' AND city NOT REGEXP '[aeiou]$'

/*
MS SQL can also use this:

SELECT DISTINCT(city)
FROM station
WHERE city NOT LIKE '[aeiou]%' AND city NOT LIKE '%[aeiou]'
*/