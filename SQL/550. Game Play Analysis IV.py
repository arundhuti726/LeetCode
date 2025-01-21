# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC
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
# MAGIC Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.
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
# MAGIC | 1         | 2         | 2016-03-02 | 6            |
# MAGIC | 2         | 3         | 2017-06-25 | 1            |
# MAGIC | 3         | 1         | 2016-03-02 | 0            |
# MAGIC | 3         | 4         | 2018-07-03 | 5            |
# MAGIC +-----------+-----------+------------+--------------+
# MAGIC Output: 
# MAGIC +-----------+
# MAGIC | fraction  |
# MAGIC +-----------+
# MAGIC | 0.33      |
# MAGIC +-----------+
# MAGIC Explanation: 
# MAGIC Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 2974 ms
# MAGIC <h3> Beats: </h3> 54.68%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC -- /* Write your T-SQL query statement below */
# MAGIC --  --Process 1: time limit exceed  
# MAGIC -- -- CTE to find the first login date for each player
# MAGIC --   WITH first_loging AS (
# MAGIC --   SELECT
# MAGIC --     t1.player_id,
# MAGIC --     MIN(t1.event_date) AS first_login
# MAGIC --   FROM
# MAGIC --     Activity t1
# MAGIC --   GROUP BY
# MAGIC --     t1.player_id
# MAGIC -- ), 
# MAGIC -- -- CTE to count the total logins that occur the day after the first login
# MAGIC -- next_loging AS (
# MAGIC --   SELECT
# MAGIC --     COUNT(t1.player_id)*1.0 AS total_logins
# MAGIC --   FROM
# MAGIC --     first_loging t2
# MAGIC --     INNER JOIN Activity t1 ON t2.player_id = t1.player_id
# MAGIC --     AND t2.first_login = DATEADD(day,-1,t1.event_date)
# MAGIC -- )
# MAGIC -- -- Calculate the fraction of players who logged in the day after their first login
# MAGIC -- SELECT
# MAGIC --   ROUND(
# MAGIC --     (SELECT C.total_logins FROM next_loging C)
# MAGIC --     / (SELECT COUNT(F.player_id) FROM first_loging F)
# MAGIC --   , 2) AS fraction;
# MAGIC
# MAGIC
# MAGIC  --Process 2: 3014 ms
# MAGIC
# MAGIC --  -- CTE to find the first login date for each player
# MAGIC --   WITH first_loging AS (
# MAGIC --   SELECT
# MAGIC --     t1.player_id,
# MAGIC --     MIN(t1.event_date) AS first_login
# MAGIC --   FROM
# MAGIC --     Activity t1
# MAGIC --   GROUP BY
# MAGIC --     t1.player_id
# MAGIC -- ), 
# MAGIC -- -- CTE to count the total logins that occur the day after the first login
# MAGIC -- next_loging AS (
# MAGIC --   SELECT
# MAGIC --     COUNT(t1.player_id)*1.0 AS total_logins
# MAGIC --   FROM
# MAGIC --     first_loging t2
# MAGIC --     INNER JOIN Activity t1 ON t2.player_id = t1.player_id
# MAGIC --     AND t2.first_login = DATEADD(day,-1,t1.event_date)
# MAGIC -- ),
# MAGIC -- total_players AS(
# MAGIC --  SELECT COUNT(t.player_id) as total_player FROM first_loging t
# MAGIC -- )
# MAGIC -- -- Calculate the fraction of players who logged in the day after their first login
# MAGIC -- SELECT
# MAGIC --   ROUND(
# MAGIC --     (SELECT N.total_logins FROM next_loging N)
# MAGIC --     /(select T.total_player from total_players T)
# MAGIC --   , 2) AS fraction;
# MAGIC
# MAGIC --Process 3: 2975 ms
# MAGIC  
# MAGIC  -- CTE to find the first login date for each player
# MAGIC   WITH first_loging AS (
# MAGIC   SELECT
# MAGIC     t1.player_id,
# MAGIC     MIN(t1.event_date) AS first_login
# MAGIC   FROM
# MAGIC     Activity t1
# MAGIC   GROUP BY
# MAGIC     t1.player_id
# MAGIC ), 
# MAGIC -- CTE to count the total logins that occur the day after the first login
# MAGIC next_loging AS (
# MAGIC   SELECT
# MAGIC     COUNT(t1.player_id) AS total_logins
# MAGIC   FROM
# MAGIC     first_loging t2
# MAGIC     INNER JOIN Activity t1 ON t2.player_id = t1.player_id
# MAGIC     AND t2.first_login = DATEADD(day,-1,t1.event_date)
# MAGIC ),
# MAGIC total_players AS(
# MAGIC  SELECT COUNT(t.player_id) as total_player FROM first_loging t
# MAGIC )
# MAGIC -- Calculate the fraction of players who logged in the day after their first login
# MAGIC SELECT
# MAGIC   ROUND(
# MAGIC     (SELECT (total_logins*1.0) FROM next_loging N)
# MAGIC     /(select T.total_player from total_players T)
# MAGIC   , 2) AS fraction;
# MAGIC
# MAGIC
