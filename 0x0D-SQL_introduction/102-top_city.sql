-- Script that displays the top 3 cities with the highest average temperatures during July and August in descending order.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3;
