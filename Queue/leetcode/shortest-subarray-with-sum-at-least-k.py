class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        '''Approach: Monotonic queue combined with Prefix Sum. The problem
        asks to find the shortest subarray whose sum is atleast k. We could
        have simply used sliding window and try to update our length once
        we have found a subarray with sum atleast k but the problem arises
        once we realize our array could contain negative numbers which would
        require for a better approach. The problem could still be solved using
        sliding window but here we are using monotonic queue. So as the problem
        name suggests we are trying to find a subarray so the one thing that
        we will always do is once we found a sum which is atleast equal to k
        we start popping out from the left to check if our sum will still be
        valid. So here comes the reason why we should be using monotonic queue
        and not an ordinary queue. The reason is if we maintain normal queue
        we would be just popping from the left and trying to compare the sum
        but what if a negative number follows that element then our sum will
        definitely decrease right so if we were to keep the previous sum without
        including the negative number then we would get a false alarm that our
        window isnot valid when it could actually be valid. So the first thing
        we need to do is calculate the prefix sum and store it in an array.
        After that we will try to build a monotonically increasing queue because
        of the reason we mentioned above. when a negative number follows a positive
        number our sum will decrease and since we want to ensure monotonocity
        we will pop out elements and another reason is if we want to pop out
        elements we don't want to pop out the positive ones just the negative
        ones but if they are both associated then we would rather pop out
        the sum of both and expect to see a change rather than popping out
        a positive number which was followed by a negative number and expect
        to see a change that wouldn't be right.'''

        minimum_length = float('inf')
        queue = deque()
        current_sum = 0
        prefix_sum = [0] #having an offset zero so that it won't mess up when checking if the sum is atleast k

        #for calculating prefix sum
        for num in nums:
            current_sum += num
            prefix_sum.append(current_sum)

        #for finding the length of shortest subarray
        for index,num in enumerate(prefix_sum):

            #ensuring our queue is montonically increasing
            while queue and num < prefix_sum[queue[-1]]:
                queue.pop()
            queue.append(index)

            #checking if our current prefix sum is atleast k while popping out the leftmost element and update the length
            while queue and prefix_sum[queue[-1]] - prefix_sum[queue[0]]>= k:
                minimum_length = min(minimum_length,index - queue[0])
                queue.popleft()

        return minimum_length if minimum_length!= float('inf') else -1
        #Time Complexity: O(n)
        #Space Complexity: O(n) because we used queue
            