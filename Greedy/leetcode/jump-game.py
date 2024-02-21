class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''Approach: Greedy. the problem is asking if we can reach the end
        or not given the maximum jumps we can at each step. Here we are
        being greedy on jumping as maximum as we can and checking where
        we will end up if we jump using the current move and if we have
        jumped previously. we take the maximum position we could be at each
        iteration and if the maximum position that I could reach standing
        on a position is itself then I can't go anywhere which means I
        can't reach the end. otherwise I can reach the end'''
        maximum_move = 1
        for right in range(len(nums)-1):
            maximum_move = max(nums[right]+right+1,maximum_move)
            if maximum_move <= right+1:
                return False
        return True
        #Time Complexity: O(n)
        #Space Complexity: O(1)