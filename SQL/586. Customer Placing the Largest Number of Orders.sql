-- Databricks notebook source
-- MAGIC %md
-- MAGIC <h5> ROBLEM DESCRIPTION </h5>
-- MAGIC Orders
-- MAGIC
-- MAGIC +-----------------+----------+
-- MAGIC | Column Name     | Type     |
-- MAGIC +-----------------+----------+
-- MAGIC | order_number    | int      |
-- MAGIC | customer_number | int      |
-- MAGIC +-----------------+----------+
-- MAGIC order_number is the primary key (column with unique values) for this table.
-- MAGIC This table contains information about the order ID and the customer ID.
-- MAGIC  
-- MAGIC
-- MAGIC Write a solution to find the customer_number for the customer who has placed the largest number of orders.
-- MAGIC
-- MAGIC The test cases are generated so that exactly one customer will have placed more orders than any other customer.
-- MAGIC
-- MAGIC The result format is in the following example.
-- MAGIC
-- MAGIC  
-- MAGIC
-- MAGIC Example 1:
-- MAGIC
-- MAGIC Input: 
-- MAGIC Orders table:
-- MAGIC +--------------+-----------------+
-- MAGIC | order_number | customer_number |
-- MAGIC +--------------+-----------------+
-- MAGIC | 1            | 1               |
-- MAGIC | 2            | 2               |
-- MAGIC | 3            | 3               |
-- MAGIC | 4            | 3               |
-- MAGIC +--------------+-----------------+
-- MAGIC Output: 
-- MAGIC +-----------------+
-- MAGIC | customer_number |
-- MAGIC +-----------------+
-- MAGIC | 3               |
-- MAGIC +-----------------+
-- MAGIC Explanation: 
-- MAGIC The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
-- MAGIC So the result is customer_number 3.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Run Time: </h3> 872 ms
-- MAGIC <h3> Beats: </h3> 81.48%
-- MAGIC <h3> Complexity: </h3> O(n)
-- MAGIC

-- COMMAND ----------

/* Write your T-SQL query statement below */
select customer_number
from (
  select customer_number, count(*) as totalOrder
  from Orders
  group by customer_number
) a
where totalOrder = (select max(totalOrder) from (select count(*) as totalOrder from Orders group by customer_number) b)


