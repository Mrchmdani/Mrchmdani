/*
OUTPUT:
name employee

employee that have salary > 2000
employee < 10 months

sort employee_id asc
*/

SELECT name
FROM employee
WHERE salary > 2000 AND months < 10
ORDER BY employee_id