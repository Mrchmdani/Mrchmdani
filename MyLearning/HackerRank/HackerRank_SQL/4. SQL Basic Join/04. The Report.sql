/*
output:
1. name, grade, mark
2. filter out student that have grade < 8
3. order by grade DESC
4. if there are student that have same grade(8-10), order by name ASC
5. grade that lower than 8 must be NULL as their name, and list DESC
6. if there are student that have same grade(1-7), order by marks ASC
*/

#IF clause
SELECT IF(g.grade >= 8, s.name, NULL),
    g.grade, 
    s.marks
FROM students s
JOIN grades g
ON s.marks BETWEEN g.min_mark AND g.max_mark
ORDER BY grade DESC, name ASC, marks ASC

/*
#CASE CLAUSE
SELECT CASE WHEN grade <= 7 THEN name = NULL
    WHEN grade >= 8 THEN name END,              #simpler : CASE WHEN grade <= 7 THEN name = NULL ELSE s.name END
    g.grade, 
    s.marks
FROM students s
JOIN grades g
ON s.marks BETWEEN g.min_mark AND g.max_mark
ORDER BY grade DESC, name ASC, marks ASC

#Learning purpose for me trying subquery
SELECT CASE WHEN grade <= 7 THEN name = NULL
            WHEN grade >= 8 THEN name END,
        grade,
        marks
FROM (
      SELECT s.name, g.grade, s.marks
      FROM students s
      JOIN grades g
      ON s.marks BETWEEN g.min_mark AND g.max_mark
    ) data
ORDER BY grade DESC, name ASC, marks ASC
*/