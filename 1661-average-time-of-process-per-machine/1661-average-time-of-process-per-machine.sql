select a.machine_id, 
round(
    (
        (select sum(timestamp) from Activity where activity_type = 'end' and machine_id = a.machine_id)
                                                    -
        (select sum(timestamp) from Activity where activity_type = 'start' and machine_id = a.machine_id)
    )
/  (select count(distinct process_id) where machine_id = a.machine_id)
, 3) as processing_time
from Activity as a
group by machine_id; 