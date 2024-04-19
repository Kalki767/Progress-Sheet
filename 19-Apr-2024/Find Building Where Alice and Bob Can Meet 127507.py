# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        '''Approach: Monotonic Stack. The problem asks to find the meeting place
        for alice and bob based on the rules given. To find this all we have to
        do is find the next greater element for each height and whenever a query
        is asked check for the given rules. After that if the height of j is
        less than or equal to the height of i we will be at least in the next
        greater element of j. Therefore we have to check if that building is
        greater than the height of building i if so we will just append it to
        our list if not we will find the next greater element of that element
        and if we end up on -1 then alice and bob will not meet because our
        starting point was the next greater element of j therefore if all 
        elements that we are founding are less than heights[i] and if at some
        point we find -1 that means there is no building that is greater than
        the ith building.'''

        #for tracking the next greater element
        building = [-1]*len(heights)
        stack = []
        answer = []

        #use stack to track the next greater element for each value
        for index, height in enumerate(heights):
            while stack and stack[-1][0] < height:
                prev_height, prev_index = stack.pop()
                building[prev_index] = index
            stack.append((height, index))
        
        #for each query perform the following operation
        for query in queries:
            i, j = query
            #if i is greater than j swap them because we want them to be ordered
            if i > j:
                i, j = j, i
            
            #if alice and bob are on the same building then they can meet there
            if i == j:
                answer.append(i)
            
            #if the height of alice is less than the height of bob then alice can move up there
            elif heights[i] < heights[j]:
                answer.append(j)
            
            #otherwise find a bigger buliding for both
            else:
                first, second = building[i], building[j]
                if first == -1 or second  == -1:
                    answer.append(-1)
                else:
                    current = j
                    ''' start with the first bigger building for the second element and
                    iterate until u find a bigger element for both.'''
                    while building[current] != -1 and heights[current] <= heights[i]:
                        current = building[current]
                
                    #if the current height is greater than the height of i then both alice and bob can move to the current
                    if heights[current] > heights[i]:
                        answer.append(current)
                    else:
                        answer.append(-1) #otherwise they can't meet
                       
        return answer
        #Time Complexity: O(n**2)
        #Space Complexity: O(n)