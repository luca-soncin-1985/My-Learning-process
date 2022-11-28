select first_name, salary
from employee
WHERE salary > (
    SELECT salary
    from employee
    where manager_id = id);
