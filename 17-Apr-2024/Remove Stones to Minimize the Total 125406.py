# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)
        while k >0:
            stone = -heappop(piles)
            heappush(piles,-ceil(stone/2))
            k -= 1
        piles = [-pile for pile in piles]
        return sum(piles)