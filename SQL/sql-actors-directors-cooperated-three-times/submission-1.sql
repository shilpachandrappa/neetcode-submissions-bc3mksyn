-- Write your query below
WITH CTE AS
(SELECT COUNT(*) as cnt, actor_id, director_id
FROM actor_director
GROUP BY actor_id,director_id )
SELECT actor_id, director_id  FROM CTE WHERE cnt >= 3