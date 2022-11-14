/*
OUTPUT:
1. name in occupation asc, followed by each profession first letter and parenthesis with no space. exmpl : name(D)
2. number of occupation in asc with format :
There are a total of [occupation_count] [occupation]s.


SELECT CASE
    WHEN occupation = 'Doctor' THEN CONCAT(name,'(',LEFT(occupation,1),')')
    WHEN occupation = 'Professor' THEN CONCAT(name,'(',LEFT(occupation,1),')')
    WHEN occupation = 'Singer' THEN CONCAT(name,'(',LEFT(occupation,1),')')
    WHEN occupation = 'Actor' THEN CONCAT(name,'(',LEFT(occupation,1),')')
    END
FROM occupations
ORDER BY name;

SELECT CASE
    WHEN occupation = 'Doctor' THEN CONCAT('There are a total of ', COUNT(occupation),' doctors.')
    WHEN occupation = 'Professor' THEN CONCAT('There are a total of ', COUNT(occupation),' professors.')
    WHEN occupation = 'Singer' THEN CONCAT('There are a total of ', COUNT(occupation),' singers.')
    WHEN occupation = 'Actor' THEN CONCAT('There are a total of ', COUNT(occupation),' actors.')
    END
FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation), occupation;
*/

# Simplification
SELECT 
    CONCAT(name,'(',LEFT(occupation, 1),')')
FROM 
    occupations
ORDER BY 
    name;

SELECT 
    CONCAT('There are a total of ', COUNT(occupation),' ', LOWER(occupation),'s.') as total
FROM
    occupations
GROUP BY
    occupation
ORDER BY
    total;