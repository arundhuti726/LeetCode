# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [1,2,3,4,5,6,7], k = 3
# MAGIC Output: [5,6,7,1,2,3,4]
# MAGIC Explanation:
# MAGIC rotate 1 steps to the right: [7,1,2,3,4,5,6]
# MAGIC rotate 2 steps to the right: [6,7,1,2,3,4,5]
# MAGIC rotate 3 steps to the right: [5,6,7,1,2,3,4]
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [-1,-100,3,99], k = 2
# MAGIC Output: [3,99,-1,-100]
# MAGIC Explanation: 
# MAGIC rotate 1 steps to the right: [99,-1,-100,3]
# MAGIC rotate 2 steps to the right: [3,99,-1,-100]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 1224 ms
# MAGIC <h3> Beats: </h3> 5.10%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        import numpy as np  # Import numpy library

        l = len(nums)  # Get the length of the list
        if k > 0:  # Check if k is greater than 0
            for i in range(k):  # Loop k times
                nums.insert(0, nums.pop())  # pop() the last element and push into the 0th location
