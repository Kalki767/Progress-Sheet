class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''Approach: Binary Search. The problem asks to find the insert 
        position of an element in a sorted list. Therefore all we need to do
        is find the position of that element using a binary search since it
        doesn't exist in the list we won't find it but at last our left pointer
        would be on a position that we could insert our current value.'''
        position = 0
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
        #Time Complexity: O(logn)
        #Space Complexity: O(1)