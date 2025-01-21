# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Employee
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | id          | int     |
# MAGIC | name        | varchar |
# MAGIC | department  | varchar |
# MAGIC | managerId   | int     |
# MAGIC +-------------+---------+
# MAGIC id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table indicates the name of an employee, their department, and the id of their manager.
# MAGIC If managerId is null, then the employee does not have a manager.
# MAGIC No employee will be the manager of themself.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find managers with at least five direct reports.
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
# MAGIC Employee table:
# MAGIC +-----+-------+------------+-----------+
# MAGIC | id  | name  | department | managerId |
# MAGIC +-----+-------+------------+-----------+
# MAGIC | 101 | John  | A          | null      |
# MAGIC | 102 | Dan   | A          | 101       |
# MAGIC | 103 | James | A          | 101       |
# MAGIC | 104 | Amy   | A          | 101       |
# MAGIC | 105 | Anne  | A          | 101       |
# MAGIC | 106 | Ron   | B          | 101       |
# MAGIC +-----+-------+------------+-----------+
# MAGIC Output: 
# MAGIC +------+
# MAGIC | name |
# MAGIC +------+
# MAGIC | John |
# MAGIC +------+

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 610 ms
# MAGIC <h3> Beats: </h3> 36.91%
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC Select Name from Employee t1 -- Select the Name column from the Employee table aliased as t1
# MAGIC -- Perform an inner join with a subquery that selects managerId
# MAGIC inner join (select managerId from
# MAGIC ( -- Subquery that selects all columns and adds a dense_rank partitioned by managerId and ordered by id
# MAGIC select *, dense_rank() over (partition by managerId order by id) as DR from Employee)  a
# MAGIC -- Filter the results where the dense_rank is equal to 5
# MAGIC where DR=5)  t2 
# MAGIC -- Join condition on the id of t1 and managerId of t2
# MAGIC on t1.id=t2.managerId
