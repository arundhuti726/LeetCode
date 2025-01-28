# Databricks notebook source
# MAGIC
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Employee
# MAGIC
# MAGIC +--------------+---------+
# MAGIC | Column Name  | Type    |
# MAGIC +--------------+---------+
# MAGIC | id           | int     |
# MAGIC | name         | varchar |
# MAGIC | salary       | int     |
# MAGIC | departmentId | int     |
# MAGIC +--------------+---------+
# MAGIC id is the primary key (column with unique values) for this table.
# MAGIC departmentId is a foreign key (reference columns) of the ID from the Department table.
# MAGIC Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
# MAGIC  
# MAGIC
# MAGIC Table: Department
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | id          | int     |
# MAGIC | name        | varchar |
# MAGIC +-------------+---------+
# MAGIC id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
# MAGIC Each row of this table indicates the ID of a department and its name.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find employees who have the highest salary in each of the departments.
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
# MAGIC +----+-------+--------+--------------+
# MAGIC | id | name  | salary | departmentId |
# MAGIC +----+-------+--------+--------------+
# MAGIC | 1  | Joe   | 70000  | 1            |
# MAGIC | 2  | Jim   | 90000  | 1            |
# MAGIC | 3  | Henry | 80000  | 2            |
# MAGIC | 4  | Sam   | 60000  | 2            |
# MAGIC | 5  | Max   | 90000  | 1            |
# MAGIC +----+-------+--------+--------------+
# MAGIC Department table:
# MAGIC +----+-------+
# MAGIC | id | name  |
# MAGIC +----+-------+
# MAGIC | 1  | IT    |
# MAGIC | 2  | Sales |
# MAGIC +----+-------+
# MAGIC Output: 
# MAGIC +------------+----------+--------+
# MAGIC | Department | Employee | Salary |
# MAGIC +------------+----------+--------+
# MAGIC | IT         | Jim      | 90000  |
# MAGIC | Sales      | Henry    | 80000  |
# MAGIC | IT         | Max      | 90000  |
# MAGIC +------------+----------+--------+
# MAGIC Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 569 ms
# MAGIC <h3> Beats: </h3> 39.98%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Rank employees within each department by salary in descending order
    employee['dense_rank'] = employee.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    # Filter employees who have the highest salary in their department
    t2 = employee[employee['dense_rank'] == 1]
    
    # Join the filtered employees with the department DataFrame on departmentId
    result = t2.merge(department, left_on='departmentId', right_on='id', how='left')[['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']

    
    return result
