# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            one_count = 0
            while i > 0:
                if i & 1 == 1:
                    one_count += 1
                i //= 2
            answer.append(one_count)
        return answer