SELECT
s.user_id, 
(
    select min(plan_name) from subscription_events
    where s.user_id = user_id and event_date = (
        select max(event_date) from subscription_events where user_id = s.user_id
    )
) as current_plan, 
(
    select min(monthly_amount) from subscription_events
    where s.user_id = user_id and event_date = (
        select max(event_date) from subscription_events where user_id = s.user_id
    )
) as current_monthly_amount, 
(
    select max(monthly_amount) from subscription_events where s.user_id = user_id
) as max_historical_amount, 
(
    select datediff(max(event_date), min(event_date)) from subscription_events
    group by user_id
    having user_id = s.user_id 
) as days_as_subscriber
from subscription_events as s
group by user_id
having 0 = IFNULL((select count(*) from subscription_events 
where user_id = s.user_id and event_type = 'cancel'), 0) and 
1 <= IFNULL((select count(*) from subscription_events where user_id = s.user_id and event_type = 'downgrade'), 0) and days_as_subscriber >= 60 and
((current_monthly_amount / max_historical_amount) * 100) < 50
order by days_as_subscriber DESC, user_id ASC;