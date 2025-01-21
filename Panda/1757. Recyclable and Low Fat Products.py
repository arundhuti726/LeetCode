# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC
# MAGIC Products
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | product_id  | int     |
# MAGIC | low_fats    | enum    |
# MAGIC | recyclable  | enum    |
# MAGIC +-------------+---------+
# MAGIC product_id is the primary key (column with unique values) for this table.
# MAGIC low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
# MAGIC recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the ids of products that are both low fat and recyclable.
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
# MAGIC +-------------+----------+------------+
# MAGIC | product_id  | low_fats | recyclable |
# MAGIC +-------------+----------+------------+
# MAGIC | 0           | Y        | N          |
# MAGIC | 1           | Y        | Y          |
# MAGIC | 2           | N        | Y          |
# MAGIC | 3           | Y        | Y          |
# MAGIC | 4           | N        | N          |
# MAGIC +-------------+----------+------------+
# MAGIC Output: 
# MAGIC +-------------+
# MAGIC | product_id  |
# MAGIC +-------------+
# MAGIC | 1           |
# MAGIC | 3           |
# MAGIC +-------------+
# MAGIC Explanation: Only products 1 and 3 are both low fat and recyclable.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 275 ms
# MAGIC <h3> Beats: </h3> 97.68%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    #PRICESS 1
    #df = pd.DataFrame(products)
    #df = df.where((products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'))
    #df = products.filter((products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'))
    #d = df.loc[:,['product_id']].dropna()
    # Previous code is correct but, in many steps
    #return products.where((products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')).loc[:,['product_id']].dropna()

    # Process 2
    # df = pd.DataFrame(products)
    # df = products[(products['low_fats']=='Y') & (products['recyclable']=='Y')]
    # return df[['product_id']]

    #PROCESS 3 290 ms
    df = pd.DataFrame(products)
        
    return df[(df.low_fats=='Y')&(df.recyclable=='Y')][['product_id']]
