select s.name as name
from SalesPerson as s
where 'RED' != 
IFNULL((
    select c.name from Company as c
    where c.com_id = IFNULL((select com_id from Company where name like 'RED'), -100) 
                                           and 
    c.com_id = (select com_id from Orders where com_id = c.com_id and sales_id = s.sales_id)
), 0)