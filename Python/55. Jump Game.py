# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# MAGIC
# MAGIC Return true if you can reach the last index, or false otherwise.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [2,3,1,1,4]
# MAGIC Output: true
# MAGIC Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [3,2,1,0,4]
# MAGIC Output: false
# MAGIC Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 32 ms
# MAGIC <h3> Beats: </h3> 45.46%
# MAGIC <h3> Complexity: </h3> O(N)
# MAGIC

# COMMAND ----------

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i, num in enumerate(nums):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + num) #Jump till the 'max_jump' and then start the analysis again.
            
        return True

                
