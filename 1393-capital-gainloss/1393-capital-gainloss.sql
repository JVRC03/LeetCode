Select
s.stock_name, 
(
    (
        select sum(price) from Stocks where operation = 'Sell' and stock_name = s.stock_name
    )
                                        -
    (
        select sum(price) from Stocks where operation = 'Buy' and stock_name = s.stock_name
    )
) as capital_gain_loss
from Stocks as s
group by stock_name;