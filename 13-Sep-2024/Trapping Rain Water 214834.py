# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        '''Approach: Monotonic Stack. The problem asks to find the amount of water
        that will be trapped. To find this first let's observe some things. Here
        as obvious a water can be trapped between two bars if there is a space
        between them that can trap a water. For that case we are looking for a
        curve where the height of the bars were decreasing and a bar with bigger
        height came into the picture. This way we can trap a water. But the question
        rises how can we calculate the water that's trapped. It's simple for a bar
        to trap a water it needs to have to bars that are greater than itself from
        the left and the right after that all we need to find is the minimum height
        of those bars and how much water can be stored by subtracting the height of
        the bar from the minimum height. But one issue arises here if we have already
        filled water then the next time a bar with greater height comes we need to
        consider the previously filled water that is also at the same level of the
        current height that's getting kicked out. For that case we need to find out
        how many cells have this amount of height by calculating the left and right
        value for this case we will store the indexes instead of the values. So this
        is where the montonic stack came into the picture to handle the decreasing
        part. We will use montonically decreasing stack.'''
        stack = []
        trapped_water = 0
        length = len(height)
        for i in range(length):

            #while the current height is greater than the previous keep the iteration
            while stack and height[stack[-1]] <= height[i]:
                cur = stack.pop()
                if not stack: #if there is no other bar behind break the loop as no water can be trapped
                    break
                #calculate how many bars there are with the current height
                left = cur - stack[-1] - 1
                right = i - cur

                #find the minimum height and the water that can be stored with this height
                min_height = min(height[stack[-1]],height[i])
                water = min_height - height[cur]

                #total water would be the bars multiplied by the total water that can be stored on single bar
                water_trap = (left + right) * water
                trapped_water += water_trap

            stack.append(i)
        return trapped_water
        #Time Complexity: O(n)
        #Space Complexity: O(1)