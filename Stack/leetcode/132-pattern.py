class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''Approach: Monotonic Stack. The problem asks to find a 132 pattern
        where j is greater than both i and k. And i is less than k. Here we
        use montonically decreasing stack in reversed order. We reversed the
        order because we want j to be maximum as much as possible so that it
        could be greater than both i and k. and we want k to be as big as
        possible but less than j. so whenever we found an element that is
        less than k that means we found our pattern. So at first we set k to
        negative infinity so that no value is less than it. Therefore the k
        value is only updated whenever popping occurs because we want k to
        be less than j and the popping only occurs when a bigger element
        came in so that we pop elements out from the stack in that case we
        can update our k to be the maximum of the popped elements. So whenever
        we find an element that's less than k it means we have already j and
        k and we find i.'''
        k = float('-inf')
        stack = []
        for num in reversed(nums):
            if num < k:
                return True
            while stack and stack[-1] < num:
                k = max(k,stack.pop())
            stack.append(num)
        return False
        #Time Complexity: O(n)
        #Space Complexity: O(n)
            