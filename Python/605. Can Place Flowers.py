# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# MAGIC
# MAGIC Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: flowerbed = [1,0,0,0,1], n = 1
# MAGIC Output: true
# MAGIC Example 2:
# MAGIC
# MAGIC Input: flowerbed = [1,0,0,0,1], n = 2
# MAGIC Output: false

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 11 ms
# MAGIC <h3> Beats: </h3> 39.20%
# MAGIC <h3> Complexity: </h3> 
# MAGIC ## MY FIRST SUBMISSION

# COMMAND ----------

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, c = 0, 0  # Initialize index i and count c to 0
        
        def countZeros(array):
            nonlocal i, c  # Use nonlocal to modify i and c defined in the outer function
            while i < len(array):  # Iterate through the array
                if array[i] == 0:  # Check if the current position is 0
                    if (i == 0 or array[i - 1] == 0) and (i == len(array) - 1 or array[i + 1] == 0):  # Check if adjacent positions are 0 or boundaries
                        c += 1  # Increment count if a flower can be placed
                        i += 1  # Skip the next position
                i += 1  # Move to the next position
            return c  # Return the count of possible flower placements
        
        countZeros(flowerbed)  # Call the helper function to count possible placements
        return c >= n  # Return True if the count is greater than or equal to n
