# Write your MySQL query statement below
WITH cte AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as row_value FROM Person
)

DELETE FROM Person WHERE id in (SELECT id FROM cte WHERE row_value > 1)