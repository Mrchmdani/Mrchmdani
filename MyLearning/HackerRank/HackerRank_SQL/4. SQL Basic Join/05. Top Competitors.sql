/*
1. print hacker_id, name
2. hacker who achieved full score more than one challenge
3. order by total number of challenges
4. if more than one hacker full score ORDER BY hacker_id

HAVING COUNT(h.hacker_id) >= 1
ORDER BY s.score DESC
*/

SELECT 
    h.hacker_id, 
    h.name
FROM 
    hackers h
    INNER JOIN submissions s ON h.hacker_id = s.hacker_id
    INNER JOIN challenges c ON c.challenge_id = s.challenge_id
    INNER JOIN difficulty d ON c.difficulty_level = d.difficulty_level AND s.score = d.score
GROUP BY 
    1, 
    2
HAVING 
    COUNT(1) > 1
ORDER BY 
    COUNT(1) DESC, h.hacker_id;