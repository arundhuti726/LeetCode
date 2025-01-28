# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# MAGIC
# MAGIC Return the merged string.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: word1 = "abc", word2 = "pqr"
# MAGIC Output: "apbqcr"
# MAGIC Explanation: The merged string will be merged as so:
# MAGIC word1:  a   b   c
# MAGIC word2:    p   q   r
# MAGIC merged: a p b q c r
# MAGIC Example 2:
# MAGIC
# MAGIC Input: word1 = "ab", word2 = "pqrs"
# MAGIC Output: "apbqrs"
# MAGIC Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# MAGIC word1:  a   b 
# MAGIC word2:    p   q   r   s
# MAGIC merged: a p b q   r   s
# MAGIC Example 3:
# MAGIC
# MAGIC Input: word1 = "abcd", word2 = "pq"
# MAGIC Output: "apbqcd"
# MAGIC Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# MAGIC word1:  a   b   c   d
# MAGIC word2:    p   q 
# MAGIC merged: a p b q c   d
# MAGIC  

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 38 ms
# MAGIC <h3> Beats: </h3> 36,78%
# MAGIC <h3> Complexity: </h3> 
# MAGIC ## MY FIRST SUBMISSION

# COMMAND ----------

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word = []
        i = 0

        # Loop until the end of the longer word is reached
        while i < len(word1) or i < len(word2):
            if i < len(word1):  # Check if the current index is within the bounds of word1
                word.append(word1[i]) # Append the character from word1 to the merged list
            if i < len(word2): # Check if the current index is within the bounds of word2
                word.append(word2[i]) # Append the character from word2 to the merged list
            i += 1 # Increment the index counter

            final_word = ''.join(word)  # Join the list of characters into a single string
        return final_word
