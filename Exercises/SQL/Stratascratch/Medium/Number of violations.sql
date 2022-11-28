select COUNT(inspection_id) as 'count', year(inspection_date)
from sf_restaurant_health_violations
where violation_id IS NOT NULL
AND business_name = 'Roxanne Cafe'
group by year(inspection_date)
order by 2;
