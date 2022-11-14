/*
OUTPUT:
total earning (salary * months)
maximum total earning
number of employee who have maximum total earning
*/

-- Trying to solve using FROM CLAUSE SUBQUERY for learning purpose
SELECT total_earning, COUNT(employee_id)
FROM(
        SELECT employee_id, (salary*months) as total_earning
        FROM employee
    )  AS total_table
GROUP BY total_earning
ORDER BY total_earning DESC
LIMIT 1

/*
The Simplest

SELECT (salary * months) as earnings,
COUNT(*)
FROM employee
GROUP BY earnings
ORDER BY earnings desc
LIMIT 1
*/