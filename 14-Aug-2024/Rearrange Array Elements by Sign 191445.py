# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums = [num for num in nums if num>0]
        negative_nums = [num for num in nums if num<0]
        merged_nums = [0]*len(nums)
        left = right = 0
        while right<len(nums):
            merged_nums[right] = positive_nums[left]
            merged_nums[right+1] = negative_nums[left]
            right+=2
            left+=1
        return merged_nums