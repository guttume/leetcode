# Write your MySQL query statement below
with cte as (
    select *, count(1) over(partition by employee_id) as department_count from Employee
)

select  employee_id, department_id from cte where department_count = 1 or primary_flag = "Y" 