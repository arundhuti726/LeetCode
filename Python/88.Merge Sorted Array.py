# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given a string s consisting of words and spaces, return the length of the last word in the string.
# MAGIC
# MAGIC A word is a maximal 
# MAGIC substring
# MAGIC  consisting of non-space characters only.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: s = "Hello World"
# MAGIC Output: 5
# MAGIC Explanation: The last word is "World" with length 5.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: s = "   fly me   to   the moon  "
# MAGIC Output: 4
# MAGIC Explanation: The last word is "moon" with length 4.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: s = "luffy is still joyboy"
# MAGIC Output: 6
# MAGIC Explanation: The last word is "joyboy" with length 6.
# MAGIC You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# MAGIC
# MAGIC Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# MAGIC
# MAGIC The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# MAGIC Output: [1,2,2,3,5,6]
# MAGIC Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# MAGIC The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums1 = [1], m = 1, nums2 = [], n = 0
# MAGIC Output: [1]
# MAGIC Explanation: The arrays we are merging are [1] and [].
# MAGIC The result of the merge is [1].
# MAGIC Example 3:
# MAGIC
# MAGIC Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# MAGIC Output: [1]
# MAGIC Explanation: The arrays we are merging are [] and [1].
# MAGIC The result of the merge is [1].
# MAGIC Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 3 ms
# MAGIC <h3> Beats: </h3> 14.36%
# MAGIC <h3> Complexity: </h3> 
# MAGIC ## MY FIRST SUBMISSION

# COMMAND ----------

# 88 merge Sorted array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # Replace the elements in nums1 from index m onwards with the first n elements of nums2
        nums1[m:] = nums2[:n]
        # Sort nums1 in-place
        nums1.sort()
        # Print the modified nums1 array
        print(nums1)
