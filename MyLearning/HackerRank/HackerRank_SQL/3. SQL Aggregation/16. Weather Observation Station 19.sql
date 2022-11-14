/*
Consider  P1(a,c) and P2(b,d) to be two points on a 2D plane where 
(a,b) are the respective minimum and maximum values of Northern Latitude (LAT_N) and 
(c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points  and  and format your answer to display 4 decimal digits.

Euclidean Distance 2D plane formula:
d(p,q) = root( (q1-p1) power of 2 + (q2-p2) power of 2) )
*/

SELECT ROUND(
            SQRT(
                POWER(MAX(lat_n)-MIN(lat_n), 2) 
                + 
                POWER(MAX(long_w)-MIN(long_w), 2)
                )
            , 4)
FROM station