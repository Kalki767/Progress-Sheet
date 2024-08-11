# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''Approach: Binary Search. The problem asks to check if a target value exists
        in a given list. This problem is the same as search rotated array the only
        difference is there are dupicates here so we need to determine where would
        our first solution would fail since we have duplicates the only issue that
        will arise is determining which part is sorted either the left or the right.
        The easiest way to determine that is comparing the mid with the left and right.
        But what if three of them are equal so we need to handle that case since we
        can't simply determine which half is sorted but we know one thing for sure
        if the mid value is not the target then both the left and right are not the
        target therefore we can move both pointers by one shrinking the array and 
        conitnue our binary search.
        '''
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] == target: #check if the current element is the target
                return True
            
            #in the case of duplicates move both pointers by one
            if nums[low] == nums[mid] == nums[high]: 
                low += 1
                high -= 1

            #check if left half is sorted
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
        #Time Complexity: O(n/2) in the worst case we only have two unique elements and the other are duplicates
        #Space Complexity: O(1)