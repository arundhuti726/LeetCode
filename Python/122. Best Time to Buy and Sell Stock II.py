# Databricks notebook source
# MAGIC %md
# MAGIC <h3>ROBLEM DESCRIPTION  </h3>
# MAGIC You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# MAGIC
# MAGIC On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# MAGIC
# MAGIC Find and return the maximum profit you can achieve.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: prices = [7,1,5,3,6,4]
# MAGIC Output: 7
# MAGIC Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# MAGIC Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# MAGIC Total profit is 4 + 3 = 7.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: prices = [1,2,3,4,5]
# MAGIC Output: 4
# MAGIC Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# MAGIC Total profit is 4.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: prices = [7,6,4,3,1]
# MAGIC Output: 0
# MAGIC Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> 

# COMMAND ----------

class Solution:
    def maxProfit(self, prices):
        # if not prices:
        #     return 0  # Return 0 if prices list is empty

        profit = 0  # Initialize profit
        for i in range(len(prices) - 1):
            s = prices[i+1] - prices[i]  # Calculate the difference between consecutive days
            if s > 0:                    # If the difference is positive
                profit += s              # Add the difference to profit
        

        return profit
    
        

