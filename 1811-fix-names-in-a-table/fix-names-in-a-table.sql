# Write your MySQL query statement below
SELECT user_id, CONCAT(upper(substr(name, 1, 1)), lower(SUBSTR(name, 2))) as name from Users order by user_id