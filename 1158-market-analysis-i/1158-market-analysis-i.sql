SELECT
u.user_id as buyer_id, u.join_date,
(
    IFNULL(
        (select count(*) from Orders
        where buyer_id = u.user_id and order_date like '2019%')
    , 0)
) as orders_in_2019
from Users as u;