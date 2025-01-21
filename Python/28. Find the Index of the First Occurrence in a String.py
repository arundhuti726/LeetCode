# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: haystack = "sadbutsad", needle = "sad"
# MAGIC Output: 0
# MAGIC Explanation: "sad" occurs at index 0 and 6.
# MAGIC The first occurrence is at index 0, so we return 0.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: haystack = "leetcode", needle = "leeto"
# MAGIC Output: -1
# MAGIC Explanation: "leeto" did not occur in "leetcode", so we return -1.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
#Solution 1 : Memory 12.54 MB beats 20.46%, Runtime 3ms beats 12,62%
        # if haystack.__contains__(needle):
        #     return haystack.index(needle)
        # else:
        #     return -1


#Solution 2  runtime 0 ms, beat 100%
        if not needle:  # If needle is an empty string
            return 0  # Return 0 as per the problem statement
        
        for i in range(len(haystack) - len(needle) + 1):  # Loop through the haystack until the remaining substring is shorter than needle
            if haystack[i:i+len(needle)] == needle:  # Check if the substring of haystack matches needle
                return i  # Return the starting index of the match
        return -1  # Return -1 if no match is found
