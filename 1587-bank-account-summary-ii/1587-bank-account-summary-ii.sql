select 
u.name as NAME, sum(t.amount) as BALANCE
from Users as u
left join Transactions as t
on u.account = t.account
group by t.account
having BALANCE > 10000; 
