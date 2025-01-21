# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given an array nums of size n, return the majority element.
# MAGIC
# MAGIC The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [3,2,3]
# MAGIC Output: 3
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [2,2,1,1,1,2,2]
# MAGIC Output: 2

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = 0

        for num in nums:
            if count == 0:
                n = num  # Set the current candidate to the current number
            count += (1 if num == n else -1)  # Increment or decrement the count

        return n  # Return the majority element
