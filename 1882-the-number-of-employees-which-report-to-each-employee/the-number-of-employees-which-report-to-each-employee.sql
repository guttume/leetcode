# Write your MySQL query statement below
SELECT   m.employee_id,
         m.name,
         Count(e.employee_id) AS reports_count,
         Round(Avg(e.age))    AS average_age
FROM     employees e
JOIN     employees m
ON       e.reports_to = m.employee_id
GROUP BY m.employee_id 
ORDER BY m.employee_id