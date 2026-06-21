select 
d.name as Department, e.name as Employee, e.salary as Salary
from Employee as e
inner join Department as d
on e.departmentId = d.id
where e.salary = (
    select max(salary) from Employee where departmentId = d.id
);