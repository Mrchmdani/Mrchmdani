
/*
OUTPUT:
long_w based on smalest lat_n
lat_n > 38.7780
round to 4 decimal
*/

#FROM CLAUSE
SELECT ROUND(long_w, 4)
FROM (
    SELECT long_w, MIN(lat_n)
    FROM station
    WHERE lat_n > 38.7780
    GROUP BY 1
    ORDER BY 2
    ) AS min_lat
LIMIT 1

/*
#NO SUBQUERY
SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n > 38.7780
ORDER BY lat_n
LIMIT 1


#WHERE CLAUSE
SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n = (SELECT MIN(lat_n)
       FROM station
       WHERE lat_n > 38.7780)
*/