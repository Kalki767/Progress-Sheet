# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''Approach: Top Down Dynamic Programming. The problem asks to find
        all possible partitons that will given a palindromic substring. In
        other words we need to find all partitions in which every substring
        is palindrome. So to do that we need to check every partition if that
        partition will result in a valid partitioning. We created a helper
        function to check if the current partition is valid partition or
        not. If it's a valid partition we will continue to find the next
        valid partition. If we reached the end then that means we have succesfully
        partitioned it so we are going to add the current partitioned ones
        into our answer and try another way. Basically we are performing a
        backtracking and checking every possible partition. To make our algo
        efficient we used memoization when checking if the current partition
        is valid or not we can store for the current partition and resuse it
        for later use.'''
        memory = {}
        # a function to check if the current partition is valid or not
        def palindrome(s,left,right):
            if (left,right) not in memory: #memoizing it
                while left < right:
                    if s[left] != s[right]:
                        memory[(left,right)] = False
                        return False
                    left += 1
                    right -= 1
                memory[(left,right)] = True
                return True
            return memory[(left,right)]

        #perform backtracking to check every possibility
        answer = []
        def dp(index,result):

            if index == len(s): #base case
                answer.append(result[:])
                return 

            for i in range(index+1,len(s)+1): #try every possibility starting from the current index
                if palindrome(s,index,i-1):
                    result.append(s[index:i])
                    dp(i,result)
                    result.pop() 

            return 

        dp(0,[])
        return answer 
        #Time Complexity: O(2**n + n**3)
        #Space Complexity: O(n**2)