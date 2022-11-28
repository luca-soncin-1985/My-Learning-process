select worker_title 
from worker w 
join title t 
on w.worker_id = t.worker_ref_id
where salary = (
    SELECT MAX(salary)
    from worker);
