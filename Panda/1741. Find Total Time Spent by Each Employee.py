# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Employees
# MAGIC
# MAGIC +-------------+------+
# MAGIC | Column Name | Type |
# MAGIC +-------------+------+
# MAGIC | emp_id      | int  |
# MAGIC | event_day   | date |
# MAGIC | in_time     | int  |
# MAGIC | out_time    | int  |
# MAGIC +-------------+------+
# MAGIC (emp_id, event_day, in_time) is the primary key (combinations of columns with unique values) of this table.
# MAGIC The table shows the employees' entries and exits in an office.
# MAGIC event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
# MAGIC in_time and out_time are between 1 and 1440.
# MAGIC It is guaranteed that no two events on the same day intersect in time, and in_time < out_time.
# MAGIC  
# MAGIC
# MAGIC Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.
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
# MAGIC +--------+------------+---------+----------+
# MAGIC | emp_id | event_day  | in_time | out_time |
# MAGIC +--------+------------+---------+----------+
# MAGIC | 1      | 2020-11-28 | 4       | 32       |
# MAGIC | 1      | 2020-11-28 | 55      | 200      |
# MAGIC | 1      | 2020-12-03 | 1       | 42       |
# MAGIC | 2      | 2020-11-28 | 3       | 33       |
# MAGIC | 2      | 2020-12-09 | 47      | 74       |
# MAGIC +--------+------------+---------+----------+
# MAGIC Output: 
# MAGIC +------------+--------+------------+
# MAGIC | day        | emp_id | total_time |
# MAGIC +------------+--------+------------+
# MAGIC | 2020-11-28 | 1      | 173        |
# MAGIC | 2020-11-28 | 2      | 30         |
# MAGIC | 2020-12-03 | 1      | 41         |
# MAGIC | 2020-12-09 | 2      | 27         |
# MAGIC +------------+--------+------------+
# MAGIC Explanation: 
# MAGIC Employee 1 has three events: two on day 2020-11-28 with a total of (32 - 4) + (200 - 55) = 173, and one on day 2020-12-03 with a total of (42 - 1) = 41.
# MAGIC Employee 2 has two events: one on day 2020-11-28 with a total of (33 - 3) = 30, and one on day 2020-12-09 with a total of (74 - 47) = 27.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 375 ms
# MAGIC <h3> Beats: </h3> 88.29%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time']=employees['out_time']-employees['in_time']
    employees = employees.groupby(['emp_id','event_day'])['total_time'].sum().reset_index()
    employees = employees.rename(columns={'event_day':'day'})
    return employees
