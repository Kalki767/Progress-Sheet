# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        '''Approach: Heap. The problem asks to find the maximum difference between
        two elements that are taken from two different arrays. So simply what we
        can do is take the minimum and maximum out of all. But one issue that arises
        here is we might take the values from the same array which is not allowed.
        So what we did here is we add all elements along with our index to a heap.
        We used two heaps one for maximum and the other for minimum. Now upon 
        retrieving those values we check if they are from the same array or not
        if so we keep finding an element from different array. For this case we will
        have two cases the first one is choosing the minimum first and the second
        one is choosing the maximum first finally we will take the maximum of all.'''
        answer = float('-inf')
        min_heap = []
        max_heap = []

        for index in range(len(arrays)):
            cur = arrays[index]
            for num in cur:
                heappush(min_heap,(num,index))
                heappush(max_heap,(-num,index))

        minimum, min_index = min_heap[0]
        maximum , max_index = heappop(max_heap)

        while min_index == max_index and max_heap:
            maximum , max_index = heappop(max_heap)

        answer = max(answer,abs(-1*maximum - minimum))
        max_heap = []

        for index in range(len(arrays)):
            cur = arrays[index]
            for num in cur:
                heappush(max_heap,(-num,index))

        minimum, min_index = heappop(min_heap)
        maximum , max_index = max_heap[0]

        while min_index == max_index and min_heap:
           minimum, min_index = heappop(min_heap)
           
        answer = max(answer,abs(-maximum - minimum))
        return answer
        #Time Complexity: O(nlogm)
        #Space Complexity: O(n) where n is total number of elements in the given array