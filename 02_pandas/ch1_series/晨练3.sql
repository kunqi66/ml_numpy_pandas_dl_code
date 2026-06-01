SELECT e.ename,e.tel
FROM t_employee e
WHERE e.did IN
(SELECT e.did FROM t_employee e
WHERE e.ename IN ('白露','谢吉娜'))
AND ename NOT IN ('白露','谢吉娜');
/*
UPDATE t_employee SET salary = salary * 1.1
WHERE did = 10;

SELECT o.customer_id, SUM(o.order_amount)
FROM orders o
GROUP BY o.customer_id;
order by SUM(o.order_amount) 

SELECT c.customer_name,o.order_date
FROM customers c INNER JOIN orders o
on  c.customer_id = o.customer_id;


SELECT p.prodyct_name,c.category_name
FROM products p LEFT JOIN category c
on  p.category_id = c.category_id;*/
