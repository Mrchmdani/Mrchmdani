/*
1. id, age, coins_needed, power
2. minimum gold needed, non evil wand, high power, and age
3. ORDER BY power DESC
4. If one wand have = power, then ORDER BY age DESC
*/

SELECT
    w.id,
    wp.age,
    w.coins_needed,
    w.power
FROM 
    wands w
INNER JOIN
    wands_property wp ON w.code = wp.code
WHERE wp.is_evil = 0 AND w.coins_needed = (
                                           SELECT MIN(coins_needed)
                                           FROM wands w1
                                           INNER JOIN
                                           wands_property wp1 ON w1.code = wp1.code
                                           WHERE w.power = w1.power AND wp.age = wp1.age
                                          )
ORDER BY power DESC, age DESC