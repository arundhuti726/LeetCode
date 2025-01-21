# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Signups
# MAGIC
# MAGIC +----------------+----------+
# MAGIC | Column Name    | Type     |
# MAGIC +----------------+----------+
# MAGIC | user_id        | int      |
# MAGIC | time_stamp     | datetime |
# MAGIC +----------------+----------+
# MAGIC user_id is the column of unique values for this table.
# MAGIC Each row contains information about the signup time for the user with ID user_id.
# MAGIC  
# MAGIC
# MAGIC Table: Confirmations
# MAGIC
# MAGIC +----------------+----------+
# MAGIC | Column Name    | Type     |
# MAGIC +----------------+----------+
# MAGIC | user_id        | int      |
# MAGIC | time_stamp     | datetime |
# MAGIC | action         | ENUM     |
# MAGIC +----------------+----------+
# MAGIC (user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
# MAGIC user_id is a foreign key (reference column) to the Signups table.
# MAGIC action is an ENUM (category) of the type ('confirmed', 'timeout')
# MAGIC Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').
# MAGIC  
# MAGIC
# MAGIC The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.
# MAGIC
# MAGIC Write a solution to find the confirmation rate of each user.
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
# MAGIC Signups table:
# MAGIC +---------+---------------------+
# MAGIC | user_id | time_stamp          |
# MAGIC +---------+---------------------+
# MAGIC | 3       | 2020-03-21 10:16:13 |
# MAGIC | 7       | 2020-01-04 13:57:59 |
# MAGIC | 2       | 2020-07-29 23:09:44 |
# MAGIC | 6       | 2020-12-09 10:39:37 |
# MAGIC +---------+---------------------+
# MAGIC Confirmations table:
# MAGIC +---------+---------------------+-----------+
# MAGIC | user_id | time_stamp          | action    |
# MAGIC +---------+---------------------+-----------+
# MAGIC | 3       | 2021-01-06 03:30:46 | timeout   |
# MAGIC | 3       | 2021-07-14 14:00:00 | timeout   |
# MAGIC | 7       | 2021-06-12 11:57:29 | confirmed |
# MAGIC | 7       | 2021-06-13 12:58:28 | confirmed |
# MAGIC | 7       | 2021-06-14 13:59:27 | confirmed |
# MAGIC | 2       | 2021-01-22 00:00:00 | confirmed |
# MAGIC | 2       | 2021-02-28 23:59:59 | timeout   |
# MAGIC +---------+---------------------+-----------+
# MAGIC Output: 
# MAGIC +---------+-------------------+
# MAGIC | user_id | confirmation_rate |
# MAGIC +---------+-------------------+
# MAGIC | 6       | 0.00              |
# MAGIC | 3       | 0.00              |
# MAGIC | 7       | 1.00              |
# MAGIC | 2       | 0.50              |
# MAGIC +---------+-------------------+
# MAGIC Explanation: 
# MAGIC User 6 did not request any confirmation messages. The confirmation rate is 0.
# MAGIC User 3 made 2 requests and both timed out. The confirmation rate is 0.
# MAGIC User 7 made 3 requests and all were confirmed. The confirmation rate is 1.
# MAGIC User 2 made 2 requests where one was confirmed and the other timed out. The confirmation rate is 1 / 2 = 0.5.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 1362 ms
# MAGIC <h3> Beats: </h3> 13.40%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Write your T-SQL query statement below */
# MAGIC WITH temp as ( 
# MAGIC   /* Select user_id from Signups and action from Confirmations */
# MAGIC   SELECT 
# MAGIC     s.user_id,
# MAGIC     c.action
# MAGIC   /* Perform a LEFT JOIN on Signups and Confirmations tables using user_id */
# MAGIC   FROM Signups as s 
# MAGIC   LEFT JOIN Confirmations as c 
# MAGIC   on s.user_id = c.user_id
# MAGIC ) 
# MAGIC /* Calculate the confirmation rate for each user_id */
# MAGIC SELECT 
# MAGIC   user_id, 
# MAGIC   /* Calculate the confirmation rate as the ratio of confirmed actions to total actions */
# MAGIC   ROUND( 
# MAGIC     CAST(sum(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS DECIMAL(5,2) ) / count(*), 
# MAGIC     2 
# MAGIC   ) as confirmation_rate
# MAGIC from temp
# MAGIC /* Group the results by user_id */
# MAGIC GROUP BY user_id
