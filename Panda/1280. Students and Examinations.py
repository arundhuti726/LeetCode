# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Table: Students
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | student_id    | int     |
# MAGIC | student_name  | varchar |
# MAGIC +---------------+---------+
# MAGIC student_id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table contains the ID and the name of one student in the school.
# MAGIC  
# MAGIC
# MAGIC Table: Subjects
# MAGIC
# MAGIC +--------------+---------+
# MAGIC | Column Name  | Type    |
# MAGIC +--------------+---------+
# MAGIC | subject_name | varchar |
# MAGIC +--------------+---------+
# MAGIC subject_name is the primary key (column with unique values) for this table.
# MAGIC Each row of this table contains the name of one subject in the school.
# MAGIC  
# MAGIC
# MAGIC Table: Examinations
# MAGIC
# MAGIC +--------------+---------+
# MAGIC | Column Name  | Type    |
# MAGIC +--------------+---------+
# MAGIC | student_id   | int     |
# MAGIC | subject_name | varchar |
# MAGIC +--------------+---------+
# MAGIC There is no primary key (column with unique values) for this table. It may contain duplicates.
# MAGIC Each student from the Students table takes every course from the Subjects table.
# MAGIC Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the number of times each student attended each exam.
# MAGIC
# MAGIC Return the result table ordered by student_id and subject_name.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Students table:
# MAGIC +------------+--------------+
# MAGIC | student_id | student_name |
# MAGIC +------------+--------------+
# MAGIC | 1          | Alice        |
# MAGIC | 2          | Bob          |
# MAGIC | 13         | John         |
# MAGIC | 6          | Alex         |
# MAGIC +------------+--------------+
# MAGIC Subjects table:
# MAGIC +--------------+
# MAGIC | subject_name |
# MAGIC +--------------+
# MAGIC | Math         |
# MAGIC | Physics      |
# MAGIC | Programming  |
# MAGIC +--------------+
# MAGIC Examinations table:
# MAGIC +------------+--------------+
# MAGIC | student_id | subject_name |
# MAGIC +------------+--------------+
# MAGIC | 1          | Math         |
# MAGIC | 1          | Physics      |
# MAGIC | 1          | Programming  |
# MAGIC | 2          | Programming  |
# MAGIC | 1          | Physics      |
# MAGIC | 1          | Math         |
# MAGIC | 13         | Math         |
# MAGIC | 13         | Programming  |
# MAGIC | 13         | Physics      |
# MAGIC | 2          | Math         |
# MAGIC | 1          | Math         |
# MAGIC +------------+--------------+
# MAGIC Output: 
# MAGIC +------------+--------------+--------------+----------------+
# MAGIC | student_id | student_name | subject_name | attended_exams |
# MAGIC +------------+--------------+--------------+----------------+
# MAGIC | 1          | Alice        | Math         | 3              |
# MAGIC | 1          | Alice        | Physics      | 2              |
# MAGIC | 1          | Alice        | Programming  | 1              |
# MAGIC | 2          | Bob          | Math         | 1              |
# MAGIC | 2          | Bob          | Physics      | 0              |
# MAGIC | 2          | Bob          | Programming  | 1              |
# MAGIC | 6          | Alex         | Math         | 0              |
# MAGIC | 6          | Alex         | Physics      | 0              |
# MAGIC | 6          | Alex         | Programming  | 0              |
# MAGIC | 13         | John         | Math         | 1              |
# MAGIC | 13         | John         | Physics      | 1              |
# MAGIC | 13         | John         | Programming  | 1              |
# MAGIC +------------+--------------+--------------+----------------+
# MAGIC Explanation: 
# MAGIC The result table should contain all students and all subjects.
# MAGIC Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.
# MAGIC Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.
# MAGIC Alex did not attend any exams.
# MAGIC John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 848 ms
# MAGIC <h3> Beats: </h3> 14.18%
# MAGIC <h3> Complexity: </h3>

# COMMAND ----------

def students_and_examinations(students, subjects, examinations):
    # Perform a cross join between students and subjects
    df = students.merge(subjects, how='cross')
    
    # Group examinations by student_id and subject_name, and count the number of exams attended
    exam_count = examinations.groupby(['student_id', 'subject_name']).agg(exams_attended=('subject_name', 'count')).reset_index()
    
    # Merge the cross-joined dataframe with the exam count dataframe on student_id and subject_name
    df1 = df.merge(exam_count, on=['student_id','subject_name'], how='left').sort_values(by = ['student_id', 'subject_name'])

    # Fill NaN values in exams_attended with 0
    df1['attended_exams'] = df1['exams_attended'].fillna(0)
    
    # Drop the exams_attended column
    final_df = df1.drop('exams_attended',axis=1)
    
    return final_df
