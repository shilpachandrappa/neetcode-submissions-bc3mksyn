-- Write your query below
WITH CTE AS (
SELECT t.account , SUM(t.amount) as balance
FROM transactions t
JOIN users u ON  u.account = t.account 
GROUP BY t.account)
SELECT u.name, c.balance FROM CTE c
JOIN users u ON u.account =  c.account WHERE c.balance > 10000
