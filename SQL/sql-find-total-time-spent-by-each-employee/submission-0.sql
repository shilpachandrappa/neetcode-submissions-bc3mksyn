-- Write your query below
SELECT event_day AS day, emp_id, SUM(out_time - in_time) as total_time
FROM employees
GROUP BY emp_id, event_day
ORDER BY day