# Write your MySQL query statement below
SELECT
	m.NAME 
FROM
	Employee e
	JOIN Employee m ON m.id = e.managerID 
GROUP BY
	m.id 
HAVING
	count( e.id ) >= 5