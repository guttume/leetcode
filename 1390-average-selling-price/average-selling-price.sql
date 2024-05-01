# Write your MySQL query statement below
SELECT
    p.product_id, 
    COALESCE(ROUND(SUM(COALESCE(u.units, 0) * p.price) / COALESCE(SUM(COALESCE(u.units, 0)), 0), 2), 0) as average_price
FROM Prices p 
    LEFT JOIN UnitsSold u on p.product_id = u.product_id 
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id
