/*
OUTPUT:
name student

student who score > 75

order by last three character
if student three last name the same then order by id asc
*/

SELECT name
FROM students
WHERE marks > 75
ORDER BY right(name, 3), id asc