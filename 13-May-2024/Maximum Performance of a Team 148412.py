# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        '''Approach: Greedy. The problem asks to find the maximum performance of
        a team given the circumstances. To maximize the performance of a team
        we need to maximize both the efficiency and the speed but there is
        a tradeoff between the two when we are trying to maximize the speed
        we might lose efficiency and vice versa. So what if we have the efficiencies
        in decreasing order so that we could get the maximum ones first in this
        way we are trading off the efficiency for speed since the speed will
        be added but the efficiency is multiplied. So at each step we will take
        the maximum performance and when our heap is full we will pick out the
        engineer with the smallest speed since we add them according to their
        efficiency it would only be feasible if we pop them with respective
        speed.'''
        min_heap = []
        eff_speed = [(efficiency[i],speed[i]) for i in range(n)] #zip the enginners speed and performance together
        eff_speed.sort(reverse=True)
        total = 0
        ans = 0

        # iterate through the zipped engineers and add each speed
        for i in range(len(speed)):
            eff, speed = eff_speed[i]
            total += speed

            #if we still have space to add engineers to our heap
            if len(min_heap) < k:
                heappush(min_heap,(speed,eff))
            else: #otherwise pop the engineer with the smallest spees
                min_speed, min_eff = heappop(min_heap)
                heappush(min_heap,(speed,eff))
                total -= min_speed

            ans = max(ans,total*eff) #take the maximum performance

        return ans % (10**9+7)
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n)