-- Databricks notebook source
-- MAGIC %md
-- MAGIC <h5> ROBLEM DESCRIPTION </h5>
-- MAGIC Products
-- MAGIC
-- MAGIC +------------------+---------+
-- MAGIC | Column Name      | Type    |
-- MAGIC +------------------+---------+
-- MAGIC | product_id       | int     |
-- MAGIC | product_name     | varchar |
-- MAGIC | product_category | varchar |
-- MAGIC +------------------+---------+
-- MAGIC product_id is the primary key (column with unique values) for this table.
-- MAGIC This table contains data about the company's products.
-- MAGIC  
-- MAGIC
-- MAGIC Table: Orders
-- MAGIC
-- MAGIC +---------------+---------+
-- MAGIC | Column Name   | Type    |
-- MAGIC +---------------+---------+
-- MAGIC | product_id    | int     |
-- MAGIC | order_date    | date    |
-- MAGIC | unit          | int     |
-- MAGIC +---------------+---------+
-- MAGIC This table may have duplicate rows.
-- MAGIC product_id is a foreign key (reference column) to the Products table.
-- MAGIC unit is the number of products ordered in order_date.
-- MAGIC  
-- MAGIC
-- MAGIC Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.
-- MAGIC
-- MAGIC Return the result table in any order.
-- MAGIC
-- MAGIC The result format is in the following example.
-- MAGIC
-- MAGIC  
-- MAGIC
-- MAGIC Example 1:
-- MAGIC
-- MAGIC Input: 
-- MAGIC Products table:
-- MAGIC +-------------+-----------------------+------------------+
-- MAGIC | product_id  | product_name          | product_category |
-- MAGIC +-------------+-----------------------+------------------+
-- MAGIC | 1           | Leetcode Solutions    | Book             |
-- MAGIC | 2           | Jewels of Stringology | Book             |
-- MAGIC | 3           | HP                    | Laptop           |
-- MAGIC | 4           | Lenovo                | Laptop           |
-- MAGIC | 5           | Leetcode Kit          | T-shirt          |
-- MAGIC +-------------+-----------------------+------------------+
-- MAGIC Orders table:
-- MAGIC +--------------+--------------+----------+
-- MAGIC | product_id   | order_date   | unit     |
-- MAGIC +--------------+--------------+----------+
-- MAGIC | 1            | 2020-02-05   | 60       |
-- MAGIC | 1            | 2020-02-10   | 70       |
-- MAGIC | 2            | 2020-01-18   | 30       |
-- MAGIC | 2            | 2020-02-11   | 80       |
-- MAGIC | 3            | 2020-02-17   | 2        |
-- MAGIC | 3            | 2020-02-24   | 3        |
-- MAGIC | 4            | 2020-03-01   | 20       |
-- MAGIC | 4            | 2020-03-04   | 30       |
-- MAGIC | 4            | 2020-03-04   | 60       |
-- MAGIC | 5            | 2020-02-25   | 50       |
-- MAGIC | 5            | 2020-02-27   | 50       |
-- MAGIC | 5            | 2020-03-01   | 50       |
-- MAGIC +--------------+--------------+----------+
-- MAGIC Output: 
-- MAGIC +--------------------+---------+
-- MAGIC | product_name       | unit    |
-- MAGIC +--------------------+---------+
-- MAGIC | Leetcode Solutions | 130     |
-- MAGIC | Leetcode Kit       | 100     |
-- MAGIC +--------------------+---------+
-- MAGIC Explanation: 
-- MAGIC Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
-- MAGIC Products with product_id = 2 is ordered in February a total of 80.
-- MAGIC Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
-- MAGIC Products with product_id = 4 was not ordered in February 2020.
-- MAGIC Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Run Time: </h3> 367 ms
-- MAGIC <h3> Beats: </h3> 95.98%
-- MAGIC <h3> Complexity: </h3> O(NLogN)

-- COMMAND ----------

/* Write your T-SQL query statement below */
with T1 as
(
-- Select product_id and total_sale from the subquery
select product_id,total_sale
from(
-- Calculate total_sale for each product_id within the specified date range
select product_id,sum(unit) over (partition by product_id order by product_id) as total_sale
 from Orders 
 where order_date between '2020-02-01' and '2020-02-29') a
-- Filter products with total_sale greater than or equal to 100
 where total_sale >=100
-- Group by product_id and total_sale
 group by product_id,total_sale
) 
-- Select product_name and total_sale (renamed as unit) from the join of T1 and Products
select T2.product_name, T1.total_sale as unit
from T1
-- Join T1 with Products on product_id
inner join Products T2
on T1.product_id = T2.product_id
