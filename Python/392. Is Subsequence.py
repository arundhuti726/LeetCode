# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# MAGIC
# MAGIC A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: s = "abc", t = "ahbgdc"
# MAGIC Output: true
# MAGIC Example 2:
# MAGIC
# MAGIC Input: s = "axc", t = "ahbgdc"
# MAGIC Output: false
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> O(n)
# MAGIC ## MY FIRST SUBMISSION

# COMMAND ----------

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0  # Initialize pointers for both strings
        while i < len(s) and j < len(t):  # Loop until we reach the end of either string
            if s[i] == t[j]:  # If characters match, move the pointer for s
                i += 1
            j += 1  # Always move the pointer for t
        # Return True if all characters of s are found in t in order, otherwise return False
        return i == len(s)
