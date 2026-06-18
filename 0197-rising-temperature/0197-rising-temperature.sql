select id
from Weather as w
where temperature > (select max(temperature) from Weather as e where e.recordDate = w.recordDate- interval 1 day)
order by recordDate;