# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# MAGIC
# MAGIC Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# MAGIC
# MAGIC Return k after placing the final result in the first k slots of nums.
# MAGIC
# MAGIC Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
# MAGIC
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
# MAGIC ### Run Time: </h3> 76 ms
# MAGIC <h3> Beats: </h3> 5.53%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            # Count the total number of duplicates.          
            if nums.count(nums[i]) > 2:
                # if count is more than 2 then delete that value
                nums.pop(i)
            else:
                #Otherwise, move to the next element of the array
                i += 1


        return len(nums)
