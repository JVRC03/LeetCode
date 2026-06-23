SELECT 
e.employee_id, 
(
    select 
        case
            when 0 = (select count(*) from Employee where employee_id = e.employee_id and primary_flag = 'Y')
             then (select min(department_id) from Employee where employee_id = e.employee_id)
            else
                (select min(department_id) from Employee where employee_id = e.employee_id and primary_flag = 'Y')
        end
) as department_id
from Employee as e
group by employee_id; 