# Databricks notebook source
# MAGIC
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Products
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | product_id  | int     |
# MAGIC | store1      | int     |
# MAGIC | store2      | int     |
# MAGIC | store3      | int     |
# MAGIC +-------------+---------+
# MAGIC product_id is the primary key (column with unique values) for this table.
# MAGIC Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
# MAGIC If the product is not available in a store, the price will be null in that store's column.
# MAGIC  
# MAGIC
# MAGIC Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
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
# MAGIC Products table:
# MAGIC +------------+--------+--------+--------+
# MAGIC | product_id | store1 | store2 | store3 |
# MAGIC +------------+--------+--------+--------+
# MAGIC | 0          | 95     | 100    | 105    |
# MAGIC | 1          | 70     | null   | 80     |
# MAGIC +------------+--------+--------+--------+
# MAGIC Output: 
# MAGIC +------------+--------+-------+
# MAGIC | product_id | store  | price |
# MAGIC +------------+--------+-------+
# MAGIC | 0          | store1 | 95    |
# MAGIC | 0          | store2 | 100   |
# MAGIC | 0          | store3 | 105   |
# MAGIC | 1          | store1 | 70    |
# MAGIC | 1          | store3 | 80    |
# MAGIC +------------+--------+-------+
# MAGIC Explanation: 
# MAGIC Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
# MAGIC Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 481 ms
# MAGIC <h3> Beats: </h3> 65.32%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = pd.melt(products,id_vars=['product_id'],value_vars=['store1','store2','store3'],
        var_name='store', value_name='price').dropna()
    
    return products
    
