# Write your MySQL query statement below
with cte as (
    SELECT
        order_date,
        customer_pref_delivery_date,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) as seq
    FROM Delivery
)

SELECT
    ROUND((SUM(IF(order_date = customer_pref_delivery_date, 1, 0)) / count(1)) * 100, 2) as immediate_percentage
FROM cte
    where seq = 1