select c.customer_id
from customer_transactions as c
where 
(
    select datediff(
        (select max(transaction_date) from customer_transactions 
        where c.customer_id = customer_id), 
        (select min(transaction_date) from customer_transactions 
        where c.customer_id = customer_id))
) >= 30 
and
(
    (select count(*) from customer_transactions where customer_id = c.customer_id and transaction_type = 'refund') / (select count(*) from customer_transactions where customer_id = c.customer_id)
) < 0.2
group by customer_id
having count(*) > 2
order by customer_id ASC; 
