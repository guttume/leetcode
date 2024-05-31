# Write your MySQL query statement below
select 
*,
if (x + y > z, if(x + z > y, if (z + y > x, "Yes", "No"), "No"), "No") as triangle

from Triangle 