class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''Approach: Monotonic Stack. The problem asks to find the rectangle 
        with maximum area. The blocks need not be adjacent. To find the area
        what we need is to know how much the current height could extend to
        the left and the right. If we have that knowledge then the area is just
        the product of the width and the height. Therefore in simple terms
        all we need to find is the minimum life span of an element after that
        we could just multiply it by the height to find the area associated
        with that element. So we used monotonically increasing stack to keep
        track of increasing elements when a smaller element came then the life
        span of being minimum for the top of the stack has just ended so we will
        calculate how many elements are there to the right of it and to the 
        left of it then the total width is the sum of both after that the area
        is the product of width and height then we take the maximum at each
        iteration. We deal with the leftovers after we finished iterating.'''
        maximum_area = max(heights)
        stack = []

        for index, height in enumerate(heights):
            #maintaining montonically increasing stack
            while stack and heights[stack[-1]] > height:
                #the index of the current height
                current_index = stack.pop()

                #number of blocks to the right where the current element is still minimum
                right_width = index - current_index - 1 

                #number of blocks to the left where the current element is still minimum including itself
                left_width = current_index - stack[-1] if stack else current_index + 1

                #calculating the area while popping out elements
                area = (left_width + right_width) * heights[current_index]
                maximum_area = max(maximum_area,area)
            stack.append(index)

        '''at the end we will have a stack of heights which could be fully 
        extend to the right and to the left as possible so we perform the
        same thing as we did above with just a simple modification to the
        right width.'''

        while stack:
            current_index = stack.pop()
            right_width = len(heights) - current_index - 1
            left_width = current_index - stack[-1] if stack else current_index + 1
            area = (right_width + left_width)* heights[current_index]
            maximum_area = max(maximum_area,area)
            
        return maximum_area 
        #Time Complexity: O(n)
        #Space Complexity: O(n)