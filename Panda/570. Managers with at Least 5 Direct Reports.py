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
# MAGIC ### Run Time: </h3> 411 ms
# MAGIC <h3> Beats: </h3> 78.91%
# MAGIC <h3> Complexity: </h3> O

# COMMAND ----------

# Define a function to find managers with at least 5 direct reports
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    # Count the number of direct reports for each manager
    employee['count_reporty'] = employee.groupby(['managerId']).cumcount() + 1

    # Filter managers with at least 5 direct reports and get unique manager IDs
    employee2 = employee[employee['count_reporty'] >= 5][['managerId']].drop_duplicates()

    # Merge the original dataframe with the filtered managers to get their names
    employee = employee.merge(employee2, left_on='id', right_on='managerId', how='inner')[['name']]

    # Return the dataframe containing the names of the managers
    return employee
