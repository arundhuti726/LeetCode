# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# MAGIC
# MAGIC Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# MAGIC
# MAGIC Note that multiple kids can have the greatest number of candies.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: candies = [2,3,5,1,3], extraCandies = 3
# MAGIC Output: [true,true,true,false,true] 
# MAGIC Explanation: If you give all extraCandies to:
# MAGIC - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# MAGIC - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# MAGIC - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# MAGIC - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# MAGIC - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: candies = [4,2,1,1,2], extraCandies = 1
# MAGIC Output: [true,false,false,false,false] 
# MAGIC Explanation: There is only 1 extra candy.
# MAGIC Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: candies = [12,1,12], extraCandies = 10
# MAGIC Output: [true,false,true]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> O(N)
# MAGIC

# COMMAND ----------

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        mx = max(candies)

        return list(map(lambda i:i+extraCandies>=mx,candies ))

# COMMAND ----------

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        mx = max(candies)

        array_next = list(map(lambda i: i+extraCandies, candies))
              
        result = list(map(lambda i:i>=mx,array_next ))
        return result
        
