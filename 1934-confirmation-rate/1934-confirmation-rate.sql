select 
s.user_id as user_id, 
ROUND(

    IFNULL(((   select count(*) from Confirmations where user_id = s.user_id    )
                                    - 
    (   select count(*) from Confirmations where user_id = s.user_id and action = 'timeout'  ))

                                    /
    (    select count(*) from Confirmations where user_id = s.user_id    ), 0)

, 2) as confirmation_rate
from Signups as s;