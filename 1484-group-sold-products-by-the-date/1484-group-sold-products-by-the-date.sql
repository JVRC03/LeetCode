select 
a.sell_date, count(distinct product) as num_sold, 
(select group_concat(distinct product separator ',') from Activities where sell_date = a.sell_date) as products
from Activities as a
group by sell_date;