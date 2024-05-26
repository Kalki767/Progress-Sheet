# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primefactors(n):
            ans = set()
            i = 2
            while n > 1:
                while n % i == 0:
                    ans.add(i)
                    n //= i
                i += 1
            return ans
        answer = set()
        for num in nums:
            res = primefactors(num)
            answer = answer.union(res)
        return len(answer)