# Write your MySQL query statement below
with cte as (
    select *, RANK() OVER(PARTITION BY product_id ORDER BY year) as sale_row from Sales
)

select product_id, year as first_year, quantity, price from cte where sale_row = 1 