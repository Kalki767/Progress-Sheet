class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        '''Approach: Greedy. the problem asks to find the minimum possible
        value of the maximum of the list that can be achieved after performing
        any number of operations. here we are aiming to minimize the maximum
        value in our list but afterall the total sum and average of the list
        won't change becuase while we are decrementing from the current element
        we are incrementing the previous one which would neutralize the effects
        of our operation. Therefore we can achieve the minimum by distributing
        the current element to its's previous elements. but we have constraints
        implying that we need to stop the operation on an element when it
        reaches it's average of the current element with it's previous elements.
        we are calculating the average of the previous elements because we 
        want the current element to be distributed equally until our current 
        index and the maximum value that can be acheived by performing an 
        operation on a single element is that value. the problem is all about 
        distributing a bigger value to smaller values'''
        maximum = total = 0
        for index in range(len(nums)):
            total += nums[index]
            if nums[index] > maximum:
                avg = ceil(total/(index+1))
                maximum = max(maximum,avg)
        return maximum
        #Time Complexity: O(n)
        #Space Complexity: O(1)