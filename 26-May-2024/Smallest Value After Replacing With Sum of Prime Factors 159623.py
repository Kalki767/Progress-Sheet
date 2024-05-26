# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def PrimeFactors(n):
            answer = 0
            divisible = 2
            while n > 1:
                while  n%divisible == 0:
                    answer += divisible
                    n //= divisible
                divisible += 1
            return answer
        minimum = n
        while True:
            minimum = min(n,minimum)
            val = PrimeFactors(n)
            if val == n:
                break
            n = val
        return minimum