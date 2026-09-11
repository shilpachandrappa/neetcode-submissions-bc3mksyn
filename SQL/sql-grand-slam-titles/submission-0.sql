-- Write your query below
WITH CTE AS
(SELECT wimbledon AS winner
FROM championships
UNION ALL
SELECT fr_open AS winner
FROM championships
UNION ALL
SELECT us_open AS winner
FROM championships
UNION ALL
SELECT au_open AS winner
FROM championships)

SELECT c.winner AS player_id, p.player_name, COUNT(*) AS grand_slams_count
FROM CTE c
JOIN players p on p.player_id = c.winner
GROUP BY p.player_name, c.winner
