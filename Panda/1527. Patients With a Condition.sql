-- Databricks notebook source
-- MAGIC %md
-- MAGIC <h5> ROBLEM DESCRIPTION </h5>
-- MAGIC Patients
-- MAGIC
-- MAGIC +--------------+---------+
-- MAGIC | Column Name  | Type    |
-- MAGIC +--------------+---------+
-- MAGIC | patient_id   | int     |
-- MAGIC | patient_name | varchar |
-- MAGIC | conditions   | varchar |
-- MAGIC +--------------+---------+
-- MAGIC patient_id is the primary key (column with unique values) for this table.
-- MAGIC 'conditions' contains 0 or more code separated by spaces. 
-- MAGIC This table contains information of the patients in the hospital.
-- MAGIC  
-- MAGIC
-- MAGIC Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.
-- MAGIC
-- MAGIC Return the result table in any order.
-- MAGIC
-- MAGIC The result format is in the following example.
-- MAGIC
-- MAGIC  
-- MAGIC
-- MAGIC Example 1:
-- MAGIC
-- MAGIC Input: 
-- MAGIC Patients table:
-- MAGIC +------------+--------------+--------------+
-- MAGIC | patient_id | patient_name | conditions   |
-- MAGIC +------------+--------------+--------------+
-- MAGIC | 1          | Daniel       | YFEV COUGH   |
-- MAGIC | 2          | Alice        |              |
-- MAGIC | 3          | Bob          | DIAB100 MYOP |
-- MAGIC | 4          | George       | ACNE DIAB100 |
-- MAGIC | 5          | Alain        | DIAB201      |
-- MAGIC +------------+--------------+--------------+
-- MAGIC Output: 
-- MAGIC +------------+--------------+--------------+
-- MAGIC | patient_id | patient_name | conditions   |
-- MAGIC +------------+--------------+--------------+
-- MAGIC | 3          | Bob          | DIAB100 MYOP |
-- MAGIC | 4          | George       | ACNE DIAB100 | 
-- MAGIC +------------+--------------+--------------+
-- MAGIC Explanation: Bob and George both have a condition that starts with DIAB1.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Run Time: </h3> 668 ms
-- MAGIC <h3> Beats: </h3> 10.27%
-- MAGIC <h3> Complexity: </h3> 

-- COMMAND ----------

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'(^DIAB1)|( DIAB1)')]
