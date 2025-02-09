-- Databricks notebook source
-- MAGIC %md
-- MAGIC <h5> ROBLEM DESCRIPTION </h5>
-- MAGIC Insurance
-- MAGIC
-- MAGIC +-------------+-------+
-- MAGIC | Column Name | Type  |
-- MAGIC +-------------+-------+
-- MAGIC | pid         | int   |
-- MAGIC | tiv_2015    | float |
-- MAGIC | tiv_2016    | float |
-- MAGIC | lat         | float |
-- MAGIC | lon         | float |
-- MAGIC +-------------+-------+
-- MAGIC pid is the primary key (column with unique values) for this table.
-- MAGIC Each row of this table contains information about one policy where:
-- MAGIC pid is the policyholder's policy ID.
-- MAGIC tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
-- MAGIC lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
-- MAGIC lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.
-- MAGIC  
-- MAGIC
-- MAGIC Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:
-- MAGIC
-- MAGIC have the same tiv_2015 value as one or more other policyholders, and
-- MAGIC are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
-- MAGIC Round tiv_2016 to two decimal places.
-- MAGIC
-- MAGIC The result format is in the following example.
-- MAGIC
-- MAGIC  
-- MAGIC
-- MAGIC Example 1:
-- MAGIC
-- MAGIC Input: 
-- MAGIC Insurance table:
-- MAGIC +-----+----------+----------+-----+-----+
-- MAGIC | pid | tiv_2015 | tiv_2016 | lat | lon |
-- MAGIC +-----+----------+----------+-----+-----+
-- MAGIC | 1   | 10       | 5        | 10  | 10  |
-- MAGIC | 2   | 20       | 20       | 20  | 20  |
-- MAGIC | 3   | 10       | 30       | 20  | 20  |
-- MAGIC | 4   | 10       | 40       | 40  | 40  |
-- MAGIC +-----+----------+----------+-----+-----+
-- MAGIC Output: 
-- MAGIC +----------+
-- MAGIC | tiv_2016 |
-- MAGIC +----------+
-- MAGIC | 45.00    |
-- MAGIC +----------+
-- MAGIC Explanation: 
-- MAGIC The first record in the table, like the last record, meets both of the two criteria.
-- MAGIC The tiv_2015 value 10 is the same as the third and fourth records, and its location is unique.
-- MAGIC
-- MAGIC The second record does not meet any of the two criteria. Its tiv_2015 is not like any other policyholders and its location is the same as the third record, which makes the third record fail, too.
-- MAGIC So, the result is the sum of tiv_2016 of the first and last record, which is 45.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Run Time: </h3> 646 ms
-- MAGIC <h3> Beats: </h3> 91.71%
-- MAGIC <h3> Complexity: </h3> O(n)

-- COMMAND ----------

with cte as
(
select pid, tiv_2015, tiv_2016, 
count(tiv_2015) over (partition by tiv_2015) as tiv_2015_count,  -- count of rows with the same tiv_2015 value
count(*) over (partition by lat, lon) as lat_lon_count  -- count of rows with the same lat & lon
from Insurance

) 
select round(sum(tiv_2016*1.0), 2) as tiv_2016  -- sum of tiv_2016 values rounded to 2 decimal places
from cte
where lat_lon_count = 1 and tiv_2015_count > 1  -- filter rows not located in the same city and have the same tiv_2015 value
