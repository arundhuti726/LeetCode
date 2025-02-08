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
# MAGIC ### Run Time: </h3> 24140 ms
# MAGIC <h3> Beats: </h3> 43.04%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

/* Write your T-SQL query statement below */
with Low as
(
    select account_id,
    case when income < 20000 then 'Low Salary' end as category       
    from Accounts
    where income < 20000
),
High as
(
    select account_id,
    case when income > 50000 then 'High Salary' end as category       
    from Accounts
    where income > 50000
),
Avg as
(
    select account_id,
    case when income >= 20000 and income <= 50000 then 'Average Salary' end as category       
    from Accounts
    where income >= 20000 and income <= 50000
),
UN as
(
    select category, count(account_id) as accounts_count from Low group by category
    union 
    select category, count(account_id) as accounts_count from High group by category
    union 
    select category, count(account_id) as accounts_count from Avg group by category
    union
    select 'Low Salary' as category, 0 as accounts_count
    union
    select 'High Salary' as category, 0 as accounts_count
    union
    select 'Average Salary' as category, 0 as accounts_count
)
select category, max(accounts_count) as accounts_count from UN
group by category
