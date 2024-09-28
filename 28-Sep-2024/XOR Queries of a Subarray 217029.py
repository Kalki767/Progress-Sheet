# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        '''Approach: Prefix Sum. The problem asks to find the XOR of any subarray.
        There are range of queries to answer to solve this problem calculating for
        each query starting from the start to the end isnot an efficient way to solve
        the problem. But we know one thing the xor of a number with itself is zero.
        So if we know the prefix until now to find the xor of this range we can
        simply xor it with the previous one to cancel that part and the xor of the
        middle will be remaining. So we will be using prefix sum to track the xor
        till now.'''

        #Step1: calculate the prefix sum for the array
        prefix_sum = [0]
        for num in arr:
            cur = prefix_sum[-1] ^ num
            prefix_sum.append(cur)
        
        #Step2: iterate through the range of queries and build the answer
        answer = []
        for start, end in queries:
            res = prefix_sum[end+1] ^ prefix_sum[start]
            answer.append(res)

        return answer
        #Time Complexity: O(n)
        #Space Complexity: O(n) where n is the length of the array