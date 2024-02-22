class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''Approach: Monotonic decreasing Stack. The problem asks to find the
        number of days we have to wait for warmer temprature after the current
        day. So we use a montonically decreasing stack to keep track of the 
        bigger element. if the element to be appended is greater than the one
        that was in our stack then that's how much we have to wait'''
        n = len(temperatures)
        answer = [0]*n
        stack = []
        for index in range(n):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                answer[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return answer 
        #Time Complexity: O(n)
        #Space Complexity: O(n)
