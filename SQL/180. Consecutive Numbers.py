# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Logs
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | id          | int     |
# MAGIC | num         | varchar |
# MAGIC +-------------+---------+
# MAGIC In SQL, id is the primary key for this table.
# MAGIC id is an autoincrement column starting from 1.
# MAGIC  
# MAGIC
# MAGIC Find all numbers that appear at least three times consecutively.
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
# MAGIC Logs table:
# MAGIC +----+-----+
# MAGIC | id | num |
# MAGIC +----+-----+
# MAGIC | 1  | 1   |
# MAGIC | 2  | 1   |
# MAGIC | 3  | 1   |
# MAGIC | 4  | 2   |
# MAGIC | 5  | 1   |
# MAGIC | 6  | 2   |
# MAGIC | 7  | 2   |
# MAGIC +----+-----+
# MAGIC Output: 
# MAGIC +-----------------+
# MAGIC | ConsecutiveNums |
# MAGIC +-----------------+
# MAGIC | 1               |
# MAGIC +-----------------+
# MAGIC Explanation: 1 is the only number that appears consecutively for at least three times.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 949 ms
# MAGIC <h3> Beats: </h3> 80.43%
# MAGIC <h3> Complexity: </h3>

# COMMAND ----------

# MAGIC %sql
# MAGIC with cte as
# MAGIC (
# MAGIC   -- Select id and num columns and calculate the previous and next values of num using window functions
# MAGIC   select id, num,
# MAGIC     lead(num) over (order by id) as next,
# MAGIC     lag(num) over (order by id) as prev
# MAGIC   from Logs
# MAGIC )
# MAGIC -- Select num where the current value matches both the previous and next values, and group by num
# MAGIC select num as ConsecutiveNums 
# MAGIC from cte
# MAGIC where num = prev and num = next
# MAGIC group by num
