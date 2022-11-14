/*
1. print hacker_id, name, total challenges
2. total challenges DESC
3. If more than one student created the same number of challenges, then ORDER BY hacker_id
4. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result
*/

SELECT 
    h.hacker_id,
    h.name,
    COUNT(c.challenge_id) total
FROM hackers h
    INNER JOIN challenges c
    ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total IN (
                  SELECT tb2.t2
                  FROM(
                       SELECT COUNT(challenge_id) t2
                       FROM challenges
                       GROUP BY hacker_id
                      ) tb2
                  GROUP BY tb2.t2
                  HAVING COUNT(tb2.t2)=1
                  ORDER BY tb2.t2 DESC
                )
        OR
        total = (
                  SELECT MAX(tb1.t1)
                  FROM (
                        SELECT COUNT(challenge_id) t1
                        FROM challenges
                        GROUP BY hacker_id
                        ORDER BY t1 DESC
                        ) tb1
                )
ORDER BY total DESC, h.hacker_id

/*
You can use WITH clause for this problem
*/