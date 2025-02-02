# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Scores
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | id          | int     |
# MAGIC | score       | decimal |
# MAGIC +-------------+---------+
# MAGIC id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:
# MAGIC
# MAGIC The scores should be ranked from the highest to the lowest.
# MAGIC If there is a tie between two scores, both should have the same ranking.
# MAGIC After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# MAGIC Return the result table ordered by score in descending order.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Scores table:
# MAGIC +----+-------+
# MAGIC | id | score |
# MAGIC +----+-------+
# MAGIC | 1  | 3.50  |
# MAGIC | 2  | 3.65  |
# MAGIC | 3  | 4.00  |
# MAGIC | 4  | 3.85  |
# MAGIC | 5  | 4.00  |
# MAGIC | 6  | 3.65  |
# MAGIC +----+-------+
# MAGIC Output: 
# MAGIC +-------+------+
# MAGIC | score | rank |
# MAGIC +-------+------+
# MAGIC | 4.00  | 1    |
# MAGIC | 4.00  | 1    |
# MAGIC | 3.85  | 2    |
# MAGIC | 3.65  | 3    |
# MAGIC | 3.65  | 3    |
# MAGIC | 3.50  | 4    |
# MAGIC +-------+------+

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 408 ms
# MAGIC <h3> Beats: </h3> 63.58%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending = False)
    return scores[['score', 'rank']].sort_values(by='rank')
