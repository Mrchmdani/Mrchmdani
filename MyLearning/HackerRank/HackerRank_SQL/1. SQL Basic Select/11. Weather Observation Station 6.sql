/*
OUTPUT:
city names start with vowel (a, e, i, o, u) and cannot contain duplicate
*/

SELECT DISTINCT(city)
FROM station
WHERE city REGEXP '^[aeiou]'    #'^' this symbol mean 'start with ...'

/*
MS SQL can also use this:

SELECT city
FROM station
WHERE city LIKE '[aeiou]%'      #'%' this symbol mean 'anything after with ...'
*/