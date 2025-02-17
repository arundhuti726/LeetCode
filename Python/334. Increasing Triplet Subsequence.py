# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [1,2,3,4,5]
# MAGIC Output: true
# MAGIC Explanation: Any triplet where i < j < k is valid.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [5,4,3,2,1]
# MAGIC Output: false
# MAGIC Explanation: No triplet exists.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: nums = [2,1,5,0,4,6]
# MAGIC Output: true
# MAGIC Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 12 ms
# MAGIC <h3> Beats: </h3> 84.72%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:  # Define a method to check for increasing triplet
        if len(nums) < 3:  # Check if the length of nums is less than 3
            return False  # Return False if there are not enough elements
        
        first = second = float('inf')  # Initialize first and second to infinity
        for n in nums:  # Iterate through each number in nums
            if n <= first:  # Check if the current number is less than or equal to first
                first = n  # Update first to the current number
               # print('first',first)  # Print the value of first for debugging
            elif n <= second:  # Check if the current number is less than or equal to second
                second = n  # Update second to the current number
                #print('second',second)  # Print the value of second for debugging
            else:  # If the current number is greater than both first and second
                return True  # Return True indicating an increasing triplet is found
        return False  # Return False if no increasing triplet is found
