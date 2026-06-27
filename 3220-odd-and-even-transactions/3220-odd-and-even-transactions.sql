SELECT
t.transaction_date, 
(
    IFNULL((select sum(amount) from transactions
    where transaction_date = t.transaction_date and 
    MOD(amount, 2) = 1), 0)
) as odd_sum, 
(
    IFNULL((select sum(amount) from transactions
    where transaction_date = t.transaction_date and 
    MOD(amount, 2) = 0), 0)
) as even_sum
from transactions as t
group by transaction_date
order by transaction_date ASC; 