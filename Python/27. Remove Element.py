# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# MAGIC
# MAGIC Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# MAGIC
# MAGIC Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# MAGIC Return k.
# MAGIC Custom Judge:
# MAGIC
# MAGIC The judge will test your solution with the following code:
# MAGIC
# MAGIC int[] nums = [...]; // Input array
# MAGIC int val = ...; // Value to remove
# MAGIC int[] expectedNums = [...]; // The expected answer with correct length.
# MAGIC                             // It is sorted with no values equaling val.
# MAGIC
# MAGIC int k = removeElement(nums, val); // Calls your implementation
# MAGIC
# MAGIC assert k == expectedNums.length;
# MAGIC sort(nums, 0, k); // Sort the first k elements of nums
# MAGIC for (int i = 0; i < actualLength; i++) {
# MAGIC     assert nums[i] == expectedNums[i];
# MAGIC }
# MAGIC If all assertions pass, then your solution will be accepted.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [3,2,2,3], val = 3
# MAGIC Output: 2, nums = [2,2,_,_]
# MAGIC Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# MAGIC It does not matter what you leave beyond the returned k (hence they are underscores).
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [0,1,2,2,3,0,4,2], val = 2
# MAGIC Output: 5, nums = [0,1,4,0,3,_,_,_]
# MAGIC Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# MAGIC Note that the five elements can be returned in any order.
# MAGIC It does not matter what you leave beyond the returned k (hence they are underscores).

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        self.nums = nums  # Store the list in the instance variable
        self.val = val  # Store the value to be removed in the instance variable
        
        i = 0  # Initialize the index to 0
        while i < len(nums):  # Loop through the list
            if nums[i] == val:  # Check if the current element is equal to the value to be removed
                nums.pop(i)  # Remove the element if it matches the value
            else:
                i += 1  # Move to the next element if it does not match the value
        return len(nums)  # Return the length of the modified list

c = Solution()  # Create an instance of the Solution class
c.removeElement([0,1,2,2,3,0,4,2], 2)  # Call the removeElement method with the list and value to be removed
