class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        '''Approach: Binary Search. The problem asks to find the number of
        subsequences where the maximum plus the minimum is not greater than
        the given target. Here we are asked for subsequence not subarray so
        the order doesn't matter. This means we can reorder the given array.
        The reason why we are sorting the input is because we can smaller
        numbers to the start and large numbers to the end that way it would
        be easier to find the maximum value for the current element that way
        the elements between those two are also subsequences for the current
        element. Therefore all we need to do is find the index of the maximum
        value that could be added to the current element so that the subsequence
        is valid. If the value we got is less than the current number then
        there is no way that this element could be a minimum value to any 
        subsequence so we skip that element. We potentially used binary search
        for finding the value since we have already sorted it would decrease 
        our time complexity. Finally to find the combinations we draw a pattern
        and since their lengths differ we can use 2**(length -1) and add it
        to our subsequence. For decreasing time complexity even further we
        can use the pow function including the mod.'''

        mod = 10**9 + 7
        nums.sort()
        number_of_subsequences = 0

        for index ,num in enumerate(nums):
            value = target - num
            
            if value < num: #if the value is less then this can't be minimum of a subsequence
                continue

            right_index = bisect_right(nums,value)
            length = right_index - index - 1
            combinations = pow(2,length,mod)
            number_of_subsequences += combinations

        return number_of_subsequences % mod
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n) for call stack for the power function