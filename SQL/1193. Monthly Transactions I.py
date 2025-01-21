# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Transactions
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | id            | int     |
# MAGIC | country       | varchar |
# MAGIC | state         | enum    |
# MAGIC | amount        | int     |
# MAGIC | trans_date    | date    |
# MAGIC +---------------+---------+
# MAGIC id is the primary key of this table.
# MAGIC The table has information about incoming transactions.
# MAGIC The state column is an enum of type ["approved", "declined"].
# MAGIC  
# MAGIC
# MAGIC Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC The query result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Transactions table:
# MAGIC +------+---------+----------+--------+------------+
# MAGIC | id   | country | state    | amount | trans_date |
# MAGIC +------+---------+----------+--------+------------+
# MAGIC | 121  | US      | approved | 1000   | 2018-12-18 |
# MAGIC | 122  | US      | declined | 2000   | 2018-12-19 |
# MAGIC | 123  | US      | approved | 2000   | 2019-01-01 |
# MAGIC | 124  | DE      | approved | 2000   | 2019-01-07 |
# MAGIC +------+---------+----------+--------+------------+
# MAGIC Output: 
# MAGIC +----------+---------+-------------+----------------+--------------------+-----------------------+
# MAGIC | month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
# MAGIC +----------+---------+-------------+----------------+--------------------+-----------------------+
# MAGIC | 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
# MAGIC | 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
# MAGIC | 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
# MAGIC +----------+---------+-------------+----------------+--------------------+-----------------------+

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 3874 ms
# MAGIC <h3> Beats: </h3> 16.13%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Write your T-SQL query statement below */
# MAGIC SELECT month, -- Select the month column
# MAGIC country, -- Select the country column
# MAGIC total_transactions as trans_count, -- Select total_transactions and alias it as trans_count
# MAGIC approved_count, -- Select approved_count column
# MAGIC trans_total_amount, -- Select trans_total_amount column
# MAGIC approved_total_amount -- Select approved_total_amount column
# MAGIC FROM
# MAGIC (
# MAGIC SELECT 
# MAGIC     CONCAT(YEAR(trans_date),'-',Format(cast(MONTH(trans_date) as INT),'00')) as month, -- Create month column by concatenating year and month
# MAGIC     country, -- Select country column
# MAGIC     COUNT(*) AS total_transactions, -- Count total transactions and alias it as total_transactions
# MAGIC     SUM(amount) AS trans_total_amount, -- Sum of amount column and alias it as trans_total_amount
# MAGIC     SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count, -- Count approved transactions and alias it as approved_count
# MAGIC     SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount -- Sum of approved transaction amounts and alias it as approved_total_amount
# MAGIC FROM Transactions 
# MAGIC GROUP BY CONCAT(YEAR(trans_date),'-',Format(cast(MONTH(trans_date) as INT),'00')), country -- Group by month and country
# MAGIC )A
# MAGIC order by country desc,month -- Order by country in descending order and month
