# Write your MySQL query statement below
SELECT
	activity_start.machine_id,
	ROUND(AVG((activity_end.`timestamp` - activity_start.`timestamp`)), 3) as processing_time 
FROM
	( SELECT machine_id, process_id, `timestamp` FROM Activity WHERE Activity.activity_type = "start" ) AS activity_start
	JOIN ( SELECT machine_id, process_id, `timestamp` FROM Activity WHERE Activity.activity_type = "end" ) AS activity_end ON activity_start.machine_id = activity_end.machine_id 
	AND activity_start.process_id = activity_end.process_id
	GROUP BY activity_start.machine_id