class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        '''Approach: Greedy. the problem is asking to find the minimum
        number of operations we need to do to make the array sorted. Here
        we choose greedy because we are performing minimum number of 
        operations as much as possible starting from the second last element 
        since the last element is the maximum we can achieve we don't need
        to split it. after that whenever we found an element that is greater
        than the previous we find the number of splits that could be achieved
        and the maximum value that can we have after spliting that is less 
        than the previous element. So the greediness is all about finding
        the maximum number from the splits we have done that is less than
        the previous one so that we will have minimum number of splits'''
        previous = nums[-1]
        answer = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] <= previous:
                previous = nums[i]
                continue
            number_of_elements = ceil(nums[i]/previous)
            answer += number_of_elements - 1
            previous = nums[i]//number_of_elements
        return answer
        #Time Complexity: O(n)
        #Space Complexity: O(1)