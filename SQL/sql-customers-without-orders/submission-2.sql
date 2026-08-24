-- Write your query below
SELECT c.name as name
FROM customers c 
 WHERE c.id not in 
(SELECT customer_id FROM  orders  )