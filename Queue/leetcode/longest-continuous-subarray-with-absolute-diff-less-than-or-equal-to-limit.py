class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''Approach: Queue. we used montonic queue to keep track of the
        maximum and minimum elements we have encountered so far. When a
        maximum element comes it kicks out the previous max element from
        the max queue and the same thing is done for the min queue. after
        that we will have the maximum value and minimum value of our subarray
        at the first index of both queues so we check if their difference is
        greater than the limit if so we move the left pointer by one and pop
        the value associated with the left pointer from the queue from the
        left '''
        left = right = 0
        longest_subarray = 1
        #initalizing min queue and max queue
        min_queue = deque()
        max_queue = deque()
        for right in range(len(nums)):
            
            '''if the current element is greater than the element at the top
            pop the previous element'''
            while max_queue and nums[right] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(nums[right])

            '''if the previous element is greater than the current element
            pop until that condition holds'''
            while min_queue and nums[right] < min_queue[-1]:
                min_queue.pop()
            min_queue.append(nums[right])

            '''if their difference is greater than the limit pop the neccesary
            element and move the left pointer one step'''
            if max_queue[0] - min_queue[0] > limit:
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                left += 1

            #update the size of the subarray
            longest_subarray = max(longest_subarray,right-left+1)
            
        return longest_subarray
        #Time Complexity: O(n)
        #Space Complexity: O(n)