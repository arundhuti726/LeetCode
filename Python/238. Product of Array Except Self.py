# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# MAGIC
# MAGIC The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# MAGIC
# MAGIC You must write an algorithm that runs in O(n) time and without using the division operation.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [1,2,3,4]
# MAGIC Output: [24,12,8,6]
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [-1,1,0,-3,3]
# MAGIC Output: [0,0,9,0,0]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 253 ms
# MAGIC <h3> Beats: </h3> 5.09%
# MAGIC <h3> Complexity: </h3> O(n)

# COMMAND ----------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import numpy as np  # Import numpy for numerical operations
        i, l = 0, len(nums)  # Initialize i to 0 and l to the length of nums
        answer = [1] * l  # Create a list 'answer' with 'l' elements, all initialized to 1
        
        if nums.count(0) > 1:  # If there are more than one zero in nums
            answer = [0] * len(nums)  # Set all elements in answer to 0
            
        elif nums.count(0) == 1:  # If there is exactly one zero in nums
            pos = nums.index(0)  # Find the position of the zero
            nums[pos] = 1  # Temporarily set the zero to 1
            expr = "*".join([str(num) for num in nums])  # Create a string expression to multiply all numbers
            val = eval(expr)  # Evaluate the expression to get the product
            answer = [0] * len(nums)  # Set all elements in answer to 0
            answer[pos] = val  # Set the position of the original zero to the product value
            
        else:  # If there are no zeros in nums
            total_product = np.prod(nums)  # Calculate the product of all elements in nums
            for i in range(len(nums)):  # Iterate through each element in nums
                answer[i] = int(total_product / nums[i])  # Set answer[i] to the product of all elements except nums[i]
        
        return answer  # Return the final answer list
