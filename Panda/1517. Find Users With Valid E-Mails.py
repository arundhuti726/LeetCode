# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Users
# MAGIC
# MAGIC +---------------+---------+
# MAGIC | Column Name   | Type    |
# MAGIC +---------------+---------+
# MAGIC | user_id       | int     |
# MAGIC | name          | varchar |
# MAGIC | mail          | varchar |
# MAGIC +---------------+---------+
# MAGIC user_id is the primary key (column with unique values) for this table.
# MAGIC This table contains information of the users signed up in a website. Some e-mails are invalid.
# MAGIC  
# MAGIC
# MAGIC Write a solution to find the users who have valid emails.
# MAGIC
# MAGIC A valid e-mail has a prefix name and a domain where:
# MAGIC
# MAGIC The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
# MAGIC The domain is '@leetcode.com'.
# MAGIC Return the result table in any order.
# MAGIC
# MAGIC The result format is in the following example.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: 
# MAGIC Users table:
# MAGIC +---------+-----------+-------------------------+
# MAGIC | user_id | name      | mail                    |
# MAGIC +---------+-----------+-------------------------+
# MAGIC | 1       | Winston   | winston@leetcode.com    |
# MAGIC | 2       | Jonathan  | jonathanisgreat         |
# MAGIC | 3       | Annabelle | bella-@leetcode.com     |
# MAGIC | 4       | Sally     | sally.come@leetcode.com |
# MAGIC | 5       | Marwan    | quarz#2020@leetcode.com |
# MAGIC | 6       | David     | david69@gmail.com       |
# MAGIC | 7       | Shapiro   | .shapo@leetcode.com     |
# MAGIC +---------+-----------+-------------------------+
# MAGIC Output: 
# MAGIC +---------+-----------+-------------------------+
# MAGIC | user_id | name      | mail                    |
# MAGIC +---------+-----------+-------------------------+
# MAGIC | 1       | Winston   | winston@leetcode.com    |
# MAGIC | 3       | Annabelle | bella-@leetcode.com     |
# MAGIC | 4       | Sally     | sally.come@leetcode.com |
# MAGIC +---------+-----------+-------------------------+
# MAGIC Explanation: 
# MAGIC The mail of user 2 does not have a domain.
# MAGIC The mail of user 5 has the # sign which is not allowed.
# MAGIC The mail of user 6 does not have the leetcode domain.
# MAGIC The mail of user 7 starts with a period.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 350 ms
# MAGIC <h3> Beats: </h3> 72.54 %
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
     # Process 1  944 ms
    #df = pd.DataFrame(users)
        #df = df[df['mail'].str[0].str.isalpha() & df['mail'].str.contains('@leetcode.com')]  #contains will only search the string
    # Filter the dataframe to include only rows where the 'mail' column matches the specified regex pattern
    # df = df[df['mail'].str.match(r'^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$')]
    # return df

    #PROCESS 2   350 ms , beats 72.64%

    return users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$')]
    
