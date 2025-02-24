# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given an array of integers nums, calculate the pivot index of this array.
# MAGIC
# MAGIC The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# MAGIC
# MAGIC If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# MAGIC
# MAGIC Return the leftmost pivot index. If no such index exists, return -1.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [1,7,3,6,5,6]
# MAGIC Output: 3
# MAGIC Explanation:
# MAGIC The pivot index is 3.
# MAGIC Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# MAGIC Right sum = nums[4] + nums[5] = 5 + 6 = 11
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [1,2,3]
# MAGIC Output: -1
# MAGIC Explanation:
# MAGIC There is no index that satisfies the conditions in the problem statement.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: nums = [2,1,-1]
# MAGIC Output: 0
# MAGIC Explanation:
# MAGIC The pivot index is 0.
# MAGIC Left sum = 0 (no elements to the left of index 0)
# MAGIC Right sum = nums[1] + nums[2] = 1 + -1 = 0

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 19 ms
# MAGIC <h3> Beats: </h3> 19.65%
# MAGIC <h3> Complexity: </h3>  O(n)

# COMMAND ----------

import numpy as np
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_cumSum = np.cumsum(nums)  # Calculate the cumulative sum of the list
        t_sum = sum(nums)  # Calculate the total sum of the list

        for i in range(len(nums)):  # Iterate through the list
            print('l_cumSum =', l_cumSum[i], 'nums=', nums[i], 't_sum=', t_sum, '\t i=', i)  # Debug print statement
            if l_cumSum[i] - nums[i] == t_sum - l_cumSum[i]:  # Check if the pivot index condition is met
                print('l_cumSum[i] - nums[i] == t_sum - l_cumSum[i] ->', l_cumSum[i] - nums[i], t_sum - l_cumSum[i])  # Debug print statement
                return i  # Return the pivot index if condition is met
        return -1  # Return -1 if no pivot index is found

nums = [1, 7, 3, 6, 5, 6]
result = Solution().pivotIndex(nums)
display(result)
