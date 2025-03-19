# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Given an encoded string, return its decoded string.
# MAGIC
# MAGIC The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# MAGIC
# MAGIC You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
# MAGIC
# MAGIC The test cases are generated so that the length of the output will never exceed 105.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 0 ms
# MAGIC <h3> Beats: </h3> 100%
# MAGIC <h3> Complexity: </h3> O(n)

# COMMAND ----------

def repeat_string(s: str) -> str:
    stack = []  # Initialize an empty stack to keep track of characters and numbers
    for char in s:  # Iterate through each character in the input string
        if char != ']':  # If the character is not a closing bracket
            stack.append(char)  # Push the character onto the stack
        else:  # If the character is a closing bracket
            substr = ""  # Initialize an empty substring
            while stack and stack[-1] != '[':  # Pop characters until an opening bracket is found
                substr = stack.pop() + substr  # Build the substring
            stack.pop()  # Remove the '[' from the stack
            n = ""  # Initialize an empty string to build the number
            while stack and stack[-1].isdigit():  # Pop digits to form the number
                n = stack.pop() + n  # Build the number
            stack.append(int(n) * substr)  # Repeat the substring and push it back onto the stack
    return ''.join(stack)  # Join all elements in the stack to form the final result

result = repeat_string("3[a2[c]]")  # Call the function with the input string
display(result)  # Display the result

# COMMAND ----------

def repeat_string(s: str) -> str:
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
            print(f"Character '{char}' appended to stack: {stack}")
        else:
            substr = ""
            while stack and stack[-1] != '[':
                substr = stack.pop() + substr
                print(f"Building substring: {substr}")
            stack.pop()
            print(f"Opening bracket '[' removed from stack: {stack}")
            n = ""
            while stack and stack[-1].isdigit():
                n = stack.pop() + n
                print(f"Building number: {n}")
            stack.append(int(n) * substr)
            print(f"Repeated substring '{substr}' {n} times and appended to stack: {stack}")
    result = ''.join(stack)
    print(f"Final result: {result}")
    return result

result = repeat_string("3[a2[c]]")
display(result)
