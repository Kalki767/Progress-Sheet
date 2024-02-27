class Solution:
    def fib(self, n: int) -> int:
        '''Approach: Recursion'''
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
        #Time Complexity: O(2^n)
        #Space Complexity: O(n)

