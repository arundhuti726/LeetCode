# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Activity
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | user_id       | int     |
# MAGIC | session_id    | int     |
# MAGIC | activity_date | date    |
# MAGIC | activity_type | enum    |
# MAGIC +---------------+---------+
# MAGIC This table may have duplicate rows.
# MAGIC The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
# MAGIC The table shows the user activities for a social media website. 
# MAGIC Note that each session belongs to exactly one user.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.
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
# MAGIC Activity table:
# MAGIC +---------+------------+---------------+---------------+
# MAGIC | user_id | session_id | activity_date | activity_type |
# MAGIC +---------+------------+---------------+---------------+
# MAGIC | 1       | 1          | 2019-07-20    | open_session  |
# MAGIC | 1       | 1          | 2019-07-20    | scroll_down   |
# MAGIC | 1       | 1          | 2019-07-20    | end_session   |
# MAGIC | 2       | 4          | 2019-07-20    | open_session  |
# MAGIC | 2       | 4          | 2019-07-21    | send_message  |
# MAGIC | 2       | 4          | 2019-07-21    | end_session   |
# MAGIC | 3       | 2          | 2019-07-21    | open_session  |
# MAGIC | 3       | 2          | 2019-07-21    | send_message  |
# MAGIC | 3       | 2          | 2019-07-21    | end_session   |
# MAGIC | 4       | 3          | 2019-06-25    | open_session  |
# MAGIC | 4       | 3          | 2019-06-25    | end_session   |
# MAGIC +---------+------------+---------------+---------------+
# MAGIC Output: 
# MAGIC +------------+--------------+ 
# MAGIC | day        | active_users |
# MAGIC +------------+--------------+ 
# MAGIC | 2019-07-20 | 2            |
# MAGIC | 2019-07-21 | 2            |
# MAGIC +------------+--------------+ 
# MAGIC Explanation: Note that we do not care about days with zero active users.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 2468 ms
# MAGIC <h3> Beats: </h3> 36.37%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC /* Write your T-SQL query statement below */
# MAGIC
# MAGIC SELECT activity_date as day, count(distinct user_id) as active_users
# MAGIC FROM Activity
# MAGIC WHERE activity_date between '2019-06-28' and '2019-07-27'
# MAGIC GROUP BY activity_date
