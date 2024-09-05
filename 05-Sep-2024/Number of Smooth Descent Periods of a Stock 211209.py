# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        '''Approach: Sliding Window with Math. The problem asks to count the number
        of smooth descent periods of a stock. So for that case what if we find
        a window that fullfils the smooth descent period that would be counted one.
        but also if we found the maximum window avaliable in that slot then all sub
        windows are also eligible. For that case we can generate a math formula using
        some proofs which will end up being the combnatorics of n with 2. Then we
        will do this for every window that fullfills the criteria. One thing not to
        forget is each day also fullfills the criteria for that case we are expected
        to add the length of the given price on the final answer'''

        #Step1: declare variables for ease of use
        left, right = 0, 1
        length = len(prices) #due to the fact that every element also fullfills the criteria
        answer = length

        #Step2: iterate until the list gets exhausted
        while right < length:

            #check if the current window is fullfilling the criteria
            while right < length and prices[right - 1] - prices[right] == 1:
                right += 1

            window = right - left
            cur = (window - 1) * window // 2
            answer += cur
            left = right
            right += 1

        return answer
        #Time Complexity: O(n)
        #Space Complexity: O(1)