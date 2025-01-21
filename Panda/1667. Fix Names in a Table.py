# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC
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
# MAGIC ### Run Time: </h3> 299 ms
# MAGIC <h3> Beats: </h3> 89.09%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(users)

    #PROCESS 1 299 ms, beats 89.41%
    
    #Convert the 'name' field to lower case and by using  capitalize(), convert the first letter into uppercase
    df['name'] = df['name'].str.lower().str.capitalize()
    #sort by userId
    return df.sort_values(['user_id'])
    
