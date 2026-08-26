-- Write your query below
SELECT 
LEAST(from_id, to_id) as person1,
GREATEST(from_id, to_id) as person2,
COUNT(*) AS call_count,
SUM(duration) AS total_duration
FROM calls
GROUP BY 1,2