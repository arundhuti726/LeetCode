-- Databricks notebook source
-- MAGIC %md
-- MAGIC <h5> ROBLEM DESCRIPTION </h5>
-- MAGIC DailySales
-- MAGIC
-- MAGIC +-------------+---------+
-- MAGIC | Column Name | Type    |
-- MAGIC +-------------+---------+
-- MAGIC | date_id     | date    |
-- MAGIC | make_name   | varchar |
-- MAGIC | lead_id     | int     |
-- MAGIC | partner_id  | int     |
-- MAGIC +-------------+---------+
-- MAGIC There is no primary key (column with unique values) for this table. It may contain duplicates.
-- MAGIC This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
-- MAGIC The name consists of only lowercase English letters.
-- MAGIC  
-- MAGIC
-- MAGIC For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
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
-- MAGIC DailySales table:
-- MAGIC +-----------+-----------+---------+------------+
-- MAGIC | date_id   | make_name | lead_id | partner_id |
-- MAGIC +-----------+-----------+---------+------------+
-- MAGIC | 2020-12-8 | toyota    | 0       | 1          |
-- MAGIC | 2020-12-8 | toyota    | 1       | 0          |
-- MAGIC | 2020-12-8 | toyota    | 1       | 2          |
-- MAGIC | 2020-12-7 | toyota    | 0       | 2          |
-- MAGIC | 2020-12-7 | toyota    | 0       | 1          |
-- MAGIC | 2020-12-8 | honda     | 1       | 2          |
-- MAGIC | 2020-12-8 | honda     | 2       | 1          |
-- MAGIC | 2020-12-7 | honda     | 0       | 1          |
-- MAGIC | 2020-12-7 | honda     | 1       | 2          |
-- MAGIC | 2020-12-7 | honda     | 2       | 1          |
-- MAGIC +-----------+-----------+---------+------------+
-- MAGIC Output: 
-- MAGIC +-----------+-----------+--------------+-----------------+
-- MAGIC | date_id   | make_name | unique_leads | unique_partners |
-- MAGIC +-----------+-----------+--------------+-----------------+
-- MAGIC | 2020-12-8 | toyota    | 2            | 3               |
-- MAGIC | 2020-12-7 | toyota    | 1            | 2               |
-- MAGIC | 2020-12-8 | honda     | 2            | 2               |
-- MAGIC | 2020-12-7 | honda     | 3            | 2               |
-- MAGIC +-----------+-----------+--------------+-----------------+
-- MAGIC Explanation: 
-- MAGIC For 2020-12-8, toyota gets leads = [0, 1] and partners = [0, 1, 2] while honda gets leads = [1, 2] and partners = [1, 2].
-- MAGIC For 2020-12-7, toyota gets leads = [0] and partners = [1, 2] while honda gets leads = [0, 1, 2] and partners = [1, 2].

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Run Time: </h3> 975 ms
-- MAGIC <h3> Beats: </h3> 52.36%
-- MAGIC <h3> Complexity: </h3> 

-- COMMAND ----------

/* Write your T-SQL query statement below */

select t1.date_id, t1.make_name, count(distinct t2.lead_id) as unique_leads , count(distinct t2.partner_id) as unique_partners 
from 
(select date_id, make_name 
from DailySales 
group by date_id, make_name) t1 
inner join 
DailySales t2 
on t1.date_id = t2.date_id and t1.make_name = t2.make_name
group by t1.date_id, t1.make_name


-- COMMAND ----------

-- MAGIC %md
-- MAGIC [LINK: ROWS BETWEEN in SQL ](https://learnsql.com/blog/sql-window-functions-rows-clause/)
