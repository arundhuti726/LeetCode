# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Products
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | product_id    | int     |
# MAGIC | new_price     | int     |
# MAGIC | change_date   | date    |
# MAGIC +---------------+---------+
# MAGIC (product_id, change_date) is the primary key (combination of columns with unique values) of this table.
# MAGIC Each row of this table indicates that the price of some product was changed to a new price at some date.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.
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
# MAGIC Products table:
# MAGIC +------------+-----------+-------------+
# MAGIC | product_id | new_price | change_date |
# MAGIC +------------+-----------+-------------+
# MAGIC | 1          | 20        | 2019-08-14  |
# MAGIC | 2          | 50        | 2019-08-14  |
# MAGIC | 1          | 30        | 2019-08-15  |
# MAGIC | 1          | 35        | 2019-08-16  |
# MAGIC | 2          | 65        | 2019-08-17  |
# MAGIC | 3          | 20        | 2019-08-18  |
# MAGIC +------------+-----------+-------------+
# MAGIC Output: 
# MAGIC +------------+-------+
# MAGIC | product_id | price |
# MAGIC +------------+-------+
# MAGIC | 2          | 50    |
# MAGIC | 1          | 35    |
# MAGIC | 3          | 10    |
# MAGIC +------------+-------+

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 852 ms
# MAGIC <h3> Beats: </h3> 99.01%
# MAGIC <h3> Complexity: </h3> O(n log n)

# COMMAND ----------

-- Define a common table expression (CTE) named 'cte'
with cte as
(
    -- Select product_id and new_price from the subquery
    select product_id, new_price  
    from
    (
        -- Select product_id, new_price, change_date, and rank them by change_date in descending order
        select 
        product_id,
        new_price,
        change_date,
        dense_rank() over (partition by product_id order by change_date desc) as prd_rank
        from Products
        -- Filter records where change_date is on or before '2019-08-16'
        where change_date <= '2019-08-16'
    ) a
    -- Filter to get the most recent price change for each product
    where prd_rank = 1
)
-- Select product_id and price from the Products table and the CTE
select 
t1.product_id as product_id, 
-- Use COALESCE to replace NULL prices with 10
coalesce(t2.new_price, 10) as price
from Products t1
-- Perform a left join between Products and the CTE on product_id
left join cte t2
on t1.product_id = t2.product_id
-- Group by product_id and new_price to get the final result
group by t1.product_id, t2.new_price
