# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        index = 0
        for seek in range(len(nums)):
            if nums[seek]!=0:
                nums[index],nums[seek]=nums[seek],nums[index]
                index+=1
        return nums