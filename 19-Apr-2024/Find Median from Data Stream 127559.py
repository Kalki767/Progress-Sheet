# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:
    '''Approach: Heap. The problem asks to find the median of the given data
    stream. To find a median all we have to do is sort the array and find it's
    middle element. But there are elements that are getting added to the array
    that means the median is changed everytime this means the input needs to
    be sorted everytime we find a median but this will not pass the time constraints
    So we need an efficient approach. What should we do? when we are calculating
    the median what if we store the first half and the second half in differnt 
    lists since we are dividing the list when we are finding the median. Therefore
    to calculate the median we need the maximum element from the first half
    and the minimum from the second half. Therefore which datastructure would
    give us an efficient way to retrieve those? Heap!! Therefore we will use
    max heap for the first half and min heap for the second half. We are going
    to divide the array in to equal parts the first array would hold elements
    from the start to the half and the second will hold the remaining elements.
    One simple trick that we will do is all elements in the second half must
    atleast be greater than the maximum of the first half therefore whenever
    we are adding element into one of the heaps we check if this condition is
    satisfied or not. If it's not satisfied we pop elements from the two and
    swap them. And we need to handle one case when calculating the median
    if the length of the array is even or odd.'''
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.counter = 0

    def addNum(self, num: int) -> None:
        #if both the arrays have equal size add element to the first half
        if self.counter%2 == 0:
            heappush(self.max_heap,-1*num)
        else:
            heappush(self.min_heap,num)
        self.counter += 1

        #check if both heaps satisfy the property that we just mentioned
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            value = -self.max_heap[0]
            heapreplace(self.max_heap,-self.min_heap[0])
            heapreplace(self.min_heap, value)

    def findMedian(self) -> float:
        #if the size of the array is even return the average of the first elements of the two
        if self.counter%2 == 0:
            return (-self.max_heap[0]+self.min_heap[0])/2
        return -self.max_heap[0] #otherwise return the first element of the first half
    
    #Time Complexity: O(log(n/2))
    #Space Complexity: O(n)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()