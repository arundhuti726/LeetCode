# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
# MAGIC
# MAGIC You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: gain = [-5,1,5,0,-7]
# MAGIC Output: 1
# MAGIC Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: gain = [-4,-3,-2,-1,4,3,2]
# MAGIC Output: 0
# MAGIC Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> O(n)
# MAGIC

# COMMAND ----------

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}  # Initialize an empty dictionary to store the count of each element
        for element in arr:  # Iterate through each element in the input list
            counts[element] = counts.get(element, 0) + 1  # Increment the count for the element
        
        val_size = len(list(counts.values()))  # Get the number of unique counts
        uni_val_size = len(set(list(counts.values())))  # Get the number of unique counts using a set to remove duplicates

        if val_size == uni_val_size:  # Compare the sizes to check if all counts are unique
            return True  # Return True if all counts are unique
        else:
            return False  # Return False if there are duplicate counts

# COMMAND ----------


