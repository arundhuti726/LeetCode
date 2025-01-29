# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Courses
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | student     | varchar |
# MAGIC | class       | varchar |
# MAGIC +-------------+---------+
# MAGIC (student, class) is the primary key (combination of columns with unique values) for this table.
# MAGIC Each row of this table indicates the name of a student and the class in which they are enrolled.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find all the classes that have at least five students.
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
# MAGIC Courses table:
# MAGIC +---------+----------+
# MAGIC | student | class    |
# MAGIC +---------+----------+
# MAGIC | A       | Math     |
# MAGIC | B       | English  |
# MAGIC | C       | Math     |
# MAGIC | D       | Biology  |
# MAGIC | E       | Math     |
# MAGIC | F       | Computer |
# MAGIC | G       | Math     |
# MAGIC | H       | Math     |
# MAGIC | I       | Math     |
# MAGIC +---------+----------+
# MAGIC Output: 
# MAGIC +---------+
# MAGIC | class   |
# MAGIC +---------+
# MAGIC | Math    |
# MAGIC +---------+
# MAGIC Explanation: 
# MAGIC - Math has 6 students, so we include it.
# MAGIC - English has 1 student, so we do not include it.
# MAGIC - Biology has 1 student, so we do not include it.
# MAGIC - Computer has 1 student, so we do not include it.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 1630 ms
# MAGIC <h3> Beats: </h3> 26.68%
# MAGIC <h3> Complexity: </h3>

# COMMAND ----------

/* Write your T-SQL query statement below */
select class
from(
select class,count(class) as total
from Courses
group by class)a
where total>4

