select a.first_name, b.order_date, b.order_details, b.total_order_cost
FROM customers a
JOIN orders b on a.id = b.cust_id
WHERE a.first_name IN ('Jill','Eva')
ORDER BY a.id ASC
