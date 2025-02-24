# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC You are given a string s, which contains stars *.
# MAGIC
# MAGIC In one operation, you can:
# MAGIC
# MAGIC Choose a star in s.
# MAGIC Remove the closest non-star character to its left, as well as remove the star itself.
# MAGIC Return the string after all stars have been removed.
# MAGIC
# MAGIC Note:
# MAGIC
# MAGIC The input will be generated such that the operation is always possible.
# MAGIC It can be shown that the resulting string will always be unique.
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: s = "leet**cod*e"
# MAGIC Output: "lecoe"
# MAGIC Explanation: Performing the removals from left to right:
# MAGIC - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# MAGIC - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# MAGIC - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# MAGIC There are no more stars, so we return "lecoe".
# MAGIC Example 2:
# MAGIC
# MAGIC Input: s = "erase*****"
# MAGIC Output: ""
# MAGIC Explanation: The entire string is removed, so we return an empty string.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 146 ms
# MAGIC <h3> Beats: </h3> 29.32%
# MAGIC <h3> Complexity: </h3> 
# MAGIC ## MY FIRST SUBMISSION

# COMMAND ----------

class Solution:
    def removeStars(self, s: str) -> str:
      
    
        res=[]  # Initialize an empty list to store the result
        if s[0]=='*':  # Check if the first character in the string is '*'
            s = lstrip(s,'*')  # Remove leading '*' characters from the string
        else:  # If the first character is not '*'
            for i in s:  # Iterate through each character in the string
                if i=='*':  # If the current character is '*'
                    res.pop()  # Remove the last character from the result list
                else:  # If the current character is not '*'
                    res+=[i]  # Add the current character to the result list
        return "".join(res)  # Join the characters in the result list into a single string and return it


        ##########
        # The expression res+=[i] appends the element i to the list res.
        # The expression res+=s[i] would attempt to append the element at index i of the list s to res.
        # Here is an example to illustrate the difference:
