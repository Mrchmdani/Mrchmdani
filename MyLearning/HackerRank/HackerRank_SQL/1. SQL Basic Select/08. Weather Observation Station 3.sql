/*
OUTPUT:
city name exclude duplicate

city that have 'even' id number
*/

SELECT DISTINCT(city)   #city name exclude duplicate
FROM station
WHERE id %2 = 0         #city that have 'even' id number