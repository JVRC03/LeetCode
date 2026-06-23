select 
a.activity_date as day,
(
    select count(distinct user_id) from Activity
    where (activity_date = a.activity_date)
) as active_users
from Activity as a
where a.activity_date <= '2019-07-27' and (a.activity_date > ('2019-07-27' - INTERVAL 30 day))
group by activity_date
order by a.activity_date;