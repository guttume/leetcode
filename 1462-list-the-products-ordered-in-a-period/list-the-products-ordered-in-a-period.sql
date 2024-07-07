# Write your MySQL query statement below
WITH cte AS (
SELECT 
    product_id,
    SUM(unit) as total_units
FROM Orders
WHERE MONTH(order_date) = 2 AND YEAR(order_date) = 2020
GROUP BY product_id
HAVING total_units >= 100
)

SELECT product_name, total_units as unit from cte join Products p on p.product_id = cte.product_id