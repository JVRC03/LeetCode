select
s.store_id, s.store_name, s.location, 
(select product_name from inventory where price = MAX(i.price)) as most_exp_product,
(select product_name from inventory where price = MIN(i.price)) as cheapest_product,
ROUND((select quantity from inventory where price = MIN(i.price) ) / (select quantity from inventory where price = MAX(i.price)), 2) as imbalance_ratio
from stores as s
INNER JOIN inventory as i
on s.store_id = i.store_id
group by i.store_id
having 
    COUNT(distinct(i.product_name)) > 2 and 
    (select quantity from inventory where price = MAX(i.price) and i.store_id = store_id ) < (select quantity from inventory where price = MIN(i.price) and i.store_id = store_id)
ORDER BY imbalance_ratio DESC, s.store_name ASC;