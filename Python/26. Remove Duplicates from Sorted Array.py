# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# MAGIC
# MAGIC Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# MAGIC
# MAGIC Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# MAGIC Return k.
# MAGIC Custom Judge:
# MAGIC
# MAGIC The judge will test your solution with the following code:
# MAGIC
# MAGIC int[] nums = [...]; // Input array
# MAGIC int[] expectedNums = [...]; // The expected answer with correct length
# MAGIC
# MAGIC int k = removeDuplicates(nums); // Calls your implementation
# MAGIC
# MAGIC assert k == expectedNums.length;
# MAGIC for (int i = 0; i < k; i++) {
# MAGIC     assert nums[i] == expectedNums[i];
# MAGIC }
# MAGIC If all assertions pass, then your solution will be accepted.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 6 ms
# MAGIC <h3> Beats: </h3> 33.29
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1
    
