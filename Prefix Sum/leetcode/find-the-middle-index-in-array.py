class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        running_sum =0
        prefix_sum = [0]*len(nums)
        for i in range(len(nums)):
            running_sum+=nums[i]
            prefix_sum[i]=running_sum
        for index in range(len(nums)):
            left_sum = prefix_sum[index]-nums[index]
            right_sum = prefix_sum[-1]-prefix_sum[index]
            if left_sum==right_sum:
                return index
        return -1