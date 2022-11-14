/*
OUTPUT:
long_w based on largest lat_n < 137.2345
round to 4 decimal
*/

#FROM CLAUSE
SELECT ROUND(long_w, 4)
FROM (
    SELECT long_w, MAX(lat_n)
    FROM station
    WHERE lat_n < 137.2345
    GROUP BY 1
    ORDER BY 2 DESC
    ) AS max_lat
LIMIT 1

/*
#NO SUBQUERY
SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n < 137.2345
ORDER BY lat_n DESC
LIMIT 1


#WHERE CLAUSE
SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n = (SELECT MAX(lat_n)
       FROM station
       WHERE lat_n < 137.2345)
*/