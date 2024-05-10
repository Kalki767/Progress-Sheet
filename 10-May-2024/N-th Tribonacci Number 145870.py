# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memory = {0:0,1:1,2:1}
        def memo(n):
            if n not in memory:
                memory[n] = memo(n-1) + memo(n-2) + memo(n-3)
            return memory[n]
        return memo(n)