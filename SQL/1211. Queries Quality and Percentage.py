# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Queries
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | query_name  | varchar |
# MAGIC | result      | varchar |
# MAGIC | position    | int     |
# MAGIC | rating      | int     |
# MAGIC +-------------+---------+
# MAGIC This table may have duplicate rows.
# MAGIC This table contains information collected from some queries on a database.
# MAGIC The position column has a value from 1 to 500.
# MAGIC The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
# MAGIC  
# MAGIC
# MAGIC We define query quality as:
# MAGIC
# MAGIC The average of the ratio between query rating and its position.
# MAGIC
# MAGIC We also define poor query percentage as:
# MAGIC
# MAGIC The percentage of all queries with rating less than 3.
# MAGIC
# MAGIC Write a solution to find each query_name, the quality and poor_query_percentage.
# MAGIC
# MAGIC Both quality and poor_query_percentage should be rounded to 2 decimal places.
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
# MAGIC Queries table:
# MAGIC +------------+-------------------+----------+--------+
# MAGIC | query_name | result            | position | rating |
# MAGIC +------------+-------------------+----------+--------+
# MAGIC | Dog        | Golden Retriever  | 1        | 5      |
# MAGIC | Dog        | German Shepherd   | 2        | 5      |
# MAGIC | Dog        | Mule              | 200      | 1      |
# MAGIC | Cat        | Shirazi           | 5        | 2      |
# MAGIC | Cat        | Siamese           | 3        | 3      |
# MAGIC | Cat        | Sphynx            | 7        | 4      |
# MAGIC +------------+-------------------+----------+--------+
# MAGIC Output: 
# MAGIC +------------+---------+-----------------------+
# MAGIC | query_name | quality | poor_query_percentage |
# MAGIC +------------+---------+-----------------------+
# MAGIC | Dog        | 2.50    | 33.33                 |
# MAGIC | Cat        | 0.66    | 33.33                 |
# MAGIC +------------+---------+-----------------------+
# MAGIC Explanation: 
# MAGIC Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
# MAGIC Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33
# MAGIC
# MAGIC Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
# MAGIC Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 1719 ms
# MAGIC <h3> Beats: </h3> 41.86%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Write your T-SQL query statement below */
# MAGIC
# MAGIC WITH temp as ( 
# MAGIC   /* Select query_name, calculate average quality, count poor ratings, and total count */
# MAGIC   SELECT 
# MAGIC     query_name, 
# MAGIC     round(avg(rating * 1.00/position),2) as quality, /* Calculate average quality */
# MAGIC     sum(case when rating <3 then 1 else 0 end ) as poor_count, /* Count poor ratings */
# MAGIC     sum(1) as total_count /* Count total queries */
# MAGIC   from Queries
# MAGIC   GROUP BY query_name /* Group by query_name */
# MAGIC ) 
# MAGIC /* Select query_name, quality, and percentage of poor queries */
# MAGIC select query_name, 
# MAGIC   quality, 
# MAGIC   round ((poor_count * 100.00 / total_count),2) as poor_query_percentage /* Calculate poor query percentage */
# MAGIC from temp
