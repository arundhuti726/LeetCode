# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Followers
# MAGIC
# MAGIC +-------------+------+
# MAGIC | Column Name | Type |
# MAGIC +-------------+------+
# MAGIC | user_id     | int  |
# MAGIC | follower_id | int  |
# MAGIC +-------------+------+
# MAGIC (user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
# MAGIC This table contains the IDs of a user and a follower in a social media app where the follower follows the user.
# MAGIC  
# MAGIC
# MAGIC Write a solution that will, for each user, return the number of followers.
# MAGIC
# MAGIC Return the result table ordered by user_id in ascending order.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Followers table:
# MAGIC +---------+-------------+
# MAGIC | user_id | follower_id |
# MAGIC +---------+-------------+
# MAGIC | 0       | 1           |
# MAGIC | 1       | 0           |
# MAGIC | 2       | 0           |
# MAGIC | 2       | 1           |
# MAGIC +---------+-------------+
# MAGIC Output: 
# MAGIC +---------+----------------+
# MAGIC | user_id | followers_count|
# MAGIC +---------+----------------+
# MAGIC | 0       | 1              |
# MAGIC | 1       | 1              |
# MAGIC | 2       | 2              |
# MAGIC +---------+----------------+
# MAGIC Explanation: 
# MAGIC The followers of 0 are {1}
# MAGIC The followers of 1 are {0}
# MAGIC The followers of 2 are {0,1}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 1702 ms
# MAGIC <h3> Beats: </h3> 27.42%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

/* Write your T-SQL query statement below */
select user_id, count(user_id) as followers_count
from Followers
group by user_id
order by user_id
