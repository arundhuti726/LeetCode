# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# MAGIC
# MAGIC answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# MAGIC answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# MAGIC Note that the integers in the lists may be returned in any order.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums1 = [1,2,3], nums2 = [2,4,6]
# MAGIC Output: [[1,3],[4,6]]
# MAGIC Explanation:
# MAGIC For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# MAGIC For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# MAGIC Output: [[3],[]]
# MAGIC Explanation:
# MAGIC For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# MAGIC Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 160 ms
# MAGIC <h3> Beats: </h3> 20.56%
# MAGIC <h3> Complexity: </h3> 
# MAGIC

# COMMAND ----------

# PROCESS 1
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1,nums2 = list(set(nums1)),list(set(nums2))
        

        def func(nums1, nums2):
            return [n for n in nums1 if n not in nums2]
            
       
        return [func(nums1,nums2), func(nums2,nums1)]

# COMMAND ----------

###PROCESS 2
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        def func(nums1, nums2):
            ar = []
            for n in nums1:
                if n not in nums2:
                    ar.append(n)
            return ar

        a1 = func(nums1, nums2)
        a2 = func(nums2, nums1)
        
    return [list(set(a1)), list(set(a2))]
