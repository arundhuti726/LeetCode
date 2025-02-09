# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Person
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | id          | int     |
# MAGIC | email       | varchar |
# MAGIC +-------------+---------+
# MAGIC id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table contains an email. The emails will not contain uppercase letters.
# MAGIC  
# MAGIC
# MAGIC Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
# MAGIC
# MAGIC For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
# MAGIC
# MAGIC For Pandas users, please note that you are supposed to modify Person in place.
# MAGIC
# MAGIC After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Person table:
# MAGIC +----+------------------+
# MAGIC | id | email            |
# MAGIC +----+------------------+
# MAGIC | 1  | john@example.com |
# MAGIC | 2  | bob@example.com  |
# MAGIC | 3  | john@example.com |
# MAGIC +----+------------------+
# MAGIC Output: 
# MAGIC +----+------------------+
# MAGIC | id | email            |
# MAGIC +----+------------------+
# MAGIC | 1  | john@example.com |
# MAGIC | 2  | bob@example.com  |
# MAGIC +----+------------------+
# MAGIC Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 528 ms
# MAGIC <h3> Beats: </h3> 87.80%
# MAGIC <h3> Complexity: </h3> O(n)

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Write your T-SQL query statement below */
# MAGIC delete from person where ID NOT IN (
# MAGIC     select min(ID) from person group by Email
# MAGIC )
