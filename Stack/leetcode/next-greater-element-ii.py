class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''Approach: Montonic Stack. The problem asks to find the next greater
        problem but the difference is the array is circular which means we
        can go back and the first element we have found that's greater than
        the current element is the next greater element. we use a montonic
        stack to keep the maximum element we have found till now and when a
        bigger element comes it kicks out the previous elements and be on top
        of the stack so since we are storing the indexes whenever poping
        out elements occur we update the result list'''
        n = len(nums)
        result = [-1] * n
        stack = []
        for index in range(2*n):
            num = index % n
            while stack and nums[stack[-1]] < nums[num]:
                result[stack[-1]] = nums[num]
                stack.pop()
            stack.append(num)
        return result
        #Time Complexity: O(n)
        #Space Complexity: O(n) 