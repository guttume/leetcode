# Write your MySQL query statement below

with cte as (SELECT *, 
ROW_NUMBER() OVER (order by id) % 2 AS row_id, 
LAG(id) OVER (order by id) as lag_id,
LEAD(id) OVER (order by id) as lead_id
FROM Seat)

select * from (
    select 
CASE WHEN row_id = 0 THEN lag_id ELSE coalesce(lead_id, id) END as id,
student
from cte
) temp order by id
