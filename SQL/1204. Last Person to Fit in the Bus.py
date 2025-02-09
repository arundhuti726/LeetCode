# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Queue
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | person_id   | int     |
# MAGIC | person_name | varchar |
# MAGIC | weight      | int     |
# MAGIC | turn        | int     |
# MAGIC +-------------+---------+
# MAGIC person_id column contains unique values.
# MAGIC This table has the information about all people waiting for a bus.
# MAGIC The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
# MAGIC turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board.
# MAGIC weight is the weight of the person in kilograms.
# MAGIC  
# MAGIC
# MAGIC There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.
# MAGIC
# MAGIC Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.
# MAGIC
# MAGIC Note that only one person can board the bus at any given turn.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Queue table:
# MAGIC +-----------+-------------+--------+------+
# MAGIC | person_id | person_name | weight | turn |
# MAGIC +-----------+-------------+--------+------+
# MAGIC | 5         | Alice       | 250    | 1    |
# MAGIC | 4         | Bob         | 175    | 5    |
# MAGIC | 3         | Alex        | 350    | 2    |
# MAGIC | 6         | John Cena   | 400    | 3    |
# MAGIC | 1         | Winston     | 500    | 6    |
# MAGIC | 2         | Marie       | 200    | 4    |
# MAGIC +-----------+-------------+--------+------+
# MAGIC Output: 
# MAGIC +-------------+
# MAGIC | person_name |
# MAGIC +-------------+
# MAGIC | John Cena   |
# MAGIC +-------------+
# MAGIC Explanation: The folowing table is ordered by the turn for simplicity.
# MAGIC +------+----+-----------+--------+--------------+
# MAGIC | Turn | ID | Name      | Weight | Total Weight |
# MAGIC +------+----+-----------+--------+--------------+
# MAGIC | 1    | 5  | Alice     | 250    | 250          |
# MAGIC | 2    | 3  | Alex      | 350    | 600          |
# MAGIC | 3    | 6  | John Cena | 400    | 1000         | (last person to board)
# MAGIC | 4    | 2  | Marie     | 200    | 1200         | (cannot board)
# MAGIC | 5    | 4  | Bob       | 175    | ___          |
# MAGIC | 6    | 1  | Winston   | 500    | ___          |
# MAGIC +------+----+-----------+--------+--------------+

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 2631 ms
# MAGIC <h3> Beats: </h3> 67.41%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Write your T-SQL query statement below */
# MAGIC with cte as
# MAGIC (
# MAGIC    select *, sum(weight) over (order by turn) as runningtotal 
# MAGIC    from Queue
# MAGIC )
# MAGIC select top 1 person_name 
# MAGIC from cte
# MAGIC where runningtotal <= 1000
# MAGIC order by turn desc
# MAGIC
