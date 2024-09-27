# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        '''Approach: Monotonic Stack. The problem asks to find out the building that alice
        and bob could meet based on the given conditions. To solve this problem the
        first observation is we are trying to find the next greater element starting
        from some index till the end. To do that the brute force would be for each
        and every query to find the next greater element. But this is not an efficient
        way as we are repeating the same operation over and over again. So to avoid
        this the first thing that we can observe here is that we can have different
        starting points with the same ending point in that case the array to be scanned
        will be the same we will simply try to find an element that's greater than
        the starting point. Now if we come from backward we can see that if an element
        is greater than the previous element there is no need to keep that element
        because when we are trying to find the next greater element the previous element
        has no chance of getting selected for that case we can keep a monotonically
        decreasing sequence while moving backward. And for each starting index we
        can simply find the next greater element using binary search as the stack is
        already sorted in reversed order. So for this case we need to sort the queries
        in reversed manner to get the bigger ending positions first as we are moving
        backward.'''

        #a function to find the next greater element for the given index in the stack
        def leftmost(index):
            #perform simple binary search
            left, right = 0, len(stack) - 1
            answer = float('inf')
            while left <= right:
                mid = left + (right - left)//2
                cur_index = stack[mid][1]
                #since the array is reverse sorted the movement is also reversed
                if heights[cur_index] > heights[index]:
                    left = mid + 1
                    answer = min(answer,cur_index)
                else:
                    right = mid - 1
            return answer
        
        #before sorting the queries append the index to them to hold the indexes
        for i in range(len(queries)):
            x,y = queries[i]
            if x > y:
                queries[i] = [y,x]
            queries[i].append(i)
        
        queries.sort(reverse = True, key = lambda x : x[1])
        answer = [-1 for _ in range(len(queries))]
        stack = []

        #iterate through the queries and update the answer
        for query in queries:
            x, y, index = query
            last_index = stack[-1][1] - 1 if stack else len(heights)-1

            #add elements to the stack until the ending point which is y
            for i in range(last_index,y,-1):
                while stack and heights[i] >= stack[-1][0]:
                    stack.pop()
                stack.append([heights[i],i])
            
            #if the height is lesser then they both can move to y
            if heights[x] < heights[y]:
                answer[index] = y
            elif x == y:
                answer[index] = x
            else:
                #otherwise call the binary search function and update the result
                res = leftmost(x)
                if res != float('inf'):
                    answer[index] = res

        return answer
        #Time Complexity: O(mlog(m) + mlog(k)) where n is the length of the queries and k is the length of the stack
        #Space Complexity: O(n) where n is the length of the heights