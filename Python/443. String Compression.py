# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given an array of characters chars, compress it using the following algorithm:
# MAGIC
# MAGIC Begin with an empty string s. For each group of consecutive repeating characters in chars:
# MAGIC
# MAGIC If the group's length is 1, append the character to s.
# MAGIC Otherwise, append the character followed by the group's length.
# MAGIC The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# MAGIC
# MAGIC After you are done modifying the input array, return the new length of the array.
# MAGIC
# MAGIC You must write an algorithm that uses only constant extra space.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: chars = ["a","a","b","b","c","c","c"]
# MAGIC Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# MAGIC Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# MAGIC Example 2:
# MAGIC
# MAGIC Input: chars = ["a"]
# MAGIC Output: Return 1, and the first character of the input array should be: ["a"]
# MAGIC Explanation: The only group is "a", which remains uncompressed since it's a single character.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# MAGIC Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# MAGIC Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> O(n)
# MAGIC

# COMMAND ----------

class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0  # Initialize pointers i and j to 0
        while i < len(chars):  # Loop until i reaches the end of chars
            char = chars[i]  # Store the current character
            count = 0  # Initialize count for the current character
            while i < len(chars) and chars[i] == char:  # Count occurrences of the current character
                i += 1  # Move to the next character
                count += 1  # Increment the count
            chars[j] = char  # Place the character at the j-th position
            j += 1  # Move to the next position in the compressed list
            if count > 1:  # If the character count is more than 1
                for n in str(count):  # Convert count to string and iterate over each digit
                    chars[j] = n  # Place each digit in the compressed list
                    j += 1  # Move to the next position in the compressed list
        return j  # Return the length of the compressed list
