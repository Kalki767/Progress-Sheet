# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''Approach: Top down Dynamic Programming. The problem asks to check
        if we can partition the given array in to two parts that have the
        same sum. The first thing that we are worried abt is if the sum is
        even or not. If the sum is odd then that means we definitely can't
        partition the given array. If not we might be able. So since we say
        the sum of the two arrays need to be equal that means there sum could
        only be half of the total sum. So since we are not asked the components
        of the array we can simply take this sum and check if we can make
        this sum by taking some elements of the array. In other words if we
        take the sum as an argument then simply check if this sum can become
        zero by decrementing some values of the array in that case we would
        return true. So standing at each index we will have to choice either
        to pick that element or not to pick that element. Therefore we might
        get our answer from one of the two branches so we need to check if
        we have got our answer in atleast one of our branches for that we
        will use the or operator. The memoization part comes in to boil
        down the time complexity of our algoirthm since we are doing repetitive
        work we can simply store our current states in a hashmap and if we
        ever need them we will simply retrieve from our hashmap instead of
        doing all the work again.''' 
        memory = {}
        def partition(index,value):
            if value == 0: #if we manage to found elements that sum to target 
                return True

            if index >= len(nums) or value < 0: #if we run out of bound or our sum is less than zero
                return False

            state = (index,value)
            if state not in memory: #check if we already have calculated the current state or not
                memory[state] = partition(index+1,value-nums[index]) or partition(index+1,value)

            return memory[(index,value)] 

        value = sum(nums)
        #if the sum is odd we simply return false
        if value %2 != 0:
            return False

        return partition(0,value//2) #otherwise we call the function
        #Time Complexity: O(n)
        #Space Complexity: O(n)