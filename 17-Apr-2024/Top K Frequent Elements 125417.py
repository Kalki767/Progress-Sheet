# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''Approach: Min Heap. The problem asks to find the top k frequent
        elements in the array. To solve this problem all we have to do is
        compare the elements of the array based on their frequency. So first
        we will have a counter to count the frequencies after that we are going 
        to build a min heap with size of k why min heap because we want our
        result with size of k which contains only maximum frequent numbers.
        Therefore while building the min heap our comparison would be based
        on the frequencies of the elements and after the heap becomes full
        we check if substituting this would be feasible meaning if the current
        frequency is greater than the minimum of the heap then we would replace
        it.'''

        heap = []
        counter = Counter(nums) #count the frequency of each element
        for key, value in counter.items():
            if len(heap) < k: #if our heap is not full add elements to it
                heappush(heap,(value,key))
            else:
                if value > heap[0][0]: #if the current frequency is greater than the minimum
                    heapreplace(heap,(value,key))
        
        #append the values in the heap to our answer
        answer = []
        for key, val in heap:
            answer.append(val)
            
        return answer
        #Time Complexity: O(nlogk)
        #Space Complexity: O(k)