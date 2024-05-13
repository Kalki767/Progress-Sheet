# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''Approach: Top Down Dynamic Programming. The problem asks to find
        the longest common subsequence of two texts. To find that we start
        at the first index and try out all possibilities if the characters
        on those indexes are the same then we will check for the next ones
        if not we are going to try either by moving one of the indexes and
        taking the maximum. The base case will be when either of the indexes
        run out of bound. In this case we make sure that we have generated
        each possible combination but the time complexity won't pass so we
        need to memoize it so that we won't have to recalculate previously
        calculated values. The states will be the indexes of both texts.'''
        memory = {}
        def dp(i,j):
            #base case for checking if we have run out of bounds
            if i >= len(text1) or j >= len(text2):
                return 0
            
            # otherwise check if the state is already calculated if not calculate it
            state = (i,j)
            if state not in memory:
                ans = 0
                #if we find a matching character then add one to our answer and increment both indexes
                if text1[i] == text2[j]:
                    ans = 1 + dp(i+1,j+1)
                else:
                    #otherwise check by incrementing either of the indexes
                    ans = max(dp(i+1,j),dp(i,j+1))
                memory[state] = ans

            return memory[state]

        return dp(0,0)
        #Time Complexity: O(n**2)
        #Space Complexity: O(n**2)