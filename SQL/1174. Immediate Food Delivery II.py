# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Delivery
# MAGIC
# MAGIC +-----------------------------+---------+
# MAGIC | Column Name                 | Type    |
# MAGIC +-----------------------------+---------+
# MAGIC | delivery_id                 | int     |
# MAGIC | customer_id                 | int     |
# MAGIC | order_date                  | date    |
# MAGIC | customer_pref_delivery_date | date    |
# MAGIC +-----------------------------+---------+
# MAGIC delivery_id is the column of unique values of this table.
# MAGIC The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
# MAGIC  
# MAGIC
# MAGIC If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
# MAGIC
# MAGIC The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.
# MAGIC
# MAGIC Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Delivery table:
# MAGIC +-------------+-------------+------------+-----------------------------+
# MAGIC | delivery_id | customer_id | order_date | customer_pref_delivery_date |
# MAGIC +-------------+-------------+------------+-----------------------------+
# MAGIC | 1           | 1           | 2019-08-01 | 2019-08-02                  |
# MAGIC | 2           | 2           | 2019-08-02 | 2019-08-02                  |
# MAGIC | 3           | 1           | 2019-08-11 | 2019-08-12                  |
# MAGIC | 4           | 3           | 2019-08-24 | 2019-08-24                  |
# MAGIC | 5           | 3           | 2019-08-21 | 2019-08-22                  |
# MAGIC | 6           | 2           | 2019-08-11 | 2019-08-13                  |
# MAGIC | 7           | 4           | 2019-08-09 | 2019-08-09                  |
# MAGIC +-------------+-------------+------------+-----------------------------+
# MAGIC Output: 
# MAGIC +----------------------+
# MAGIC | immediate_percentage |
# MAGIC +----------------------+
# MAGIC | 50.00                |
# MAGIC +----------------------+
# MAGIC Explanation: 
# MAGIC The customer id 1 has a first order with delivery id 1 and it is scheduled.
# MAGIC The customer id 2 has a first order with delivery id 2 and it is immediate.
# MAGIC The customer id 3 has a first order with delivery id 5 and it is scheduled.
# MAGIC The customer id 4 has a first order with delivery id 7 and it is immediate.
# MAGIC Hence, half the customers have immediate first orders.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 2966 ms
# MAGIC <h3> Beats: </h3> 14.10%
# MAGIC <h3> Complexity: </h3>

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Write your T-SQL query statement below */
# MAGIC --Process 1 3360 ms
# MAGIC -- select round((count(*) * 100.0) / (select count(distinct customer_id) from Delivery), 2) as immediate_percentage  from (
# MAGIC -- select 
# MAGIC --     customer_id,
# MAGIC --     count(*) over (partition by customer_id) as total_customers,
# MAGIC --     order_date,
# MAGIC --     min(order_date) over (partition by customer_id) as first_order,
# MAGIC --     (case when order_date = customer_pref_delivery_date then 'immediate'
# MAGIC --           else 'scheduled' end) as Order_Type,
# MAGIC --     dense_rank() over (partition by customer_id order by order_date) as order_rank      
# MAGIC --   from Delivery)a
# MAGIC --   where a.order_rank = 1 and a.Order_Type = 'immediate'
# MAGIC
# MAGIC --PROCESS 2, 480 ms (best Process from leet submission)
# MAGIC -- with first_order as
# MAGIC -- (
# MAGIC --     select customer_id, min(order_date) AS first_order_date
# MAGIC --     from Delivery
# MAGIC --     group by customer_id
# MAGIC -- )
# MAGIC -- select 
# MAGIC --         round(avg(case
# MAGIC --                     when order_date = customer_pref_delivery_date then 1.0
# MAGIC --                     else 0.0
# MAGIC --                 end) * 100, 2) as immediate_percentage
# MAGIC -- from Delivery d
# MAGIC -- join first_order fo
# MAGIC -- on d.customer_id = fo.customer_id
# MAGIC -- and d.order_date = fo.
# MAGIC
# MAGIC --PROCESS 3, 2803 ms (my Process)
# MAGIC with order_type as
# MAGIC (
# MAGIC select customer_id, order_date,
# MAGIC (case when order_date = customer_pref_delivery_date then 'immediate'
# MAGIC else 'scheduled' end) as Order_Type
# MAGIC from Delivery
# MAGIC ),
# MAGIC first_order as
# MAGIC (
# MAGIC     select customer_id, min(order_date) AS first_order_date
# MAGIC     from Delivery
# MAGIC     group by customer_id
# MAGIC )
# MAGIC  select round(count(t1.customer_id)*100.0/(select count(distinct customer_id) from Delivery),2) as immediate_percentage
# MAGIC  from order_type t1
# MAGIC  join first_order t2
# MAGIC  on t1.customer_id = t2.customer_id and t1.order_date = t2.first_order_date
# MAGIC  where t1.Order_Type = 'immediate'
# MAGIC   
