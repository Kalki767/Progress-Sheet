# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        '''Approach: Binary Search. The problem asks to find the maximum among the
        minimums by choosing some random numbers from the intervals. Here by
        observation we saw that the minimum value can be obtained from neighbouring
        intervals if we sort the intervals in increasing order. So if we know the
        maximum range that we could have between two neighbours the minimum among
        them will be the maximum range that could be achieved but this is not our
        answer since there might be overlapping intervals we need to search for the
        maximum value that satisfies our condition. We are searching on the range
        of values from 0 to the maximum that we found by iterating. So instead of
        checking every element meaning applying linear search we can apply binary
        search for an efficient searching method. So for each value all we have to
        check is can this be a minimum difference across all the intervals. We can
        have a helper function to check whether or not this is a valid value if so
        we will increment the left pointer otherwise we will shift the right pointer.
        '''
        #a helper function to check the validity of a given difference
        def check(diff):
            prev = start[0]

            '''iterate through the start and increment the diff on the current 
            starting point if that point is greater than the end of the next interval
            then simply return false otherwise continue iterating'''
            for i in range(0,len(start)-1):
                next_val = prev + diff
                if next_val > start[i+1] + d:
                    return False
                prev = max(next_val,start[i+1])
            return True
        
        #find the maximum differnece that we can have
        maxi = float('inf')
        start.sort()
        for i in range(1,len(start)):
            cur = start[i] + d - start[i-1]
            maxi = min(maxi,cur)
        
        #perform a binary search on the answer
        left,right = 0, maxi
        answer = 0
        while left <= right:
            mid = left + (right - left)//2
            if check(mid):
                answer = max(answer,mid)
                left = mid + 1
            else:
                right = mid - 1

        return answer
        #Time Complexity: O(nlogn) where n is the length of the start array
        #Space Complexity: O(1)