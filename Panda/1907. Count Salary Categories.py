# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Accounts
# MAGIC
# MAGIC +-------------+------+
# MAGIC | Column Name | Type |
# MAGIC +-------------+------+
# MAGIC | account_id  | int  |
# MAGIC | income      | int  |
# MAGIC +-------------+------+
# MAGIC account_id is the primary key (column with unique values) for this table.
# MAGIC Each row contains information about the monthly income for one bank account.
# MAGIC  
# MAGIC
# MAGIC Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
# MAGIC
# MAGIC "Low Salary": All the salaries strictly less than $20000.
# MAGIC "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# MAGIC "High Salary": All the salaries strictly greater than $50000.
# MAGIC The result table must contain all three categories. If there are no accounts in a category, return 0.
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
# MAGIC Accounts table:
# MAGIC +------------+--------+
# MAGIC | account_id | income |
# MAGIC +------------+--------+
# MAGIC | 3          | 108939 |
# MAGIC | 2          | 12747  |
# MAGIC | 8          | 87709  |
# MAGIC | 6          | 91796  |
# MAGIC +------------+--------+
# MAGIC Output: 
# MAGIC +----------------+----------------+
# MAGIC | category       | accounts_count |
# MAGIC +----------------+----------------+
# MAGIC | Low Salary     | 1              |
# MAGIC | Average Salary | 0              |
# MAGIC | High Salary    | 3              |
# MAGIC +----------------+----------------+
# MAGIC Explanation: 
# MAGIC Low Salary: Account 2.
# MAGIC Average Salary: No accounts.
# MAGIC High Salary: Accounts 3, 6, and 8.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 487 ms
# MAGIC <h3> Beats: </h3> 75.75%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    
    High = (accounts['income'] > 50000).sum()
    Low =  (accounts['income'] < 20000).sum()
    Avg =  ((accounts['income'] <=50000) & (accounts['income'] >=20000)).sum()
    
    results = pd.DataFrame({'category':['Low Salary','Average Salary','High Salary'],'accounts_count':[Low,Avg,High]})
    return results
    
    # In a Pandas DataFrame, when a column returns an empty result, "count()" returns "None" (or null) because it is specifically designed to count non-null values, while "sum()" returns 0 because it treats empty or null values as zero when calculating the sum; essentially, "count" is counting the number of non-null values, so if there are no non-null values, it has nothing to count, resulting in "None", whereas "sum" will just add up "0" for each missing value, leading to a final sum of 0. 
    
