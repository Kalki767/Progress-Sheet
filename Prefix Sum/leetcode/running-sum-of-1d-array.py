class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = 0
        for index in range(len(nums)):
            current_sum+=nums[index]
            nums[index]=current_sum
        return nums