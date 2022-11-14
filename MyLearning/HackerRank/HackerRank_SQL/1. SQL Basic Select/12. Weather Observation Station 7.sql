/*
OUTPUT:
city names that end with vowel (a, e, i, o, u) and cannot contain duplicate
*/

SELECT DISTINCT(city)
FROM station
WHERE city REGEXP '[aeiou]$'    #'$' this symbol mean 'end with ...'

/*
MS SQL can also use this:

SELECT DISTINCT(city)
FROM station
WHERE city LIKE '%[aeiou]'      #'%' this symbol mean 'anything ending with ...'
*/