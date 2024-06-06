# Write your MySQL query statement below
with cte as (
select person_id, person_name, weight, turn, sum(weight) over(order by turn) as cumulative_weight from Queue
)

select person_name from cte where cumulative_weight <= 1000 order by turn desc limit 1