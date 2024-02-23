class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''Approach: Monotonic Stack. Here the problem asks the total sum
        that we would have if we sum up the minimum of each subarray and
        analyze it. The brute force approach would be generating each
        subarray and taking the minimum and summing up but since we have
        our constraints we need to find an optimal solution. from the problem
        description we need to find how many times the current number can be
        chosen as a minimum of a subarray. that means finding the life span
        of an element being minimum. To do that we use stack and when a
        minimum number comes after then this means this number can no longer
        be a minimum in our subarray. so we pop out that element and find for
        how long it has been minimum. by calculating the number of elements
        to it's left and the number of elements to it's right. so we need to
        store the indexes in the stack. after finishing the for loop we
        ended up having a monotonically increasing stack so we do the same
        operation'''
        stack = []
        answer = 0
        for index in range(len(arr)+1):
            #check if the stack is not empty and if it mets one condition
            while stack and (index == len(arr) or arr[index] < arr[stack[-1]]):

                num = stack.pop()
                left_boundary = stack[-1] if stack else -1
                right_boundary = index

                '''the life span is the number of elements including the
                number that's popped out and the left and the right form
                a combination so we multiply them'''
                life_span = (right_boundary - num) * (num - left_boundary)
                answer += (life_span * arr[num])
                answer %= (10**9+7)
            stack.append(index)
        return int(answer)
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        