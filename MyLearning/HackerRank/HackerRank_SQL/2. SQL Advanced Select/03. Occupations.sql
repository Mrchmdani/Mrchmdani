/*
1. Pivot occupation column
2. sort name ASC and displayed underneath it's occupation
3. column doctor, professor, singer, actor
4. print NULL when there are no more names corresponding to an occupation
*/

SELECT MIN(doctor),
    MIN(professor),
    MIN(singer),
    MIN(actor)
FROM (SELECT ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name),
     CASE WHEN occupation = 'Doctor' THEN name END AS Doctor,
     CASE WHEN occupation = 'Professor' THEN name END AS Professor,
     CASE WHEN occupation = 'Singer' THEN name END AS Singer,
     CASE WHEN occupation = 'Actor' THEN name END AS Actor
     FROM occupations
     ) rowtable
     GROUP BY row