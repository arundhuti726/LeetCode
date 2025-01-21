# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Views
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | article_id    | int     |
# MAGIC | author_id     | int     |
# MAGIC | viewer_id     | int     |
# MAGIC | view_date     | date    |
# MAGIC +---------------+---------+
# MAGIC There is no primary key (column with unique values) for this table, the table may have duplicate rows.
# MAGIC Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
# MAGIC Note that equal author_id and viewer_id indicate the same person.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find all the authors that viewed at least one of their own articles.
# MAGIC
# MAGIC Return the result table sorted by id in ascending order.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Views table:
# MAGIC +------------+-----------+-----------+------------+
# MAGIC | article_id | author_id | viewer_id | view_date  |
# MAGIC +------------+-----------+-----------+------------+
# MAGIC | 1          | 3         | 5         | 2019-08-01 |
# MAGIC | 1          | 3         | 6         | 2019-08-02 |
# MAGIC | 2          | 7         | 7         | 2019-08-01 |
# MAGIC | 2          | 7         | 6         | 2019-08-02 |
# MAGIC | 4          | 7         | 1         | 2019-07-22 |
# MAGIC | 3          | 4         | 4         | 2019-07-21 |
# MAGIC | 3          | 4         | 4         | 2019-07-21 |
# MAGIC +------------+-----------+-----------+------------+
# MAGIC Output: 
# MAGIC +------+
# MAGIC | id   |
# MAGIC +------+
# MAGIC | 4    |
# MAGIC | 7    |
# MAGIC +------+
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 565 ms
# MAGIC <h3> Beats: </h3> 24.02%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    #PROCESS 1
    
    # df = pd.DataFrame(views)
    # # Filter rows where author_id is equal to viewer_id
    # df_filtered = df[df['author_id'] == df['viewer_id']]

    # # Group by article_id and author_id, and count the occurrences
    # df_grouped = df_filtered.groupby(['article_id', 'author_id']).size().reset_index(name='counts')

    # # Sort the grouped DataFrame by author_id
    # #df_sorted = df_grouped.sort_values(by='author_id')

    # # Select the author_id column, rename it to 'id', and display the result
    # df_result = df_grouped[['author_id']].rename(columns={'author_id': 'id'}).sort_values(by='id').drop_duplicates()
    # return df_result

#     """" The .size().reset_index(name='counts') is used to count the number of occurrences for each group
#  and to convert the resulting Series into a DataFrame with a column named 'counts'.
# This is necessary because the groupby operation returns a Series, and we need a DataFrame for further processing.

# Example without .size().reset_index(name='counts')
# df_grouped_example = df_filtered.groupby(['article_id', 'author_id']).size()
# display(df_grouped_example)

# Example with .size().reset_index(name='counts')
# df_grouped = df_filtered.groupby(['article_id', 'author_id']).size().reset_index(name='counts')
# display(df_grouped) """

    # process 2 ms 407
     # return views.loc[views['author_id']==views['viewer_id'],['author_id']].sort_values('author_id').rename(columns={'author_id':'id'}).drop_duplicates('id')


    #Process 3 ms 330
     d = views[views.author_id == views.viewer_id][['author_id']].rename(columns={'author_id': 'id'}).drop_duplicates('id').sort_values('id')
     return d
