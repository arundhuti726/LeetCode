# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Employees
# MAGIC
# MAGIC +-------------+----------+
# MAGIC | Column Name | Type     |
# MAGIC +-------------+----------+
# MAGIC | employee_id | int      |
# MAGIC | name        | varchar  |
# MAGIC | manager_id  | int      |
# MAGIC | salary      | int      |
# MAGIC +-------------+----------+
# MAGIC In SQL, employee_id is the primary key for this table.
# MAGIC This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null). 
# MAGIC  
# MAGIC
# MAGIC Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.
# MAGIC
# MAGIC Return the result table ordered by employee_id.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input:  
# MAGIC Employees table:
# MAGIC +-------------+-----------+------------+--------+
# MAGIC | employee_id | name      | manager_id | salary |
# MAGIC +-------------+-----------+------------+--------+
# MAGIC | 3           | Mila      | 9          | 60301  |
# MAGIC | 12          | Antonella | null       | 31000  |
# MAGIC | 13          | Emery     | null       | 67084  |
# MAGIC | 1           | Kalel     | 11         | 21241  |
# MAGIC | 9           | Mikaela   | null       | 50937  |
# MAGIC | 11          | Joziah    | 6          | 28485  |
# MAGIC +-------------+-----------+------------+--------+
# MAGIC Output: 
# MAGIC +-------------+
# MAGIC | employee_id |
# MAGIC +-------------+
# MAGIC | 11          |
# MAGIC +-------------+
# MAGIC
# MAGIC Explanation: 
# MAGIC The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
# MAGIC Kalel's manager is employee 11, who is still in the company (Joziah).
# MAGIC Joziah's manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 742 ms
# MAGIC <h3> Beats: </h3> 50.35%
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

/* Write your T-SQL query statement below */
select employee_id
from Employees
where manager_id is not null 
and salary < 30000
and manager_id not in (select employee_id from Employees )
order by employee_id
