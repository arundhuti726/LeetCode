# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC In the world of Dota2, there are two parties: the Radiant and the Dire.
# MAGIC
# MAGIC The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
# MAGIC
# MAGIC Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# MAGIC Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# MAGIC Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.
# MAGIC
# MAGIC The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
# MAGIC
# MAGIC Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 12 ms
# MAGIC <h3> Beats: </h3> 56.80%
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

## PROCESS 1
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        i,j,voters = 0,1,deque(senate) 
        voters = deque(senate)
        radiant = deque()
        dire = deque()

        for i, voter in enumerate(voters):
            if voter == 'R':
                radiant.append(i)
                print(f"Radiant voter at index {i} added to radiant queue: {radiant}")  # Comment: Add Radiant voter to queue
            else:
                dire.append(i)
                print(f"Dire voter at index {i} added to dire queue: {dire}")  # Comment: Add Dire voter to queue

        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()
            print(f"Radiant voter at index {r_index} and Dire voter at index {d_index} dequeued")  # Comment: Dequeue voters
            if r_index < d_index:
                radiant.append(r_index + len(voters))
                print(f"Radiant voter at index {r_index} wins and re-added to queue: {radiant}")  # Comment: Radiant wins
            else:
                dire.append(d_index + len(voters))
                print(f"Dire voter at index {d_index} wins and re-added to queue: {dire}")  # Comment: Dire wins

        if radiant:
            return "Radiant"  # Comment: Radiant wins overall
        else:
            return "Dire"  # Comment: Dire wins overall

                

# COMMAND ----------

###    PROCESS 2 

        # Initialize the deque with the given voters
        voters = deque(senate) 

        # Create deques for Radiant and Dire senators with their respective indices
        radiant = deque(i for i, v in enumerate(voters) if v == 'R')  # Provide the R's index
        dire = deque(i for i, v in enumerate(voters) if v == 'D') # Provide the  D's index
        print('radiant=',radiant)  
        print('dire=',dire)

        # Continue the process until one of the queues is empty
        while radiant and dire:
            r_index = radiant.popleft()   # Get the index of the first Radiant senator
            d_index = dire.popleft()      # Get the index of the first Dire senator
            if r_index < d_index:         # If Radiant senator's index is less than Dire senator's index
                radiant.append(r_index + len(voters))   # Radiant senator bans Dire senator and gets a new index
            else:                  # If Dire senator's index is less than or equal to Radiant senator's index
                dire.append(d_index + len(voters))   # Dire senator bans Radiant senator and gets a new index

        # Return the winning team
        return "Radiant" if radiant else "Dire"
