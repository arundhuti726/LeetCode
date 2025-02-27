# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# MAGIC
# MAGIC Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# MAGIC
# MAGIC  
# MAGIC Example 1:
# MAGIC
# MAGIC Input: s = "abciiidef", k = 3
# MAGIC Output: 3
# MAGIC Explanation: The substring "iii" contains 3 vowel letters.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: s = "aeiou", k = 2
# MAGIC Output: 2
# MAGIC Explanation: Any substring of length 2 contains 2 vowels.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: s = "leetcode", k = 3
# MAGIC Output: 2
# MAGIC Explanation: "lee", "eet" and "ode" contain 2 vowels.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 86 ms
# MAGIC <h3> Beats: </h3> 51.67%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

## Accepted Solution

class Solution:  # Define a class named Solution
    def maxVowels(self, s: str, k: int) -> int:  # Define a method maxVowels that takes a string s and an integer k as input and returns an integer
        vowels = set('aeiouAEIOU')  # Create a set containing all vowels
        s, sub = list(s), s[0:k]  # Convert the input string to a list and get the substring of length k
        mx = i = l = 0  # Initialize variables mx, i, and l to 0

        while i < k:  # Start a while loop iterating over the first k elements of the string
            if s[i] in vowels:  # Check if the current character is a vowel
                mx += 1  # Increment the count of vowels
            i += 1  # Move to the next character

        temp = mx  # Assign the count of vowels to a temporary variable
        while i < len(s):  # Start a while loop iterating over the remaining elements of the string
            if s[i] in vowels:  # Check if the current character is a vowel
                temp += 1  # Increment the count of vowels
            if s[i - k] in vowels:  # Check if the character k positions before the current character is a vowel
                temp -= 1  # Decrement the count of vowels
            mx = max(mx, temp)  # Update the maximum count of vowels
            i += 1  # Move to the next character

        return mx  # Return the maximum count of vowels within any substring of length k

c = Solution()  # Create an instance of the Solution class
c.maxVowels("abciiidef", 3)  # Call the maxVowels method with the input string "abciiidef" and substring length 3

# COMMAND ----------

## My solition 1, throw timed out error due to a really big array

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiouAEIOU')              
        s,sub = list(s), s[0:k]                              
        mx=i=l = 0
        

        while i <= len(s) - k:
            c = 0
            l, j = i, i + k

            while l < j:
                if s[l] in vowels:
                    c += 1
                l += 1
            mx = max(mx, c)
            i += 1
        return mx

        
