/*
1. print hacker_id, name, total score is sum of maximum score of all challenges ORDER BY total score DESC
2. IF more than one hacker achieved the same total score, then ORDER BY hacker id
3. EXCLUDE total score = 0
*/

SELECT hacker_id, name, SUM(total_score) total
FROM (
    SELECT h.hacker_id, h.name, MAX(s.score) total_score
    FROM hackers h
    INNER JOIN submissions s ON h.hacker_id = s.hacker_id
    GROUP BY 1, 2, challenge_id
    ) data
GROUP BY 1, 2
HAVING total > 0
ORDER BY total DESC, hacker_id