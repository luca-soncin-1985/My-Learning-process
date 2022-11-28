select first_name, last_name, city, order_details
from customers
left join orders
on customers.id = orders.cust_id
order by 1, 4;
