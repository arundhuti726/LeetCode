# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
# MAGIC
# MAGIC A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 34 ms
# MAGIC <h3> Beats: </h3> 50.52
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------



import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        
        def combine_array(gr):
            combined = []
            for i in gr:
                row = ''.join(map(str, i))
                combined.append(row)
            return combined

        transpose_array = np.array(grid)
        grid2 = transpose_array.T

        row1, row2 = combine_array(grid), combine_array(grid2)
        print('1:',row1)
        print('2:',row2)

        result,c = [],0
        for r1 in row1:
            for r2 in row2:
                result.append((r1, r2))
                print('r1=',r1,'r2=',r2)
                if r1 == r2:
                    c += 1
                    print('c=',c)
                   # break
                # else:
                #     continue

        return c


       
        # n = len(grid)
        # hash = {}
        # pairs = 0
        
        # for i in range(n):
        #     row = tuple(grid[i])
        #     hash[row] = hash.get(row, 0) + 1
                
        # for j in range(n):
        #     column = tuple(grid[i][j] for i in range(n))
        #     if column in hash:
        #         pairs += hash[column]
        
        # return pairs        

        
        # n = len(grid)  # Get the size of the grid (number of rows/columns)
        # hash = {}  # Initialize an empty dictionary to store row counts
        # pairs = 0  # Initialize the count of equal pairs to 0
        
        # for i in range(n):  # Iterate through each row in the grid
        #     row = tuple(grid[i])  # Convert the row to a tuple (to use as a dictionary key)
        #     print(f"Row {i}: {row}")
        #     hash[row] = hash.get(row, 0) + 1  # Increment the count of this row in the dictionary
        #     print(f"Row {i}: {row}, Count: {hash[row]}")  # Print the row and its count in the dictionary
                
        # for j in range(n):  # Iterate through each column in the grid
        #     column = tuple(grid[i][j] for i in range(n))  # Convert the column to a tuple
        #     print(f"Column {j}: {column}")
        #     if column in hash:  # Check if this column matches any row in the dictionary
        #         pairs += hash[column]  # Add the count of matching rows to the pairs count
        #     print(f"Column {j}: {column}, Pairs: {pairs}")  # Print the column and the current pairs count
        
        # print(f"Total pairs: {pairs}")  # Print the total count of equal row-column pairs

        # return pairs
