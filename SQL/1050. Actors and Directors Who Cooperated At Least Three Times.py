# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC ActorDirector
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | actor_id    | int     |
# MAGIC | director_id | int     |
# MAGIC | timestamp   | int     |
# MAGIC +-------------+---------+
# MAGIC timestamp is the primary key (column with unique values) for this table.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
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
# MAGIC ActorDirector table:
# MAGIC +-------------+-------------+-------------+
# MAGIC | actor_id    | director_id | timestamp   |
# MAGIC +-------------+-------------+-------------+
# MAGIC | 1           | 1           | 0           |
# MAGIC | 1           | 1           | 1           |
# MAGIC | 1           | 1           | 2           |
# MAGIC | 1           | 2           | 3           |
# MAGIC | 1           | 2           | 4           |
# MAGIC | 2           | 1           | 5           |
# MAGIC | 2           | 1           | 6           |
# MAGIC +-------------+-------------+-------------+
# MAGIC Output: 
# MAGIC +-------------+-------------+
# MAGIC | actor_id    | director_id |
# MAGIC +-------------+-------------+
# MAGIC | 1           | 1           |
# MAGIC +-------------+-------------+
# MAGIC Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 1568 ms
# MAGIC <h3> Beats: </h3> 66.77%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Write your T-SQL query statement below */
# MAGIC with cte as
# MAGIC (
# MAGIC select actor_id,director_id,max(rnk) as rnk
# MAGIC from
# MAGIC (
# MAGIC select actor_id,director_id, dense_rank() over (partition by actor_id,director_id order by timestamp) as rnk
# MAGIC from ActorDirector
# MAGIC ) a
# MAGIC group by actor_id,director_id
# MAGIC )select actor_id,director_id from cte
# MAGIC where rnk >=3
# MAGIC
# MAGIC
# MAGIC
