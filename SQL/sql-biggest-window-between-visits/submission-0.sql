-- Write your query below select user_id , MAX(days_since_previous) AS biggest_window from cte2 GROUP BY user_id

WITH cte AS 
(SELECT user_id , visit_date , LEAD(visit_date) over(PARTITION BY user_id ORDER BY visit_date) AS prev_date FROM user_visits),
CTE2 AS(
SELECT user_id , visit_date, prev_date ,CASE 
WHEN prev_date IS NULL THEN    '2021-1-1'   - visit_date
ELSE  prev_date- visit_date  END  AS days_since_previous 
from cte)
select user_id , MAX(days_since_previous) AS biggest_window from cte2 GROUP BY user_id
