# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC MyNumbers
# MAGIC
# MAGIC +-------------+------+
# MAGIC | Column Name | Type |
# MAGIC +-------------+------+
# MAGIC | num         | int  |
# MAGIC +-------------+------+
# MAGIC This table may contain duplicates (In other words, there is no primary key for this table in SQL).
# MAGIC Each row of this table contains an integer.
# MAGIC  
# MAGIC
# MAGIC A single number is a number that appeared only once in the MyNumbers table.
# MAGIC
# MAGIC Find the largest single number. If there is no single number, report null.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC MyNumbers table:
# MAGIC +-----+
# MAGIC | num |
# MAGIC +-----+
# MAGIC | 8   |
# MAGIC | 8   |
# MAGIC | 3   |
# MAGIC | 3   |
# MAGIC | 1   |
# MAGIC | 4   |
# MAGIC | 5   |
# MAGIC | 6   |
# MAGIC +-----+
# MAGIC Output: 
# MAGIC +-----+
# MAGIC | num |
# MAGIC +-----+
# MAGIC | 6   |
# MAGIC +-----+
# MAGIC Explanation: The single numbers are 1, 4, 5, and 6.
# MAGIC Since 6 is the largest single number, we return it.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: 
# MAGIC MyNumbers table:
# MAGIC +-----+
# MAGIC | num |
# MAGIC +-----+
# MAGIC | 8   |
# MAGIC | 8   |
# MAGIC | 7   |
# MAGIC | 7   |
# MAGIC | 3   |
# MAGIC | 3   |
# MAGIC | 3   |
# MAGIC +-----+
# MAGIC Output: 
# MAGIC +------+
# MAGIC | num  |
# MAGIC +------+
# MAGIC | null |
# MAGIC +------+
# MAGIC Explanation: There are no single numbers in the input table so we return null.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 624 ms
# MAGIC <h3> Beats: </h3> 51.13%
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

/* Write your T-SQL query statement below */
select 
    coalesce(max(num),NULL)  as num
from(
select num, count(num) as cnt
from MyNumbers
group by num
) a
where cnt = 1


