# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for val in arr:
            heappush(heap,(abs(val-x),val))
        answer = []
        for i in range(k):
            diff, value = heappop(heap)
            answer.append(value)
        answer.sort()
        return answer
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n)