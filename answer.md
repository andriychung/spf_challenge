# Summer 2022 Data Science Intern Challenge

## Question 1
On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

### a. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

The average AOV of $3145.13 are caused by the exceptionally high amount $704000 of 18 orders of shop id 42 and user id 607. Looking at AOV per shop, 2 shops are much higher than others, namely shop 42 and 78, with AOV of $235101.49 and $49213.04. Excluding the 2 shops, AOV per shop ranges from $162.85 to $403.55, and the AOV is $299.68 which is more reasonable. Further investigation can be carried out on the accuracy of orders of shops 42 and 78.

### b. What metric would you report for this dataset?

Instead of the average (mean) order value, median can be used as metric.  Median reveals that half of the orders are below median and half of the orders are above, and is not biased by extremes.

### c. What is its value?

Median of order values = $284 (q1.ipynb shows the calculation)


## Question 2

### a. How many orders were shipped by Speedy Express in total?

SQL:
<code>

    SELECT count(1) FROM Orders o join Shippers s on o.ShipperID = s.ShipperID and s.ShipperName = 'Speedy Express';

</code>
Output: 54


### b. What is the last name of the employee with the most orders?

SQL: 
<code>

    select LastName from Employees where employeeid = (select employeeid from Orders o group by employeeid order by count(1) desc limit 1)

</code>
Output: Peacock

### c. What product was ordered the most by customers in Germany?

SQL: 
<code>
    
    select ProductName from products where productid = (

    select p.productid product_count from orders o 
    join customers c on o.customerid = c.customerid and c.country = 'Germany' 
    join orderDetails d on o.orderid = d.orderid
    join products p on p.productid = d.productid
    group by p.productid 
    order by count(1) desc
    limit 1
    )

</code>

Output: Gorgonzola Telino