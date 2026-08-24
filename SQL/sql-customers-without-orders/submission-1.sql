-- Write your query below
SELECT c.name as name
FROM customers c 
 WHERE c.name not in (SELECT c.name as name
FROM customers c 
 JOIN orders o  ON o.customer_id = c.id )