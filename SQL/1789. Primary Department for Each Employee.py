# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Employee
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   |  Type   |
# MAGIC +---------------+---------+
# MAGIC | employee_id   | int     |
# MAGIC | department_id | int     |
# MAGIC | primary_flag  | varchar |
# MAGIC +---------------+---------+
# MAGIC (employee_id, department_id) is the primary key (combination of columns with unique values) for this table.
# MAGIC employee_id is the id of the employee.
# MAGIC department_id is the id of the department to which the employee belongs.
# MAGIC primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary.
# MAGIC  
# MAGIC
# MAGIC Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.
# MAGIC
# MAGIC Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.
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
# MAGIC +-------------+---------------+--------------+
# MAGIC | employee_id | department_id | primary_flag |
# MAGIC +-------------+---------------+--------------+
# MAGIC | 1           | 1             | N            |
# MAGIC | 2           | 1             | Y            |
# MAGIC | 2           | 2             | N            |
# MAGIC | 3           | 3             | N            |
# MAGIC | 4           | 2             | N            |
# MAGIC | 4           | 3             | Y            |
# MAGIC | 4           | 4             | N            |
# MAGIC +-------------+---------------+--------------+
# MAGIC Output: 
# MAGIC +-------------+---------------+
# MAGIC | employee_id | department_id |
# MAGIC +-------------+---------------+
# MAGIC | 1           | 1             |
# MAGIC | 2           | 1             |
# MAGIC | 3           | 3             |
# MAGIC | 4           | 3             |
# MAGIC +-------------+---------------+
# MAGIC Explanation: 
# MAGIC - The Primary department for employee 1 is 1.
# MAGIC - The Primary department for employee 2 is 1.
# MAGIC - The Primary department for employee 3 is 3.
# MAGIC - The Primary department for employee 4 is 3.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 815 ms
# MAGIC <h3> Beats: </h3> 75.04%
# MAGIC <h3> Complexity: </h3>

# COMMAND ----------

-- Create a common table expression (CTE) named CTE
WITH CTE AS
(
  -- Select employee_id and department_id based on conditions
  SELECT 
    employee_id,
    -- Assign department_id if primary_flag is 'Y' or if TOTAL_ENGAGEMENT equals 1
    CASE WHEN primary_flag='Y' THEN department_id 
         WHEN TOTAL_ENGAGEMENT = 1 THEN department_id
         END AS department_id
  FROM
  (       
    -- Select employee_id, department_id, primary_flag, and calculate TOTAL_ENGAGEMENT
    SELECT 
        employee_id, 
        department_id, 
        primary_flag,
        -- Count the number of engagements per employee
        COUNT(employee_id) OVER (PARTITION BY employee_id ORDER BY department_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING ) AS TOTAL_ENGAGEMENT
    FROM Employee 
  ) A
) 
-- Select all columns from the CTE where department_id is not null
SELECT *
FROM CTE
WHERE department_id IS NOT NULL

# COMMAND ----------

--Process 2
WITH cte as( SELECT 
employee_id,
department_id,  
row_number() over (partition by employee_id order by primary_flag desc) as pos
FROM Employee
) SELECT employee_id, department_id from cte where pos = 1

