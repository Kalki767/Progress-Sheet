class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''Approach: Binary Search. The problem asks to find the minimum number
        of a sorted array which has been rotated n times where n is unknown.
        To solve this problem since it should be in logn we can't use brute
        force because that would result in n and it wouldn't pass the testcase.
        Here we can use on fact if the array is rotated there is one fluctuation
        where the current value is greater than the next value. A point where
        the sorted array fails. So what we will do is try to find that pivot
        or if the array wasn't rotated then we keep a minimum value and if nothing
        is returned we return our minimum as it would be on the first'''
        left,right,minimum = 0, len(nums)-1, float('inf')
        while left <= right:
            mid = left + (right - left)//2
            if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
            minimum = min(nums[0],nums[mid],minimum)
        return minimum
        #Time Compelxity: O(logn)
        #Space Complexity: O(1)