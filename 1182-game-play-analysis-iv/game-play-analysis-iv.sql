# Write your MySQL query statement below
WITH cte AS (
	SELECT
		player_id,
		event_date,
		lead( event_date ) over ( PARTITION BY player_id ORDER BY event_date ) next_date,
		dense_rank() over ( PARTITION BY player_id ORDER BY event_date ) AS rnk 
	FROM
		Activity 
	) SELECT
	round( sum( CASE WHEN datediff( next_date, event_date ) = 1 THEN 1 ELSE 0 END )/ count( DISTINCT player_id ), 2 ) fraction 
FROM
	cte 
WHERE
	rnk = 1