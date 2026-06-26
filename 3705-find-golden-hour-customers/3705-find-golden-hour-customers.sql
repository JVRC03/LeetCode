SELECT
customer_id, 
(
    select count(*) from restaurant_orders
    where customer_id = r.customer_id
) as total_orders, 
(
ROUND(((
    select count(*) from restaurant_orders where (customer_id = r.customer_id)
    and ((hour(order_timestamp) >= 11 and (hour(order_timestamp) < 14) or ((hour(order_timestamp) = 14) and minute(order_timestamp) = 0)) or 
    (hour(order_timestamp) >= 18 and (hour(order_timestamp) < 21) or ((hour(order_timestamp) = 21) and minute(order_timestamp) = 0)))
) / (select count(*) from restaurant_orders
    where customer_id = r.customer_id ))
* 100)) as peak_hour_percentage, 
(
    IFNULL(ROUND((select avg(order_rating) from restaurant_orders
    where customer_id = r.customer_id), 2), 0)
) as average_rating
from restaurant_orders as r
group by customer_id
having total_orders >= 3 and average_rating >= 4 and 
(
    IFNULL(((select count(*) from restaurant_orders 
    where customer_id = r.customer_id and 
    order_rating IS NOT NULL)), 0)
) >= 
(total_orders / 2) 
and 
(
    ( select count(*) from restaurant_orders 
      where (customer_id = r.customer_id)
      and ((hour(order_timestamp) >= 11 
      and (hour(order_timestamp) < 14) or 
      ((hour(order_timestamp) = 14) and minute(order_timestamp) = 0)) 
      or (hour(order_timestamp) >= 18 and (hour(order_timestamp) < 21) 
      or ((hour(order_timestamp) = 21) and minute(order_timestamp) = 0)))
      ) / total_orders
) 
>= 0.6
order by average_rating DESC, customer_id DESC; 
