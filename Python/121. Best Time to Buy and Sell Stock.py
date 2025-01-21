# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC You are given an array prices where prices[i] is the price of a given stock on the ith day.
# MAGIC
# MAGIC You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# MAGIC
# MAGIC Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: prices = [7,1,5,3,6,4]
# MAGIC Output: 5
# MAGIC Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# MAGIC Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: prices = [7,6,4,3,1]
# MAGIC Output: 0
# MAGIC Explanation: In this case, no transactions are done and the max profit = 0.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 31 ms
# MAGIC <h3> Beats: </h3> 92.41
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0  # Return 0 if prices list is empty
        
        min_price = float('inf')  # Initialize min_price to infinity
        max_profit = 0  # Initialize max_profit to 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price if current price is lower
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max_profit if current profit is higher
        
        return max_profit  # Return the maximum profit found
