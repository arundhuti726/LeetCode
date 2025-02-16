# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# MAGIC
# MAGIC Note that you must do this in-place without making a copy of the array.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [0,1,0,3,12]
# MAGIC Output: [1,3,12,0,0]
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [0]
# MAGIC Output: [0]
# MAGIC
# MAGIC Input: nums = [0,0,1]
# MAGIC Output: [1,0,0]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 21 ms
# MAGIC <h3> Beats: </h3> 16.10%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

 # My process 2
 class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        import numpy as np
        i,l = 0,len(nums)
       
        while i!=l:
            if nums[i]==0:
                nums.insert(l,nums.pop(i))
                l-=1
            else:
                i+=1
                

# COMMAND ----------

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # process 1
        # i,j = 0,0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[i],nums[j] = nums[j], nums[i]
        #         j+=1
