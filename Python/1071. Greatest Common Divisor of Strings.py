# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# MAGIC
# MAGIC Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: str1 = "ABCABC", str2 = "ABC"
# MAGIC Output: "ABC"
# MAGIC Example 2:
# MAGIC
# MAGIC Input: str1 = "ABABAB", str2 = "ABAB"
# MAGIC Output: "AB"
# MAGIC Example 3:
# MAGIC
# MAGIC Input: str1 = "LEET", str2 = "CODE"
# MAGIC Output: ""

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> O(Log(Min(N,M)))
# MAGIC

# COMMAND ----------

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def gcd(a, b):
            while b:
                a, b = b, a % b   # Compute the greatest common divisor using the Euclidean algorithm
            return a
        
        if str1 + str2 != str2 + str1:  # Check if concatenation of str1 and str2 in both orders is the same
            return ""
        
        gcd_length = gcd(len(str1), len(str2))  # Find the gcd of the lengths of str1 and str2
        return str1[:gcd_length]  # Return the substring of str1 from the start to the gcd length

        
