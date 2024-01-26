class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Step1: count the occurences of 0 and 1 in the list
        count_of_zero = nums.count(0)
        count_of_one = nums.count(1)
        left=0

        #Step2:iterate through the array once while updating elements based on the status of the count variables
        while left<len(nums):
            if count_of_zero>0:
                nums[left]=0
                count_of_zero-=1
            elif count_of_one>0:
                nums[left]=1
                count_of_one-=1
            else:
                nums[left]=2
            left+=1
    