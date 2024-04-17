# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.counter = 0
        self.length = k
        # add the elements in the list into the heap
        while self.counter < len(nums):
            heappush(self.heap,nums[self.counter])
            self.counter += 1
        #if the size of the heap is greater than k pop the minimum elements
        while self.counter > k:
            heappop(self.heap)
            self.counter -= 1
        

    def add(self, val: int) -> int:
        #if the size is still less than k add elements to it
        if self.counter < self.length:
            heappush(self.heap,val)
            self.counter += 1
        else:
            #if the current element is greater than the minimum of the previous element replace it
            if self.heap[0] < val:
                heapreplace(self.heap,val)
        
        return self.heap[0]
        #Time Complexity: O(logk)
        #Space Complexity: O(k)



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)