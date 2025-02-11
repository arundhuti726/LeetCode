# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given a string s, reverse only all the vowels in the string and return it.
# MAGIC The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: s = "IceCreAm"
# MAGIC
# MAGIC Output: "AceCreIm"
# MAGIC
# MAGIC Explanation:
# MAGIC
# MAGIC The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
# MAGIC
# MAGIC Example 2:
# MAGIC
# MAGIC Input: s = "leetcode"
# MAGIC
# MAGIC Output: "leotcede"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 7 ms
# MAGIC <h3> Beats: </h3> 91.46%
# MAGIC <h3> Complexity: </h3> O(N)
# MAGIC

# COMMAND ----------

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')              # Create a set of vowels for quick lookup
        s = list(s)                             # Convert the string to a list to allow modification
        i, j = 0, len(s) - 1                    # Initialize two pointers, one at the start and one at the end

        while i < j:                            # Loop until the two pointers meet
            if s[i] not in vowels:              # If the character at the start pointer is not a vowel
                i += 1                          # Move the start pointer to the right
            elif s[j] not in vowels:            # If the character at the end pointer is not a vowel
                j -= 1                          # Move the end pointer to the left
            else:                               # If both characters are vowels
                s[i], s[j] = s[j], s[i]         # Swap the vowels
                i += 1                          # Move the start pointer to the right
                j -= 1                          # Move the end pointer to the left

        return ''.join(s)                       # Convert the list back to a string and return it
       
