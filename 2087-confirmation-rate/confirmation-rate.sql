# Write your MySQL query statement below
SELECT u.user_id,
    ROUND(SUM(IF(c.action = "confirmed", 1, 0))/ COUNT(u.user_id), 2) as confirmation_rate
FROM Signups u 
    LEFT JOIN Confirmations c on u.user_id = c.user_id
GROUP BY u.user_id