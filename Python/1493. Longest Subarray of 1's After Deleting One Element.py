# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given a binary array nums, you should delete one element from it.
# MAGIC
# MAGIC Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
# MAGIC
# MAGIC  
# MAGIC Example 1:
# MAGIC
# MAGIC Input: nums = [1,1,0,1]
# MAGIC Output: 3
# MAGIC Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: nums = [0,1,1,1,0,1,1,0,1]
# MAGIC Output: 5
# MAGIC Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# MAGIC Example 3:
# MAGIC
# MAGIC Input: nums = [1,1,1]
# MAGIC Output: 2
# MAGIC Explanation: You must delete one element.
# MAGIC  

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> multiple
# MAGIC <h3> Beats: </h3> multiple
# MAGIC <h3> Complexity: </h3> multiple

# COMMAND ----------

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
       

            #    PROCESS 3

            low = zeros = 0
            for high in range(len(nums)):
                if nums[high] == 0:
                    zeros += 1
                if zeros > 1:
                    if nums[low] == 0:
                        zeros -= 1
                    low += 1

            return high - low
            

        

# COMMAND ----------

##   PROCESS 2
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

            # zeros = [i for i, x in enumerate(nums) if x == 0]
            # l,result = len(zeros),0

        

            # if l != 0 and len(nums)-l == 0:
            #     result = 0
            # elif l == 0 and len(nums) != 0:
            #     result = len(nums)-1
            # elif l != 0 and len(nums)-l != 0:
            #     max_len = 0
            #     for z in zeros:
            #         temp_ary = nums[:z] + nums[z+1:]
            #         ones_len = max(len(list(g)) for k, g in itertools.groupby(temp_ary) if k == 1)
            #         if ones_len > max_len:
            #             max_len = ones_len
            #     result = max_len

            # return result


# COMMAND ----------

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #PROCESS 1
        #zeros = [i for i, x in enumerate(nums) if x == 0]
        #ones = [i for i, x in enumerate(nums) if x != 0]

        # print('zeros;',zeros)
        # print('ones;',ones)
        #for i ,x in in enumerate(nums):


        # if x == 0:
        #     return 0
        
        # elif  len(zeros) == 0 and len(ones)!=0 :
        #     return len(ones)-1


        # elif len(zeros) != 0 and len(ones)!=0:
        
        #     max_len = 0
        #     for z in zeros:
        #         # print('max_len=',max_len)
                # Remove the zero at index z and calculate the length of consecutive ones
                # temp_ary = nums[:z] + nums[z+1:]
                # print('ary[:z]=',nums[:z])
                # print('ary[z+1:]',nums[z+1:])
                # print(f'temp_ary: {temp_ary}')
                # Find the maximum length of consecutive ones in temp_ary
                # ones_len = max(len(list(g)) for k, g in itertools.groupby(temp_ary) if k == 1)
                # print(f'ones_len: {ones_len}')
            #     if ones_len > max_len:
            #         max_len = ones_len
            # return max_len

