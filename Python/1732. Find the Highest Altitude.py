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
    def largestAltitude(self, gain: List[int]) -> int:
        i, k, v = 0, len(gain) + 1, 0  # Initialize i to 0, k to length of gain + 1, and v to 0
        
        result = [0] * k  # Create a list of zeros with length k

        while i < len(gain):  # Loop through each element in gain
            v = v + gain[i]  # Update v by adding the current gain value
            i, result[i] = i + 1, v  # Increment i and update result at index i with v
            
        return max(result)  # Return the maximum value in result
