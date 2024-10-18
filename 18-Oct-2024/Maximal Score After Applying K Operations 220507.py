# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        max_heap = [-num for num in nums]
        heapify(max_heap)
        for i in range(k):
            cur = -heappop(max_heap)
            score += cur
            cur = math.ceil(cur/3)
            heappush(max_heap,-cur)
        return score