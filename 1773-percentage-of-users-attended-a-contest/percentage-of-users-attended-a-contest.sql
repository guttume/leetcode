# Write your MySQL query statement below
SELECT
    contest_id,
    ROUND(COUNT(user_id) * 100.0 / u.total_users, 2) AS percentage
FROM
    Register,
    (SELECT COUNT(1) as total_users from users) as u
GROUP BY
    contest_id
ORDER BY
    percentage DESC,
    contest_id ASC;