/*
OUTPUT:
finding difference between miscalcuation (using salaries with any zeros removed) and the actual average salary.
actual - miscalculated average monthly salaries

round it up to the next integer

note: i can't use ceiling or ceil on this question. The value can't be roundup above 0,5 and rather it goes down to 0 or round down.
~weird~
*/

SELECT
    ROUND(AVG(salary))
    -
    ROUND(AVG(REPLACE(salary,'0','')))
FROM employees