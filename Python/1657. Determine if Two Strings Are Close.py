# Databricks notebook source
# MAGIC %md
# MAGIC <h5> ROBLEM DESCRIPTION </h5>
# MAGIC Two strings are considered close if you can attain one from the other using the following operations:
# MAGIC
# MAGIC Operation 1: Swap any two existing characters.
# MAGIC For example, abcde -> aecdb
# MAGIC Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# MAGIC For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# MAGIC You can use the operations on either string as many times as necessary.
# MAGIC
# MAGIC Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
# MAGIC
# MAGIC  
# MAGIC
# MAGIC Example 1:
# MAGIC
# MAGIC Input: word1 = "abc", word2 = "bca"
# MAGIC Output: true
# MAGIC Explanation: You can attain word2 from word1 in 2 operations.
# MAGIC Apply Operation 1: "abc" -> "acb"
# MAGIC Apply Operation 1: "acb" -> "bca"
# MAGIC Example 2:
# MAGIC
# MAGIC Input: word1 = "a", word2 = "aa"
# MAGIC Output: false
# MAGIC Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
# MAGIC Example 3:
# MAGIC
# MAGIC Input: word1 = "cabbba", word2 = "abbccc"
# MAGIC Output: true
# MAGIC Explanation: You can attain word2 from word1 in 3 operations.
# MAGIC Apply Operation 1: "cabbba" -> "caabbb"
# MAGIC Apply Operation 2: "caabbb" -> "baaccc"
# MAGIC Apply Operation 2: "baaccc" -> "abbccc"
# MAGIC  

# COMMAND ----------

# MAGIC %md
# MAGIC ### Run Time: </h3> 90 ms
# MAGIC <h3> Beats: </h3> 61%
# MAGIC <h3> Complexity: </h3> O(N)
# MAGIC

# COMMAND ----------

from collections import Counter 
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
       
        def count_occurrence(word):
            c = Counter(word)
            return c.values()

        def product(array):
            p=1
            for i in array:
                p *=i
            return p

      

        s1,s2,cnt1,cnt2,p1,p2 = set(word1),set(word2),count_occurrence(word1), count_occurrence(word2),1,1
              
        
        if len(word1) != len(word2):
            return False
        else:
            p1,p2,sm1,sm2,mx1,mx2 = product(cnt1),product(cnt2),sum(cnt1),sum(cnt2),max(cnt1),max(cnt2)
         
            if mx1 > mx2:
                diff = mx1-mx2
            else:
                diff = mx2-mx1

            
            if p1 == p2 and sm1 == sm2 and diff <= 2:
                c=0
                for s in s1:
                    if s in s2:
                        c += 1
                if c == len(s1):
                    return True
                else:
                    return False
            
            else: 
                return False
                

          
