# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Users
# MAGIC
# MAGIC +----------------+---------+
# MAGIC | Column Name    | Type    |
# MAGIC +----------------+---------+
# MAGIC | user_id        | int     |
# MAGIC | name           | varchar |
# MAGIC +----------------+---------+
# MAGIC user_id is the primary key (column with unique values) for this table.
# MAGIC This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
# MAGIC  
# MAGIC
# MAGIC Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
# MAGIC
# MAGIC Return the result table ordered by user_id.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Users table:
# MAGIC +---------+-------+
# MAGIC | user_id | name  |
# MAGIC +---------+-------+
# MAGIC | 1       | aLice |
# MAGIC | 2       | bOB   |
# MAGIC +---------+-------+
# MAGIC Output: 
# MAGIC +---------+-------+
# MAGIC | user_id | name  |
# MAGIC +---------+-------+
# MAGIC | 1       | Alice |
# MAGIC | 2       | Bob   |
# MAGIC +---------+-------+

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 1055 ms
# MAGIC <h3> Beats: </h3> 87.03%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC select user_id, 
# MAGIC -- Concatenate the uppercase first letter with the lowercase rest of the name
# MAGIC concat(upper(left(name,1)),lower(right(name,len(name)-1))) as name
# MAGIC -- From the Users table
# MAGIC from Users
# MAGIC -- Order the results by user_id in ascending order
# MAGIC order by user_id
