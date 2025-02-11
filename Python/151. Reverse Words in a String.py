# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given an input string s, reverse the order of the words.
# MAGIC
# MAGIC A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# MAGIC
# MAGIC Return a string of the words in reverse order concatenated by a single space.
# MAGIC
# MAGIC Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: s = "the sky is blue"
# MAGIC Output: "blue is sky the"
# MAGIC Example 2:
# MAGIC
# MAGIC Input: s = "  hello world  "
# MAGIC Output: "world hello"
# MAGIC Explanation: Your reversed string should not contain leading or trailing spaces.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: s = "a good   example"
# MAGIC Output: "example good a"
# MAGIC Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> O(n)

# COMMAND ----------

class Solution:
    def reverseWords(self, s: str) -> str:
       
        clean_s =" ".join(s.split())                             # Remove extra whitespace
        i = 0
      
        cnt_spc = clean_s.count(" ")                             # count space
        ary = s.split()                                          # Split the string   o/p: ['the', 'sky', 'is', 'blue']
       
        while i <=cnt_spc:                                       # Loop until the two pointers meet
          
            ary[i] , ary[cnt_spc] = ary[cnt_spc] , ary[i]        # Swap the words
            i+=1                                                 # Move the start pointer to the right
            cnt_spc=cnt_spc-1                                    # Move the end pointer to the left

        return ' '.join(ary)                                     # Convert the list back to a string and return it
        
