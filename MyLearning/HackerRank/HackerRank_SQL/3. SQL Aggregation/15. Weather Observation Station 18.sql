
/*
Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.
a happens to equal the minimum value in Northern Latitude (LAT_N in STATION). x1
b happens to equal the minimum value in Western Longitude (LONG_W in STATION). y1
c happens to equal the maximum value in Northern Latitude (LAT_N in STATION). x2
d happens to equal the maximum value in Western Longitude (LONG_W in STATION). y2
Query the Manhattan Distance between points  and  and round it to a scale of 4 decimal places.

Formula Manhattan Distance:
In a plane with p1 at (x1, y1) and p2 at (x2, y2), 
it is |x1 - x2| + |y1 - y2|

#"| |" symbol mean absolute (always positive), so we used ABS()
*/

SELECT ROUND(
            ABS(
                (MIN(lat_n)-MAX(lat_n))
                +
                (MIN(long_w)-MAX(long_w))
                )
            , 4)
FROM station