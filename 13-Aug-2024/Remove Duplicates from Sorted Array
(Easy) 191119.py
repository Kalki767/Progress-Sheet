# Problem: Remove Duplicates from Sorted Array
(Easy) - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j =0,1
        while j<len(nums):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
            j+=1
        return i+1