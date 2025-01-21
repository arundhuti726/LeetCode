# Databricks notebook source
# MAGIC
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Employees
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | employee_id | int     |
# MAGIC | name        | varchar |
# MAGIC | salary      | int     |
# MAGIC +-------------+---------+
# MAGIC employee_id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table indicates the employee ID, employee name, and salary.
# MAGIC  
# MAGIC
# MAGIC Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
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
# MAGIC +-------------+---------+--------+
# MAGIC | employee_id | name    | salary |
# MAGIC +-------------+---------+--------+
# MAGIC | 2           | Meir    | 3000   |
# MAGIC | 3           | Michael | 3800   |
# MAGIC | 7           | Addilyn | 7400   |
# MAGIC | 8           | Juan    | 6100   |
# MAGIC | 9           | Kannon  | 7700   |
# MAGIC +-------------+---------+--------+
# MAGIC Output: 
# MAGIC +-------------+-------+
# MAGIC | employee_id | bonus |
# MAGIC +-------------+-------+
# MAGIC | 2           | 0     |
# MAGIC | 3           | 0     |
# MAGIC | 7           | 7400  |
# MAGIC | 8           | 0     |
# MAGIC | 9           | 7700  |
# MAGIC +-------------+-------+
# MAGIC Explanation: 
# MAGIC The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
# MAGIC The employee with ID 3 gets 0 bonus because their name starts with 'M'.
# MAGIC The rest of the employees get a 100% bonus.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 430 ms
# MAGIC <h3> Beats: </h3> 62,71
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

# My approach 578 ms, beats 29.23%
# import pandas as pd
# import numpy as np

# def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
#     df = pd.DataFrame(employees)
#     # Create a 'bonus' column  and update it based on the condition: 
#     # if employee_id is odd and name does not start with 'M' (case insensitive), set bonus to salary, otherwise set to 0
#       # The get method can grab a given index of the string.
#     df['bonus'] = np.where((df['employee_id']%2!=0) & (~df['name'].str.upper().str.get(0).isin(['M'])),df['salary'],0)
#     # Select only 'employee_id' and 'bonus' columns, sort by 'employee_id', and display the DataFrame
#     #df = df[['employee_id','bonus']].sort_values('employee_id')
#     return df[['employee_id','bonus']].sort_values('employee_id')

# CASE STATEMENT SYNTAX     
#df['new_column'] = np.where(df['col2']<9, 'value1',
#                    np.where(df['col2']<12, 'value2',
#                    np.where(df['col2']<15, 'value3', 'value4')))
# This particular function looks at the value in the column called col2 and returns:

# “value1” if the value in col2 is less than 9
# “value2” if the value in col2 is less than 12
# “value3” if the value in col2 is less than 15
# “value4” if none of the previous conditions are true

# BEST Approach according to Leet submission 430 ms beats 60.38 %
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    is_odd = (employees['employee_id'] % 2 == 1)
    doesnt_start_with_M = ~employees['name'].str.startswith('M')
    employees['bonus'] = np.where(is_odd & doesnt_start_with_M, employees['salary'], 0)
    return employees[['employee_id', 'bonus']].sort_values(by=['employee_id'])
   
