# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum=0
        current =0
        i,j=0,0
        n = len(nums)
        while j<n:
            if nums[i]==1 and nums[j]==1:
                current+=1
            elif nums[i]!=1:
                i+=1
            else:
                maximum = max(current,maximum)
                current=0
                i=j+1
            j+=1
        maximum = max(current,maximum)
        return maximum
