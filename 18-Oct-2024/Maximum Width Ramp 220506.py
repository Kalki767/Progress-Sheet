# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        '''Approach: Monotonic Stack with Binary Search. The problem asks to find
        the maximum distance between two indexes i,j where nums[i]'''
        def bisect_left_reverse(x):
            # Get the insertion point as if the list were sorted in ascending order
            pos = bisect_left(reversed_stack, x)
            
            # Adjust the position for the reverse sorted array
            return len(stack_val) - pos - 1
        stack_val = []
        stack_index = {}
        for index, value in enumerate(nums):
            while stack_val and stack_val[-1] <= value:
                stack_val.pop()
                
            stack_val.append(value)
            stack_index[value] = index
        answer = 0
        reversed_stack = list(reversed(stack_val))
        length = len(stack_val)
        for index, value in enumerate(nums):
            next_greater = bisect_left_reverse(value)
            if next_greater == length:
                continue
            
            cur = stack_index[stack_val[next_greater]]
            answer = max(answer,cur - index)
        return answer