# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Customer
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | customer_id | int     |
# MAGIC | product_key | int     |
# MAGIC +-------------+---------+
# MAGIC This table may contain duplicates rows. 
# MAGIC customer_id is not NULL.
# MAGIC product_key is a foreign key (reference column) to Product table.
# MAGIC  
# MAGIC
# MAGIC Table: Product
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | product_key | int     |
# MAGIC +-------------+---------+
# MAGIC product_key is the primary key (column with unique values) for this table.
# MAGIC  
# MAGIC
# MAGIC Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Customer table:
# MAGIC +-------------+-------------+
# MAGIC | customer_id | product_key |
# MAGIC +-------------+-------------+
# MAGIC | 1           | 5           |
# MAGIC | 2           | 6           |
# MAGIC | 3           | 5           |
# MAGIC | 3           | 6           |
# MAGIC | 1           | 6           |
# MAGIC +-------------+-------------+
# MAGIC Product table:
# MAGIC +-------------+
# MAGIC | product_key |
# MAGIC +-------------+
# MAGIC | 5           |
# MAGIC | 6           |
# MAGIC +-------------+
# MAGIC Output: 
# MAGIC +-------------+
# MAGIC | customer_id |
# MAGIC +-------------+
# MAGIC | 1           |
# MAGIC | 3           |
# MAGIC +-------------+
# MAGIC Explanation: 
# MAGIC The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 4034 ms
# MAGIC <h3> Beats: </h3> 24.57%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC /* Write your T-SQL query statement below */
# MAGIC
# MAGIC with cte as
# MAGIC (
# MAGIC   select 
# MAGIC     customer_id, 
# MAGIC     product_key, 
# MAGIC     count(product_key) over (partition by customer_id order by product_key) as uniqueProductPurchase
# MAGIC   from Customer
# MAGIC   group by customer_id, product_key
# MAGIC )
# MAGIC select customer_id
# MAGIC from cte
# MAGIC where uniqueProductPurchase = (select count(distinct product_key) from Product)
