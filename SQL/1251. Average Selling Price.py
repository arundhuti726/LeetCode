# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Prices
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | product_id    | int     |
# MAGIC | start_date    | date    |
# MAGIC | end_date      | date    |
# MAGIC | price         | int     |
# MAGIC +---------------+---------+
# MAGIC (product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
# MAGIC Each row of this table indicates the price of the product_id in the period from start_date to end_date.
# MAGIC For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
# MAGIC  
# MAGIC
# MAGIC Table: UnitsSold
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | product_id    | int     |
# MAGIC | purchase_date | date    |
# MAGIC | units         | int     |
# MAGIC +---------------+---------+
# MAGIC This table may contain duplicate rows.
# MAGIC Each row of this table indicates the date, units, and product_id of each product sold. 
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. If a product does not have any sold units, its average selling price is assumed to be 0.
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
# MAGIC Prices table:
# MAGIC +------------+------------+------------+--------+
# MAGIC | product_id | start_date | end_date   | price  |
# MAGIC +------------+------------+------------+--------+
# MAGIC | 1          | 2019-02-17 | 2019-02-28 | 5      |
# MAGIC | 1          | 2019-03-01 | 2019-03-22 | 20     |
# MAGIC | 2          | 2019-02-01 | 2019-02-20 | 15     |
# MAGIC | 2          | 2019-02-21 | 2019-03-31 | 30     |
# MAGIC +------------+------------+------------+--------+
# MAGIC UnitsSold table:
# MAGIC +------------+---------------+-------+
# MAGIC | product_id | purchase_date | units |
# MAGIC +------------+---------------+-------+
# MAGIC | 1          | 2019-02-25    | 100   |
# MAGIC | 1          | 2019-03-01    | 15    |
# MAGIC | 2          | 2019-02-10    | 200   |
# MAGIC | 2          | 2019-03-22    | 30    |
# MAGIC +------------+---------------+-------+
# MAGIC Output: 
# MAGIC +------------+---------------+
# MAGIC | product_id | average_price |
# MAGIC +------------+---------------+
# MAGIC | 1          | 6.96          |
# MAGIC | 2          | 16.96         |
# MAGIC +------------+---------------+
# MAGIC Explanation: 
# MAGIC Average selling price = Total Price of Product / Number of products sold.
# MAGIC Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
# MAGIC Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 538 ms
# MAGIC <h3> Beats: </h3> 54.88
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Select product_id and calculate the average price */
# MAGIC select 
# MAGIC     t1.product_id, 
# MAGIC     /* Calculate the average price using COALESCE to handle nulls and ROUND to format the result */
# MAGIC     coalesce(round(cast(sum(t1.price * t2.units) as float) / sum(t2.units), 2),0) as average_price 
# MAGIC from 
# MAGIC     Prices t1
# MAGIC /* Perform a left join between Prices and UnitsSold tables */
# MAGIC left join 
# MAGIC     UnitsSold t2
# MAGIC /* Join on product_id and ensure purchase_date is within the price date range */
# MAGIC on 
# MAGIC     t1.product_id = t2.product_id
# MAGIC     and 
# MAGIC     t2.purchase_date between t1.start_date and t1.end_date
# MAGIC /* Group by product_id to aggregate the results */
# MAGIC group by 
# MAGIC     t1.product_id
# MAGIC /* Order the results by product_id */
# MAGIC order by t1.product_id
