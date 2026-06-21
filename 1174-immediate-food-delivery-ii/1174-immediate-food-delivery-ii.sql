SELECT 
    ROUND(
    ((   
        select count(em) from 
        (
            select delivery_id as em from Delivery
            group by customer_id
            having min(order_date) = min(customer_pref_delivery_date) 
            order by order_date ASC
        ) jvrc
    ) / (select count(distinct customer_id) from Delivery))
    *100, 2) as immediate_percentage;
