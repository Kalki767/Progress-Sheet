# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        '''Approach: Top Down Dynamic Programming. The problem asks to find
        the minimum number of partitions we need to make so that the resulting
        strings in the partitions are palindrome. This question is the same
        as palindrome 1 except we don't need to carry the partitioned strings
        as a parameter rather if we were able to partition succesfully we
        will just simply return 0. Everytime we partition a string we are
        adding the number of partitions by one in that case we add one to
        the current number of partitions and call the function for the 
        remaining substring. To decrease the time complexity we will memoize
        it using our state which will be the index.'''
        memory = {}
        # a function to check if the current partition is valid or not
        def palindrome(s,left,right):       
            return s[left:right+1] == s[left:right+1][::-1]
        answer = []
        def dp(index,n):
            if index == n: #base case
                return 0
            if index not in memory:
                answer = float('inf') #since we are trying to calculate the minimum
                for i in range(index+1,len(s)+1): #try every possibility starting from the current index
                    if palindrome(s,index,i-1):
                        answer = min(answer,dp(i,n)+1)
                memory[index] = answer

            return memory[index]
        return dp(0,len(s)) - 1 #the last partition will also be counted so decrease by one
        #Time Complexity: O(n**2)
        #Space Complexity: O(n)

