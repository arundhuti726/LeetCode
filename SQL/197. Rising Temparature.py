# Databricks notebook source
# MAGIC %md
# MAGIC <h3>ROBLEM DESCRIPTION</h3>
# MAGIC Table: Weather
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | id            | int     |
# MAGIC | recordDate    | date    |
# MAGIC | temperature   | int     |
# MAGIC +---------------+---------+
# MAGIC id is the column with unique values for this table.
# MAGIC There are no different rows with the same recordDate.
# MAGIC This table contains information about the temperature on a certain day.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
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
# MAGIC Weather table:
# MAGIC +----+------------+-------------+
# MAGIC | id | recordDate | temperature |
# MAGIC +----+------------+-------------+
# MAGIC | 1  | 2015-01-01 | 10          |
# MAGIC | 2  | 2015-01-02 | 25          |
# MAGIC | 3  | 2015-01-03 | 20          |
# MAGIC | 4  | 2015-01-04 | 30          |
# MAGIC +----+------------+-------------+
# MAGIC Output: 
# MAGIC +----+
# MAGIC | id |
# MAGIC +----+
# MAGIC | 2  |
# MAGIC | 4  |
# MAGIC +----+
# MAGIC Explanation: 
# MAGIC In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
# MAGIC In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 793 ms
# MAGIC <h3> Beats: </h3> 51.95%
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Select the id from the subquery */
# MAGIC select id
# MAGIC from(
# MAGIC   /* Subquery to calculate temperature difference and previous date */
# MAGIC   select 
# MAGIC     id, 
# MAGIC     temperature, 
# MAGIC     recordDate, 
# MAGIC     lag(temperature) over (order by recordDate) as ld, 
# MAGIC     (temperature - lag(temperature) over (order by recordDate)) as diff, 
# MAGIC     lag(recordDate) over (order by recordDate) as prevDate
# MAGIC   from Weather
# MAGIC ) a
# MAGIC /* Filter where the temperature difference is positive and the previous date is exactly one day before the current date */
# MAGIC where diff is not null and diff > 0 and datediff(day, prevDate, recordDate) = 1
