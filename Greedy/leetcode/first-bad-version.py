# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''Approach: Binary Search. The problem asks to find the first defected
        element given the number of bulbs and defects. So we can assume that
        the first time a bulb is bad means the bulb before it is not bad that
        means we can check if the current element is bad and the previous element
        is not bad then we return the mid. We used binary search to minimize
        the number of calls to the API.'''
        left , right = 0 , n
        while left <= right:
            mid = left + (right - left)//2
            if not isBadVersion(mid-1) and isBadVersion(mid):
                return mid
            elif isBadVersion(mid):
                right = mid -1
            else:
                left = mid + 1
        return
        #Time Complexity: O(logn)
        #Space Complexity: O(1)