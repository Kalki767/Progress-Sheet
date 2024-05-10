# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''Approach: Dynamic Programming. The problem asks to find the maximum
        amount of money if we rob the houses given that we don't rob conescutive
        houses. For that matter at each steo we have two choices either to rob
        that house or not to rob the house. If we decide to rob the current
        house since we cannot rob the next house we will simply go to the
        house that's two steps away and increase the money by the current
        value. If we choose not to rob the house then we will directly go to
        the next house and the amount of money that we have will be the same
        as the previous one. So the basic intuition is based on this decision
        we will take the maximum money we could make standing from each house.
        To avoid recalculating the same value over and over again we can
        store them and use them later which is basically memoization.'''
        money = {}
        def robbing(index):
            if index >= len(nums):
                return 0
            if index not in money:
                money[index] = max(nums[index] + robbing(index+2), robbing(index+1))
            return money[index]
        return robbing(0)
        #Time Complexity: O(n)
        #Space Complexity: O(n)