# Write your MySQL query statement below
-- WITH cte AS (
--     SELECT *, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as row_value FROM Person
-- )

-- DELETE FROM Person WHERE id in (SELECT id FROM cte WHERE row_value > 1)

delete p1 from person p1,person p2 
where p1.email=p2.email and p1.id>p2.id;