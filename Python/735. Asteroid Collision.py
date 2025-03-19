# Databricks notebook source
# MAGIC %md
# MAGIC <h3> ROBLEM DESCRIPTION </h3>
# MAGIC We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
# MAGIC
# MAGIC For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# MAGIC
# MAGIC Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: asteroids = [5,10,-5]
# MAGIC Output: [5,10]
# MAGIC Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# MAGIC Example 2:
# MAGIC
# MAGIC Input: asteroids = [8,-8]
# MAGIC Output: []
# MAGIC Explanation: The 8 and -8 collide exploding each other.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: asteroids = [10,2,-5]
# MAGIC Output: [10]
# MAGIC Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 7 ms
# MAGIC <h3> Beats: </h3> 59.18%
# MAGIC <h3> Complexity: </h3> O(n)
# MAGIC

# COMMAND ----------

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         res = []  
#         for asteroid in asteroids:  
            
#             while res and asteroid < 0 < res[-1]: 
                
#                 if res[-1] < -asteroid: 
#                     res.pop()  
#                     continue  
#                 elif res[-1] == -asteroid:  
#                     res.pop() 
#                 break  
#             else:  
#                 res.append(asteroid)  
                       
#         return res 



# COMMAND ----------

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []  # Initialize an empty list to store the result
        c = 0  
        for asteroid in asteroids:  # Iterate through each asteroid in the input list
            c = c + 1  
            print('count=', c, 'asteroid =', asteroid, 'res =', res)  
            while res and asteroid < 0 < res[-1]:  # Check if there is a collision
                print('inside While:: res =', res, 'asteroid =', asteroid, 'res[-1]=', res[-1])  
                
                if res[-1] < -asteroid:  # If the last asteroid in the result list is smaller than the current asteroid
                    res.pop()  # Remove the last asteroid from the result list
                    continue  # Continue to the next iteration of the while loop
                elif res[-1] == -asteroid:  # If the last asteroid in the result list is equal to the current asteroid
                    print('inside elif:: res =', res, 'asteroid =', asteroid, 'res[-1]=', res[-1])  
                    res.pop()  # Remove the last asteroid from the result list
                break  # Break out of the while loop
            else:  # If no collision occurs
                res.append(asteroid)  # Add the current asteroid to the result list
                print('res =', res)  
        
        return res  # Return the final result list
