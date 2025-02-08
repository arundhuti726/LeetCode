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
# MAGIC ### Run Time: </h3> 751 ms
# MAGIC <h3> Beats: </h3> 9.74%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['rank'] = activity.groupby(['player_id'])['event_date'].rank(method='dense')
    filter_data = activity[activity['rank']==1]
    

    result = filter_data.merge(activity, on=['player_id', 'event_date'], how='inner')[['player_id','event_date']].rename(columns={'event_date':'first_login'})
    
    return result
