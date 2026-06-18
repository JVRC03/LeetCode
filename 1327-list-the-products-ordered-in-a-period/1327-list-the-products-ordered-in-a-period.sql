SELECT 
P.product_name, sum(O.unit) as unit
FROM PRODUCTS AS P
INNER JOIN ORDERS AS O
ON p.product_id = o.product_id
where o.order_date like '2020-02-%'
group by o.product_id
having sum(unit) >= 100;
