# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Customers
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | id          | int     |
# MAGIC | name        | varchar |
# MAGIC +-------------+---------+
# MAGIC id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table indicates the ID and name of a customer.
# MAGIC  
# MAGIC
# MAGIC Table: Orders
# MAGIC
# MAGIC +-------------+------+
# MAGIC | Column Name | Type |
# MAGIC +-------------+------+
# MAGIC | id          | int  |
# MAGIC | customerId  | int  |
# MAGIC +-------------+------+
# MAGIC id is the primary key (column with unique values) for this table.
# MAGIC customerId is a foreign key (reference columns) of the ID from the Customers table.
# MAGIC Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find all customers who never order anything.
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
# MAGIC Customers table:
# MAGIC +----+-------+
# MAGIC | id | name  |
# MAGIC +----+-------+
# MAGIC | 1  | Joe   |
# MAGIC | 2  | Henry |
# MAGIC | 3  | Sam   |
# MAGIC | 4  | Max   |
# MAGIC +----+-------+
# MAGIC Orders table:
# MAGIC +----+------------+
# MAGIC | id | customerId |
# MAGIC +----+------------+
# MAGIC | 1  | 3          |
# MAGIC | 2  | 1          |
# MAGIC +----+------------+
# MAGIC Output: 
# MAGIC +-----------+
# MAGIC | Customers |
# MAGIC +-----------+
# MAGIC | Henry     |
# MAGIC | Max       |
# MAGIC +-----------+

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 517 ms
# MAGIC <h3> Beats: </h3> 30.64%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    #PROCESS 1   257 ms  , beats 99.03    

    # df = customers[~customers['id'].isin(orders['customerId'])].rename(columns={'name':'Customers'})
        
    # return df[['Customers']]

    # PROCESS 2   687 ms
    # result = customers[~customers['id'].isin(orders['customerId'])]
    # return result[['name']].rename(columns={'name':'Customers'})

#PROCESS 3
    d1 = pd.DataFrame(customers)
    d2 = pd.DataFrame(orders)

    
    return d1[~(d1.id).isin(d2.customerId)][['name']].rename(columns={'name':'Customers'})
