# Write your MySQL query statement below
SELECT
    p.project_id,
    ROUND(AVG(e.experience_years), 2) as average_years
FROM Project p
    LEFT JOIN Employee e on e.employee_id = p.employee_id
GROUP BY p.project_id