# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Tweets
# MAGIC
# MAGIC +----------------+---------+
# MAGIC | Column Name    | Type    |
# MAGIC +----------------+---------+
# MAGIC | tweet_id       | int     |
# MAGIC | content        | varchar |
# MAGIC +----------------+---------+
# MAGIC tweet_id is the primary key (column with unique values) for this table.
# MAGIC content consists of characters on an American Keyboard, and no other special characters.
# MAGIC This table contains all the tweets in a social media app.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
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
# MAGIC Tweets table:
# MAGIC +----------+-----------------------------------+
# MAGIC | tweet_id | content                           |
# MAGIC +----------+-----------------------------------+
# MAGIC | 1        | Let us Code                       |
# MAGIC | 2        | More than fifteen chars are here! |
# MAGIC +----------+-----------------------------------+
# MAGIC Output: 
# MAGIC +----------+
# MAGIC | tweet_id |
# MAGIC +----------+
# MAGIC | 2        |
# MAGIC +----------+
# MAGIC Explanation: 
# MAGIC Tweet 1 has length = 11. It is a valid tweet.
# MAGIC Tweet 2 has length = 33. It is an invalid tweet.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 320 ms
# MAGIC <h3> Beats: </h3> 80.68%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    #PROCESS 1 ms 367
    # filtered_tweets = tweets[tweets['content'].str.len() > 15]
    # return filtered_tweets[['tweet_id']]

    #PROCESS 2 (one liner of Process 1) # ms 327, beats 81.54
    return tweets[tweets['content'].str.len() > 15][['tweet_id']] 
    
    
