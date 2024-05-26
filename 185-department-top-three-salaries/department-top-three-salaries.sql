# Write your MySQL query statement below
with cte as (
    select departmentId, salary, name, dense_rank() over (partition by departmentId order by salary desc) as r from Employee
)

select d.name as Department, cte.name as Employee, cte.salary as Salary from cte join Department d on cte.departmentId = d.id where cte.r <= 3