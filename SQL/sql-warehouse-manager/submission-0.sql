-- Write your query below
WITH CTE AS (
SELECT (width * length * height) AS mul , product_id 
FROM products)
SELECT w.name as warehouse_name , SUM(c.mul* w.units) AS volume 
FROM CTE c
JOIN warehouse w ON c.product_id = w.product_id
GROUP BY w.name