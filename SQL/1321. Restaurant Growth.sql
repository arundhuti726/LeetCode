-- Databricks notebook source
-- MAGIC %md
-- MAGIC <h5> ROBLEM DESCRIPTION </h5>
-- MAGIC Customer
-- MAGIC
-- MAGIC +---------------+---------+
-- MAGIC | Column Name   | Type    |
-- MAGIC +---------------+---------+
-- MAGIC | customer_id   | int     |
-- MAGIC | name          | varchar |
-- MAGIC | visited_on    | date    |
-- MAGIC | amount        | int     |
-- MAGIC +---------------+---------+
-- MAGIC In SQL,(customer_id, visited_on) is the primary key for this table.
-- MAGIC This table contains data about customer transactions in a restaurant.
-- MAGIC visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
-- MAGIC amount is the total paid by a customer.
-- MAGIC  
-- MAGIC
-- MAGIC You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).
-- MAGIC
-- MAGIC Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.
-- MAGIC
-- MAGIC Return the result table ordered by visited_on in ascending order.
-- MAGIC
-- MAGIC The result format is in the following example.
-- MAGIC
-- MAGIC  
-- MAGIC
-- MAGIC Example 1:
-- MAGIC
-- MAGIC Input: 
-- MAGIC Customer table:
-- MAGIC +-------------+--------------+--------------+-------------+
-- MAGIC | customer_id | name         | visited_on   | amount      |
-- MAGIC +-------------+--------------+--------------+-------------+
-- MAGIC | 1           | Jhon         | 2019-01-01   | 100         |
-- MAGIC | 2           | Daniel       | 2019-01-02   | 110         |
-- MAGIC | 3           | Jade         | 2019-01-03   | 120         |
-- MAGIC | 4           | Khaled       | 2019-01-04   | 130         |
-- MAGIC | 5           | Winston      | 2019-01-05   | 110         | 
-- MAGIC | 6           | Elvis        | 2019-01-06   | 140         | 
-- MAGIC | 7           | Anna         | 2019-01-07   | 150         |
-- MAGIC | 8           | Maria        | 2019-01-08   | 80          |
-- MAGIC | 9           | Jaze         | 2019-01-09   | 110         | 
-- MAGIC | 1           | Jhon         | 2019-01-10   | 130         | 
-- MAGIC | 3           | Jade         | 2019-01-10   | 150         | 
-- MAGIC +-------------+--------------+--------------+-------------+
-- MAGIC Output: 
-- MAGIC +--------------+--------------+----------------+
-- MAGIC | visited_on   | amount       | average_amount |
-- MAGIC +--------------+--------------+----------------+
-- MAGIC | 2019-01-07   | 860          | 122.86         |
-- MAGIC | 2019-01-08   | 840          | 120            |
-- MAGIC | 2019-01-09   | 840          | 120            |
-- MAGIC | 2019-01-10   | 1000         | 142.86         |
-- MAGIC +--------------+--------------+----------------+
-- MAGIC Explanation: 
-- MAGIC 1st moving average from 2019-01-01 to 2019-01-07 has an average_amount of (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
-- MAGIC 2nd moving average from 2019-01-02 to 2019-01-08 has an average_amount of (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
-- MAGIC 3rd moving average from 2019-01-03 to 2019-01-09 has an average_amount of (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
-- MAGIC 4th moving average from 2019-01-04 to 2019-01-10 has an average_amount of (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Run Time: </h3> 580 ms
-- MAGIC <h3> Beats: </h3> 57.36%
-- MAGIC <h3> Complexity: </h3> O(n log n)

-- COMMAND ----------

-- Define a common table expression (CTE) named 'cte'
with cte as
(
  -- Select visited_on, calculate a 7-day rolling sum of amount, and assign row numbers
  select visited_on, 
         sum(amount) over (order by visited_on rows between 6 PRECEDING AND CURRENT ROW) as amount,
         row_number() over (order by visited_on) as days_vist
  -- Aggregate the amount by visited_on date
  from (select visited_on, sum(amount) as amount from Customer group by visited_on) a
) 
-- Select visited_on, amount, and calculate the average amount over 7 days
select visited_on, 
       amount, 
       round(amount/7.0, 2) as average_amount 
from cte
-- Filter to include only rows where the day number is greater than 6
where days_vist > 6

-- COMMAND ----------

-- MAGIC %md
-- MAGIC [LINK: ROWS BETWEEN in SQL ](https://learnsql.com/blog/sql-window-functions-rows-clause/)
