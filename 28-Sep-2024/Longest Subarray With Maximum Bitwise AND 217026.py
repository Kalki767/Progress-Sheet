# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''Approach: Sliding Window with bitmask. The problem asks to find the length
        of the longest subarray that has the maximum AND value across the subarray.
        To solve this a basic observation would be to use a sliding window to solve
        it. But we can use a simple trick here the maximum and value that we coulld
        have is the maximum value of the array. Because AND operations between two
        different numbers end up giving a number that's smaller than the bigger number
        for that case all we have to do is find the maximum number and at the start
        of this maximum number count it's consecutives that are equal to it and take
        the maximum. '''
        maximum = max(nums)
        right = 0
        max_length = 1
        while right < len(nums):
            if nums[right] != maximum:
                right += 1
                continue
            length = 0
            while right < len(nums) and nums[right] == maximum:
                length += 1
                right += 1
            max_length = max(max_length,length)
        return max_length
        #Time Complexity: O(n)
        #Space Complexity: O(1)