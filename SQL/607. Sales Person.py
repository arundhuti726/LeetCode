# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC SalesPerson
# MAGIC
# MAGIC +-----------------+---------+
# MAGIC | Column Name     | Type    |
# MAGIC +-----------------+---------+
# MAGIC | sales_id        | int     |
# MAGIC | name            | varchar |
# MAGIC | salary          | int     |
# MAGIC | commission_rate | int     |
# MAGIC | hire_date       | date    |
# MAGIC +-----------------+---------+
# MAGIC sales_id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.
# MAGIC  
# MAGIC
# MAGIC Table: Company
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | com_id      | int     |
# MAGIC | name        | varchar |
# MAGIC | city        | varchar |
# MAGIC +-------------+---------+
# MAGIC com_id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table indicates the name and the ID of a company and the city in which the company is located.
# MAGIC  
# MAGIC
# MAGIC Table: Orders
# MAGIC
# MAGIC +-------------+------+
# MAGIC | Column Name | Type |
# MAGIC +-------------+------+
# MAGIC | order_id    | int  |
# MAGIC | order_date  | date |
# MAGIC | com_id      | int  |
# MAGIC | sales_id    | int  |
# MAGIC | amount      | int  |
# MAGIC +-------------+------+
# MAGIC order_id is the primary key (column with unique values) for this table.
# MAGIC com_id is a foreign key (reference column) to com_id from the Company table.
# MAGIC sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
# MAGIC Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
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
# MAGIC SalesPerson table:
# MAGIC +----------+------+--------+-----------------+------------+
# MAGIC | sales_id | name | salary | commission_rate | hire_date  |
# MAGIC +----------+------+--------+-----------------+------------+
# MAGIC | 1        | John | 100000 | 6               | 4/1/2006   |
# MAGIC | 2        | Amy  | 12000  | 5               | 5/1/2010   |
# MAGIC | 3        | Mark | 65000  | 12              | 12/25/2008 |
# MAGIC | 4        | Pam  | 25000  | 25              | 1/1/2005   |
# MAGIC | 5        | Alex | 5000   | 10              | 2/3/2007   |
# MAGIC +----------+------+--------+-----------------+------------+
# MAGIC Company table:
# MAGIC +--------+--------+----------+
# MAGIC | com_id | name   | city     |
# MAGIC +--------+--------+----------+
# MAGIC | 1      | RED    | Boston   |
# MAGIC | 2      | ORANGE | New York |
# MAGIC | 3      | YELLOW | Boston   |
# MAGIC | 4      | GREEN  | Austin   |
# MAGIC +--------+--------+----------+
# MAGIC Orders table:
# MAGIC +----------+------------+--------+----------+--------+
# MAGIC | order_id | order_date | com_id | sales_id | amount |
# MAGIC +----------+------------+--------+----------+--------+
# MAGIC | 1        | 1/1/2014   | 3      | 4        | 10000  |
# MAGIC | 2        | 2/1/2014   | 4      | 5        | 5000   |
# MAGIC | 3        | 3/1/2014   | 1      | 1        | 50000  |
# MAGIC | 4        | 4/1/2014   | 1      | 4        | 25000  |
# MAGIC +----------+------------+--------+----------+--------+
# MAGIC Output: 
# MAGIC +------+
# MAGIC | name |
# MAGIC +------+
# MAGIC | Amy  |
# MAGIC | Mark |
# MAGIC | Alex |
# MAGIC +------+
# MAGIC Explanation: 
# MAGIC According to orders 3 and 4 in the Orders table, it is easy to tell that only salesperson John and Pam have sales to company RED, so we report all the other names in the table salesperson.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 595 ms
# MAGIC <h3> Beats: </h3> 94.10%
# MAGIC <h3> Complexity: </h3>

# COMMAND ----------

-- Select the name column from the SalesPerson table
select name 
from SalesPerson 
-- Filter out sales_id that are present in the subquery
where sales_id not in (
    -- Subquery to get sales_id from Orders table
    select t1.sales_id
    from Orders t1
    -- Left join with Company table on com_id
    left join Company t2
    on t1.com_id = t2.com_id 
    -- Filter where the name in Company table is 'RED' (case insensitive)
    where upper(t2.name) = 'RED'
)
