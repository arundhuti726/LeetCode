-- Databricks notebook source
-- MAGIC %md
-- MAGIC <h5> ROBLEM DESCRIPTION </h5>
-- MAGIC RequestAccepted
-- MAGIC
-- MAGIC +----------------+---------+
-- MAGIC | Column Name    | Type    |
-- MAGIC +----------------+---------+
-- MAGIC | requester_id   | int     |
-- MAGIC | accepter_id    | int     |
-- MAGIC | accept_date    | date    |
-- MAGIC +----------------+---------+
-- MAGIC (requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
-- MAGIC This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
-- MAGIC  
-- MAGIC
-- MAGIC Write a solution to find the people who have the most friends and the most friends number.
-- MAGIC
-- MAGIC The test cases are generated so that only one person has the most friends.
-- MAGIC
-- MAGIC The result format is in the following example.
-- MAGIC
-- MAGIC  
-- MAGIC
-- MAGIC Example 1:
-- MAGIC
-- MAGIC Input: 
-- MAGIC RequestAccepted table:
-- MAGIC +--------------+-------------+-------------+
-- MAGIC | requester_id | accepter_id | accept_date |
-- MAGIC +--------------+-------------+-------------+
-- MAGIC | 1            | 2           | 2016/06/03  |
-- MAGIC | 1            | 3           | 2016/06/08  |
-- MAGIC | 2            | 3           | 2016/06/08  |
-- MAGIC | 3            | 4           | 2016/06/09  |
-- MAGIC +--------------+-------------+-------------+
-- MAGIC Output: 
-- MAGIC +----+-----+
-- MAGIC | id | num |
-- MAGIC +----+-----+
-- MAGIC | 3  | 3   |
-- MAGIC +----+-----+
-- MAGIC Explanation: 
-- MAGIC The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # PROCESS 1
-- MAGIC ### Run Time: </h3> 653 ms
-- MAGIC <h3> Beats: </h3> 31.30%
-- MAGIC <h3> Complexity: </h3> 
-- MAGIC
-- MAGIC # PROCESS 2
-- MAGIC
-- MAGIC ### Run Time: </h3> 479 ms
-- MAGIC <h3> Beats: </h3> 77.04%
-- MAGIC <h3> Complexity: </h3> O(n + m)

-- COMMAND ----------

/* Write your T-SQL query statement below */
--Process 1
-- with cte as
-- (
-- select requester_id as id from RequestAccepted 
-- union all
-- select accepter_id as id from RequestAccepted 
-- ) 
-- select id, count(id) as num 
-- from cte
-- group by id
-- having count(id) = (select max(count) from (select count(id) as count from cte group by id) subquery)

-- COMMAND ----------

--PROCESS 2
with cte1 as
(
-- Select requester_id and rename as id from RequestAccepted table
select requester_id as id from RequestAccepted 
-- Union with accepter_id renamed as id from RequestAccepted table
union all
select accepter_id as id from RequestAccepted 
),
cte2 as( 
-- Count occurrences of each id in cte1
select id, count(id) as num
from cte1
-- Group by id to get the count for each id
group by id)

-- Select all columns from cte2 where num is equal to the maximum num in cte2
select * from cte2
where num = (select max(num) from cte2)
