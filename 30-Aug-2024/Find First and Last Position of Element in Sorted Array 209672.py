# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''Approach: Binary Search. The problem asks to find the first and
        last position of the given element. If the target doesn't exist in
        the given list we return -1 for both values. The brute force approach
        would be to find the element in a linear time and check if it exists
        and store it's first index and last index but we are asked to implement
        a solution that runs in logn therefore we need to use binary search.
        Here the searching is not just to find the element but to also update
        the first and last position. Therefore to find the first position we
        need to go to the left whenever a value greater than or equal to the
        target element is encountered whenever we got a match we update our
        first position. The same goes to finding the last position. We go to
        the right whenever we found an element that is less than or equal to
        the target. If the target doesn't exist we just return -1.'''

        #To find the first position
        def leftSearch():
            left, right = 0, len(nums) - 1
            best = -1
            while left <= right:
                mid = left + (right - left)//2

                if nums[mid] == target:
                    best = mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
            return best
        
        #To find the last position
        def rightSearch():
            left, right = 0, len(nums) - 1
            best = -1
            while left <= right:
                mid = left + (right - left)//2

                if nums[mid] == target:
                    best = mid
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid -1
            return best

        return [leftSearch(),rightSearch()]
        #Time Complexity: O(logn)
        #Space Complexity: O(1)
        