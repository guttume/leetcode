# Write your MySQL query statement below
with cte as (
select *, LAG(recordDate) OVER(order by recordDate) as prev_d, LAG(temperature) OVER(order by recordDate) as prev from Weather
)

select id from cte where temperature > prev and date_sub(recordDate, INTERVAL 1 DAY) = prev_d