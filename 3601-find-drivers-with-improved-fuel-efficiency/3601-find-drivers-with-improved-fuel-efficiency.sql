SELECT
d.driver_id, d.driver_name,
(
        ROUND(((select sum(distance_km / fuel_consumed) from trips 
        where MONTH(trip_date) <= 6 and driver_id = d.driver_id) / (select count(*) from trips where MONTH(trip_date) <= 6 and driver_id = d.driver_id)), 2)
    
) as first_half_avg, 
(
    ROUND(((select sum(distance_km / fuel_consumed) from trips 
        where MONTH(trip_date) > 6 and driver_id = d.driver_id) / (select count(*) from trips where MONTH(trip_date) > 6 and driver_id = d.driver_id)), 2)
) as second_half_avg, 
(
    select ROUND((((select sum(distance_km / fuel_consumed) from trips 
        where MONTH(trip_date) > 6 and driver_id = d.driver_id) / (select count(*) from trips where MONTH(trip_date) > 6 and driver_id = d.driver_id)) - ((select sum(distance_km / fuel_consumed) from trips 
        where MONTH(trip_date) <= 6 and driver_id = d.driver_id) / (select count(*) from trips where MONTH(trip_date) <= 6 and driver_id = d.driver_id))), 2)
) as efficiency_improvement
from drivers as d
group by driver_id
having first_half_avg != 0 and second_half_avg != 0 and efficiency_improvement > 0
order by efficiency_improvement DESC, driver_name ASC;
