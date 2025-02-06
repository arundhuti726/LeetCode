# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Triangle
# MAGIC
# MAGIC +-------------+------+
# MAGIC | Column Name | Type |
# MAGIC +-------------+------+
# MAGIC | x           | int  |
# MAGIC | y           | int  |
# MAGIC | z           | int  |
# MAGIC +-------------+------+
# MAGIC In SQL, (x, y, z) is the primary key column for this table.
# MAGIC Each row of this table contains the lengths of three line segments.
# MAGIC  
# MAGIC
# MAGIC Report for every three line segments whether they can form a triangle.
# MAGIC
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC The result format is in the following example.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 403 ms
# MAGIC <h3> Beats: </h3> 82.21%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

/* Write your T-SQL query statement below */

/* Select columns x, y, z and a case statement to determine if they form a triangle */
select x, y, z,
Case when T1*T2*T3=1 then 'Yes' /* If all conditions are met, it's a triangle */
else 'No' end as triangle /* Otherwise, it's not a triangle */
from(
/* Select all columns and calculate T1, T2, T3 for triangle inequality conditions */
select *,
CASE WHEN (abs(x)+abs(y))>abs(z) THEN 1 /* Check if sum of abs(x) and abs(y) is greater than abs(z) */
     Else 0
     End   as T1,
CASE WHEN (abs(z)+abs(y))>abs(x) THEN 1 /* Check if sum of abs(z) and abs(y) is greater than abs(x) */
     Else 0
     End   as T2,
CASE WHEN (abs(x)+abs(z))>abs(y) THEN 1 /* Check if sum of abs(x) and abs(z) is greater than abs(y) */
     Else 0
     End   as T3
from Triangle)a /* From the Triangle table */
