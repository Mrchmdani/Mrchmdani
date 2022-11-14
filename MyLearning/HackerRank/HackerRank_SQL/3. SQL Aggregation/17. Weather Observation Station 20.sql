/*
1. Query median Northern Latitude (lat_n)
2. Round 4 decimal
*/

SELECT ROUND(s.lat_n, 4) 
FROM station s 
WHERE (
    SELECT FLOOR(COUNT(s.id) / 2 )      #count total id 499/2 = 249.5 = 249
    FROM station) = (
        SELECT COUNT(s1.id)             #count total id 499
        FROM station s1 
        WHERE s1.lat_n > s.lat_n
    );