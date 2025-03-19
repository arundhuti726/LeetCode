# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given the head of a singly linked list, reverse the list, and return the reversed list. 

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> O(N)

# COMMAND ----------

class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val          # Initialize the value of the node
        self.next = next        # Initialize the next pointer of the node
        self.prev = prev        # Initialize the previous pointer of the node

class Solution(object):
    def __init__(self):
        self.head = None       # Initialize the head of the list
        self.tail = None       # Initialize the tail of the list 

    def reverseList(self, head):
        current = head         # Start with the head of the list 
        prev_node = None       # Initialize the previous node as None
        while current:         # Iterate through the list until the end
            next_node = current.next    # Store the next node
            current.next = prev_node    # Reverse the next pointer to point to the previous node
            current.prev = next_node    # Reverse the previous pointer to point to the next node
            prev_node = current         # Move the previous node to the current node
            current = next_node         # Move to the next node in the list

        self.head = prev_node   # Update the head to the new head of the reversed list
        return self.head        # Return the new head of the reversed list    

    def print_list(self):
        current = self.head    # Start with the head of the list
        while current:         # Iterate through the list until the end 
            print(current.val, end=" ")     # Print the value of the current node
            current = current.next          # Move to the next node in the list
        print()                             # Print a newline character


# ll = Solution()
# reversed_head = ll.reverseList(ll.head)
# ll.print_list()

# Dry run of reverseList
# Initial list: 1 <-> 2 <-> 3 <-> 4 <-> 5
# Step 1: current = 1, prev_node = None
# Step 2: next_node = 2, current.next = None, current.prev = 2
# Step 3: prev_node = 1, current = 2
# Step 4: next_node = 3, current.next = 1, current.prev = 3
# Step 5: prev_node = 2, current = 3
# Step 6: next_node = 4, current.next = 2, current.prev = 4
# Step 7: prev_node = 3, current = 4
# Step 8: next_node = 5, current.next = 3, current.prev = 5
# Step 9: prev_node = 4, current = 5
# Step 10: next_node = None, current.next = 4, current.prev = None
# Step 11: prev_node = 5, current = None
# Reversed list: 5 <-> 4 <-> 3 <-> 2 <-> 1

