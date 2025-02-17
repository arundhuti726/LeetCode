# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Employees
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | id            | int     |
# MAGIC | name          | varchar |
# MAGIC +---------------+---------+
# MAGIC id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table contains the id and the name of an employee in a company.
# MAGIC  
# MAGIC
# MAGIC Table: EmployeeUNI
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | id            | int     |
# MAGIC | unique_id     | int     |
# MAGIC +---------------+---------+
# MAGIC (id, unique_id) is the primary key (combination of columns with unique values) for this table.
# MAGIC Each row of this table contains the id and the corresponding unique id of an employee in the company.
# MAGIC  
# MAGIC
# MAGIC Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.
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
# MAGIC Employees table:
# MAGIC +----+----------+
# MAGIC | id | name     |
# MAGIC +----+----------+
# MAGIC | 1  | Alice    |
# MAGIC | 7  | Bob      |
# MAGIC | 11 | Meir     |
# MAGIC | 90 | Winston  |
# MAGIC | 3  | Jonathan |
# MAGIC +----+----------+
# MAGIC EmployeeUNI table:
# MAGIC +----+-----------+
# MAGIC | id | unique_id |
# MAGIC +----+-----------+
# MAGIC | 3  | 1         |
# MAGIC | 11 | 2         |
# MAGIC | 90 | 3         |
# MAGIC +----+-----------+
# MAGIC Output: 
# MAGIC +-----------+----------+
# MAGIC | unique_id | name     |
# MAGIC +-----------+----------+
# MAGIC | null      | Alice    |
# MAGIC | null      | Bob      |
# MAGIC | 2         | Meir     |
# MAGIC | 3         | Winston  |
# MAGIC | 1         | Jonathan |
# MAGIC +-----------+----------+
# MAGIC Explanation: 
# MAGIC Alice and Bob do not have a unique ID, We will show null instead.
# MAGIC The unique ID of Meir is 2.
# MAGIC The unique ID of Winston is 3.
# MAGIC The unique ID of Jonathan is 1.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 2679 ms
# MAGIC <h3> Beats: </h3> 59.91%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

/* Write your T-SQL query statement below */
Select t2.unique_id,t1.name
from Employees t1
left join EmployeeUNI t2
on t1.id = t2.id
