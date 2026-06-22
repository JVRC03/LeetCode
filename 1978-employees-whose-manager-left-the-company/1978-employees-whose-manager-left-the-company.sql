select e.employee_id
from Employees as e
where (e.salary < 30000) and (e.manager_id is not NULL) and IFNULL(
    (select employee_id from Employees where employee_id = e.manager_id)
    , e.employee_id
) = e.employee_id order by e.employee_id;