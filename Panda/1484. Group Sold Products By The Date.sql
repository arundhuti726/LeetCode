-- Databricks notebook source
-- MAGIC %md
-- MAGIC <h5> ROBLEM DESCRIPTION </h5>
-- MAGIC Activities:
-- MAGIC
-- MAGIC +-------------+---------+
-- MAGIC | Column Name | Type    |
-- MAGIC +-------------+---------+
-- MAGIC | sell_date   | date    |
-- MAGIC | product     | varchar |
-- MAGIC +-------------+---------+
-- MAGIC There is no primary key (column with unique values) for this table. It may contain duplicates.
-- MAGIC Each row of this table contains the product name and the date it was sold in a market.
-- MAGIC  
-- MAGIC
-- MAGIC Write a solution to find for each date the number of different products sold and their names.
-- MAGIC
-- MAGIC The sold products names for each date should be sorted lexicographically.
-- MAGIC
-- MAGIC Return the result table ordered by sell_date.
-- MAGIC
-- MAGIC The result format is in the following example.
-- MAGIC
-- MAGIC  
-- MAGIC
-- MAGIC Example 1:
-- MAGIC
-- MAGIC Input: 
-- MAGIC Activities table:
-- MAGIC +------------+------------+
-- MAGIC | sell_date  | product     |
-- MAGIC +------------+------------+
-- MAGIC | 2020-05-30 | Headphone  |
-- MAGIC | 2020-06-01 | Pencil     |
-- MAGIC | 2020-06-02 | Mask       |
-- MAGIC | 2020-05-30 | Basketball |
-- MAGIC | 2020-06-01 | Bible      |
-- MAGIC | 2020-06-02 | Mask       |
-- MAGIC | 2020-05-30 | T-Shirt    |
-- MAGIC +------------+------------+
-- MAGIC Output: 
-- MAGIC +------------+----------+------------------------------+
-- MAGIC | sell_date  | num_sold | products                     |
-- MAGIC +------------+----------+------------------------------+
-- MAGIC | 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
-- MAGIC | 2020-06-01 | 2        | Bible,Pencil                 |
-- MAGIC | 2020-06-02 | 1        | Mask                         |
-- MAGIC +------------+----------+------------------------------+
-- MAGIC Explanation: 
-- MAGIC For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
-- MAGIC For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
-- MAGIC For 2020-06-02, the Sold item is (Mask), we just return it.
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Run Time: </h3> 543 ms
-- MAGIC <h3> Beats: </h3> 63.46%
-- MAGIC <h3> Complexity: </h3>

-- COMMAND ----------

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    # Drop duplicate rows based on 'sell_date' and 'product', then sort by 'sell_date' and 'product'
    activities = activities.drop_duplicates(subset=['sell_date', 'product']).sort_values(['sell_date', 'product'])

    # Add a column 'num_sold' with the count of products sold per 'sell_date'
    activities['num_sold'] = activities.groupby(['sell_date'])['sell_date'].transform('size')
    
    # Group by 'sell_date' and aggregate the products into a comma-separated string and get the first 'num_sold' value
    activities = activities.groupby(['sell_date']).agg(
    products=('product', lambda x: ','.join(x)),
    num_sold=('num_sold', 'first')
    ).reset_index()

    return activities[['sell_date', 'num_sold', 'products']]
