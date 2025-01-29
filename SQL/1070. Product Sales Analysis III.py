# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Sales
# MAGIC
# MAGIC +-------------+-------+
# MAGIC | Column Name | Type  |
# MAGIC +-------------+-------+
# MAGIC | sale_id     | int   |
# MAGIC | product_id  | int   |
# MAGIC | year        | int   |
# MAGIC | quantity    | int   |
# MAGIC | price       | int   |
# MAGIC +-------------+-------+
# MAGIC (sale_id, year) is the primary key (combination of columns with unique values) of this table.
# MAGIC product_id is a foreign key (reference column) to Product table.
# MAGIC Each row of this table shows a sale on the product product_id in a certain year.
# MAGIC Note that the price is per unit.
# MAGIC  
# MAGIC
# MAGIC Table: Product
# MAGIC
# MAGIC +--------------+---------+
# MAGIC | Column Name  | Type    |
# MAGIC +--------------+---------+
# MAGIC | product_id   | int     |
# MAGIC | product_name | varchar |
# MAGIC +--------------+---------+
# MAGIC product_id is the primary key (column with unique values) of this table.
# MAGIC Each row of this table indicates the product name of each product.
# MAGIC  
# MAGIC
# MAGIC Write a solution to select the product id, year, quantity, and price for the first year of every product sold.
# MAGIC
# MAGIC Return the resulting table in any order.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Sales table:
# MAGIC +---------+------------+------+----------+-------+
# MAGIC | sale_id | product_id | year | quantity | price |
# MAGIC +---------+------------+------+----------+-------+ 
# MAGIC | 1       | 100        | 2008 | 10       | 5000  |
# MAGIC | 2       | 100        | 2009 | 12       | 5000  |
# MAGIC | 7       | 200        | 2011 | 15       | 9000  |
# MAGIC +---------+------------+------+----------+-------+
# MAGIC Product table:
# MAGIC +------------+--------------+
# MAGIC | product_id | product_name |
# MAGIC +------------+--------------+
# MAGIC | 100        | Nokia        |
# MAGIC | 200        | Apple        |
# MAGIC | 300        | Samsung      |
# MAGIC +------------+--------------+
# MAGIC Output: 
# MAGIC +------------+------------+----------+-------+
# MAGIC | product_id | first_year | quantity | price |
# MAGIC +------------+------------+----------+-------+ 
# MAGIC | 100        | 2008       | 10       | 5000  |
# MAGIC | 200        | 2011       | 15       | 9000  |
# MAGIC +------------+------------+----------+-------+

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 2763 ms
# MAGIC <h3> Beats: </h3> 89.98%
# MAGIC <h3> Complexity: </h3>

# COMMAND ----------

/* Write your T-SQL query statement below */
--Process 1 ()
 select product_id,year as first_year,quantity, price
 from(
 select t1.product_id, year,quantity, price,
 rank() over (partition by t1.product_id order by year) as rnk
 from Sales t1
 left join Product t2
 on t1.product_id=t2.product_id) a
 where rnk=1

--Process 2 

select  
Sales.product_id , Sales.year as first_year, quantity, price
from Sales,
 (select product_id, min(year) as year
from Sales
group by product_id ) as t

where Sales.product_id = t.product_id and Sales.year = t.year


