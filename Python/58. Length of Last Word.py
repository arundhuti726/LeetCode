# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given a string s consisting of words and spaces, return the length of the last word in the string.
# MAGIC
# MAGIC A word is a maximal 
# MAGIC substring
# MAGIC  consisting of non-space characters only.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: s = "Hello World"
# MAGIC Output: 5
# MAGIC Explanation: The last word is "World" with length 5.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: s = "   fly me   to   the moon  "
# MAGIC Output: 4
# MAGIC Explanation: The last word is "moon" with length 4.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: s = "luffy is still joyboy"
# MAGIC Output: 6
# MAGIC Explanation: The last word is "joyboy" with length 6.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        string = s.strip()   # Remove leading and trailing whitespace
        
        for i in range(len(string)):
            if string[i]==" ":
                l=0         # Reset length counter when a space is encountered
            else:
                l+=1        # Increment length counter for each non-space character
        
        return l

c = Solution()
c.lengthOfLastWord("Hello World")

            
