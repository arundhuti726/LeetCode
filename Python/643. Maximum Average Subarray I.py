# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC You are given an integer array nums consisting of n elements, and an integer k.
# MAGIC
# MAGIC Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [1,12,-5,-6,50,3], k = 4
# MAGIC Output: 12.75000
# MAGIC Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [5], k = 1
# MAGIC Output: 5.00000
# MAGIC  

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        list_sum = sum(nums[:k]) # Calculate the sum of the first 'k' elements
        crnt_sum = list_sum  # Initialize the current sum with the max sum

        for i in range(k, len(nums)):  # Iterate over the list starting from index 'k'
            crnt_sum += nums[i] - nums[i - k]  # Update the current sum by adding the new element and removing the oldest
            list_sum = max(list_sum, crnt_sum)  # Update the max sum if the current s

        max_avg = list_sum / k  # Calculate the maximum average by dividing the max sum by 'k'

        return max_avg
