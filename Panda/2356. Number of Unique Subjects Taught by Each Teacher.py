# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Teacher
# MAGIC
# MAGIC +-------------+------+
# MAGIC | Column Name | Type |
# MAGIC +-------------+------+
# MAGIC | teacher_id  | int  |
# MAGIC | subject_id  | int  |
# MAGIC | dept_id     | int  |
# MAGIC +-------------+------+
# MAGIC (subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
# MAGIC Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.
# MAGIC  
# MAGIC
# MAGIC Write a solution to calculate the number of unique subjects each teacher teaches in the university.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC The result format is shown in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Teacher table:
# MAGIC +------------+------------+---------+
# MAGIC | teacher_id | subject_id | dept_id |
# MAGIC +------------+------------+---------+
# MAGIC | 1          | 2          | 3       |
# MAGIC | 1          | 2          | 4       |
# MAGIC | 1          | 3          | 3       |
# MAGIC | 2          | 1          | 1       |
# MAGIC | 2          | 2          | 1       |
# MAGIC | 2          | 3          | 1       |
# MAGIC | 2          | 4          | 1       |
# MAGIC +------------+------------+---------+
# MAGIC Output:  
# MAGIC +------------+-----+
# MAGIC | teacher_id | cnt |
# MAGIC +------------+-----+
# MAGIC | 1          | 2   |
# MAGIC | 2          | 4   |
# MAGIC +------------+-----+
# MAGIC Explanation: 
# MAGIC Teacher 1:
# MAGIC   - They teach subject 2 in departments 3 and 4.
# MAGIC   - They teach subject 3 in department 3.
# MAGIC Teacher 2:
# MAGIC   - They teach subject 1 in department 1.
# MAGIC   - They teach subject 2 in department 1.
# MAGIC   - They teach subject 3 in department 1.
# MAGIC   - They teach subject 4 in department 1.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 480 ms
# MAGIC <h3> Beats: </h3> 59.19%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Group by 'teacher_id' and 'subject_id', then count the occurrences and reset the index
    teacher = teacher.groupby(['teacher_id', 'subject_id']).size().reset_index(name='count')

    # Calculate the sum of 'count' for each 'teacher_id' and assign it to a new column 'cnt'
    teacher['cnt'] = teacher.groupby('teacher_id')['count'].transform('sum')

    # Select 'teacher_id' and 'cnt' columns, then drop duplicate rows
    teacher = teacher[['teacher_id', 'cnt']].drop_duplicates()

    return teacher
