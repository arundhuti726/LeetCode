# Databricks notebook source
# MAGIC
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Person
# MAGIC
# MAGIC +-------------+---------+
# MAGIC | Column Name | Type    |
# MAGIC +-------------+---------+
# MAGIC | id          | int     |
# MAGIC | email       | varchar |
# MAGIC +-------------+---------+
# MAGIC id is the primary key (column with unique values) for this table.
# MAGIC Each row of this table contains an email. The emails will not contain uppercase letters.
# MAGIC  
# MAGIC
# MAGIC Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
# MAGIC
# MAGIC For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
# MAGIC
# MAGIC For Pandas users, please note that you are supposed to modify Person in place.
# MAGIC
# MAGIC After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
# MAGIC
# MAGIC The result format is in the following example.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 459 ms
# MAGIC <h3> Beats: </h3> 48.03%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

# Import pandas library
import pandas as pd

# Define a function to delete duplicate emails from a DataFrame
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the DataFrame by 'id' column
    person.sort_values(by='id', inplace=True)
    # Drop duplicate rows based on 'email' column, keeping the first occurrence
    person.drop_duplicates(subset='email', keep='first', inplace=True)

# COMMAND ----------

# Define a function to delete duplicate emails from a DataFrame
def delete_duplicate_emails(person):
    # Sort the DataFrame by 'id' column
    person = person.orderBy('id')
    # Drop duplicate rows based on 'email' column, keeping the first occurrence
    person = person.dropDuplicates(['email'])
    return person
