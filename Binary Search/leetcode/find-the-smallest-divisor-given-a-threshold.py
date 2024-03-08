class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''Approach: Binary Search. The problem asks to find the minimum divisor
        so that the sum of the list is less than or equal to the threshold.
        To find that all we have to do is try each value starting from 1 up
        to the maximum value because at maximum we could divide all the numbers
        by the maximum value and the least we could divide them by one. But
        iterating through the divisors one by one is inefficient. So we can use
        binary search to boil down the time complexity. Therefore if the current
        sum is less than or equal to the threshold we update our divisor and 
        shrink the second half if not we just shrink the first half and try looking
        for minimum divisort in the next half.'''
        lower_bound, upper_bound = 1, max(nums)
        minimum_divisor = float('inf')
        while lower_bound <= upper_bound:
            mid = lower_bound + (upper_bound - lower_bound)//2
            total = 0
            for index in range(len(nums)):
                total += ceil(nums[index]/mid)
            if total <= threshold:
                minimum_divisor = min(minimum_divisor,mid)
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1
        return minimum_divisor 
        #Time Complexity: O(nlogn)
        #Space Complexity: O(1)