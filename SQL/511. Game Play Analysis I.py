# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Activity
# MAGIC
# MAGIC +--------------+---------+
# MAGIC | Column Name  | Type    |
# MAGIC +--------------+---------+
# MAGIC | player_id    | int     |
# MAGIC | device_id    | int     |
# MAGIC | event_date   | date    |
# MAGIC | games_played | int     |
# MAGIC +--------------+---------+
# MAGIC (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
# MAGIC This table shows the activity of players of some games.
# MAGIC Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the first login date for each player.
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
# MAGIC +-----------+-----------+------------+--------------+
# MAGIC | player_id | device_id | event_date | games_played |
# MAGIC +-----------+-----------+------------+--------------+
# MAGIC | 1         | 2         | 2016-03-01 | 5            |
# MAGIC | 1         | 2         | 2016-05-02 | 6            |
# MAGIC | 2         | 3         | 2017-06-25 | 1            |
# MAGIC | 3         | 1         | 2016-03-02 | 0            |
# MAGIC | 3         | 4         | 2018-07-03 | 5            |
# MAGIC +-----------+-----------+------------+--------------+
# MAGIC Output: 
# MAGIC +-----------+-------------+
# MAGIC | player_id | first_login |
# MAGIC +-----------+-------------+
# MAGIC | 1         | 2016-03-01  |
# MAGIC | 2         | 2017-06-25  |
# MAGIC | 3         | 2016-03-02  |
# MAGIC +-----------+-------------+

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 1235 ms
# MAGIC <h3> Beats: </h3> 97.19%
# MAGIC <h3> Complexity: </h3>  O(n)
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Select player_id and event_date as first_login */
# MAGIC select player_id, event_date as first_login 
# MAGIC from(
# MAGIC /* Select player_id, event_date and assign rank based on event_date for each player_id */
# MAGIC select player_id, event_date,
# MAGIC  dense_rank() over (partition by player_id order by event_date ) as rank_no
# MAGIC from Activity ) a
# MAGIC /* Filter to get the first login for each player_id */
# MAGIC where rank_no = 1
