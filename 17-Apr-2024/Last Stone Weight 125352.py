# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''Approach: Max Heap. The problem asks to remove two heaviest stones
        and perform the operations stated and at last return the last weight.
        Therefore this would simply be a max heap why max heap because we want
        to pop the maximum element in an efficent manner. Therefore after a
        series of operations the length of the heap will be either 0 or 1.
        So if it's zero there is no stone left return 0 if there is stonde
        return the weight of that stone.'''

        #for building the max heap change the positive weight to negative ones
        stones = [-1*stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            y = heappop(stones)
            x = heappop(stones)
            if x != y: #if the weight of the two differ add their difference to the heap
                heappush(stones,y-x)
        
        return -stones[0] if stones else 0
        #Time Complexity: O(nlogn)
        #Space Complexity: O(1)