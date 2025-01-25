# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Seat
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | id          | int     |
# MAGIC | student     | varchar |
# MAGIC +-------------+---------+
# MAGIC id is the primary key (unique value) column for this table.
# MAGIC Each row of this table indicates the name and the ID of a student.
# MAGIC The ID sequence always starts from 1 and increments continuously.
# MAGIC  
# MAGIC
# MAGIC Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.
# MAGIC
# MAGIC Return the result table ordered by id in ascending order.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Seat table:
# MAGIC +----+---------+
# MAGIC | id | student |
# MAGIC +----+---------+
# MAGIC | 1  | Abbot   |
# MAGIC | 2  | Doris   |
# MAGIC | 3  | Emerson |
# MAGIC | 4  | Green   |
# MAGIC | 5  | Jeames  |
# MAGIC +----+---------+
# MAGIC Output: 
# MAGIC +----+---------+
# MAGIC | id | student |
# MAGIC +----+---------+
# MAGIC | 1  | Doris   |
# MAGIC | 2  | Abbot   |
# MAGIC | 3  | Green   |
# MAGIC | 4  | Emerson |
# MAGIC | 5  | Jeames  |
# MAGIC +----+---------+
# MAGIC Explanation: 
# MAGIC Note that if the number of students is odd, there is no need to change the last one's seat.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 819 ms
# MAGIC <h3> Beats: </h3> 13.62%
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC /* Write your T-SQL query statement below */
# MAGIC select id,
# MAGIC (case when id%2=1 and nxt_stu is not null then nxt_stu 
# MAGIC       when id%2=1 and nxt_stu is null then student
# MAGIC       else pre_stu end) as student
# MAGIC from(
# MAGIC select *, lead(student) over (order by id) as nxt_stu,
# MAGIC lag(student) over (order by id) as pre_stu
# MAGIC
# MAGIC from Seat
# MAGIC ) a
# MAGIC order by id
