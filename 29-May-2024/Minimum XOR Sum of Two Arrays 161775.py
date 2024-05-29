# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[float('inf') for _ in range(1<<n)] for _ in range(n)]
        dp.append([0 for _ in range(1<<n)])
        for index in range(n-1,-1,-1):
            for mask in range((1<<n)-1,-1,-1):
                min_xor = float('inf')
                for i in range(n):
                    if mask & (1<<i) == 0:
                        min_xor = min(min_xor, (nums1[index]^nums2[i]) + dp[index+1][mask | (1<<i)])
                dp[index][mask] = min_xor
        return dp[0][0]
