-- Write your query below
WITH CTE AS (
    SELECT exam_id,student_id,score, MAX(score) OVER(PARTITION BY exam_id 
    ) AS max_score,MIN(score) OVER(PARTITION BY exam_id 
    ) AS min_score  
    FROM exam 
    GROUP BY  exam_id, student_id
),
rankers as (
SELECT  distinct(student_id) FROM CTE where score = max_score or score = min_score)
select distinct(e.student_id) , s.student_name from  exam e 
JOIN student s on s.student_id = e.student_id
where NOT EXISTS(
    SELECT 1 FROM rankers r WHERE r.student_id = e.student_id
)