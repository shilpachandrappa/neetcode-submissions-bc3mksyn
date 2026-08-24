SELECT employee_id , CASE
 WHEN ( employee_id % 2) != 0 AND left(name,1) !='M' THEN salary 
 ELSE 0 
 end AS bonus
FROM employees 
ORDER BY employee_id 
 