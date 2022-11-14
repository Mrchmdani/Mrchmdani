/*
1. print company_code, founder, total lead manager, total senior manager, total  manager, total employee
2. table may contain duplicate record = DISTINCT
3. order by company code ASC
*/

SELECT c.company_code,
       c.founder,
       COUNT(DISTINCT lm.lead_manager_code),
       COUNT(DISTINCT sm.senior_manager_code),
       COUNT(DISTINCT m.manager_code),
       COUNT(DISTINCT e.employee_code)
FROM company c
INNER JOIN lead_manager lm ON c.company_code = lm.company_code
INNER JOIN senior_manager sm ON lm.lead_manager_code = sm.lead_manager_code
INNER JOIN manager m ON sm.senior_manager_code = m.senior_manager_code
INNER JOIN employee e ON m.manager_code = e.manager_code
GROUP BY 1,2

/*
SELECT 
    co.company_code, 
    co.founder,
    COUNT(DISTINCT lm.lead_manager_code),
    COUNT(DISTINCT sm.senior_manager_code),
    COUNT(DISTINCT m.manager_code),
    COUNT(DISTINCT e.employee_code)
FROM company co, lead_manager lm, senior_manager sm, manager m, employee e
WHERE co.company_code = lm.company_code
    AND lm.lead_manager_code = sm.lead_manager_code
    AND sm.senior_manager_code = m.senior_manager_code
    AND m.manager_code = e.manager_code
GROUP BY co.company_code, co.founder
ORDER BY co.company_code;
*/