# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''Approach: Heap. The problem asks how far we can reach with the given
        ladders and bricks. But we need to use them optimally. So what do we
        mean by optimally. We obviously want to move the small steps using 
        the bricks and the larger ones using the ladders therefore while going
        forward our first choice would be bricks but if the total bricks that
        we have already used surpass the bricks that are given to us then we
        will simply try to use a ladder for the bigger step that has been before
        but how do we find the bigger step from all the steps we took efficiently.
        This is why we use heap because it would give us the maximum step we took
        so far in an efficient manner. Therefore while going if we need bricks
        or ladders we will add the amount of bricks needed to our total bricks
        and we check have we surpassed if we already have then we check do we
        have ladders if so we will take the maximum step out of the heap and 
        increase the number of used ladders by one. If at some point the ladder
        becomes full and we are out of bricks too we will return the current
        index otherwise we will return the last index.'''
        ladder = 0
        used_bricks = []
        total_bricks = 0
        difference = []

        #calculate the differences and store them in a list so that we could use them later
        for index in range(1,len(heights)):
            difference.append(heights[index] - heights[index-1])
        
        #iterate through the differences
        for index, diff in enumerate(difference):
            #if the difference is negative then we don't want ladder or bricks
            if diff <= 0:
                continue
            
            #add the current difference to the total bricks we have used so far
            total_bricks += diff

             #push the amount of steps into our heap but we want max heap so change the sign
            heappush(used_bricks, -diff)

            #if we don't have any ladders or bricks left then return the current index
            if ladder == ladders and total_bricks > bricks:
                return index
            elif total_bricks > bricks: #if we still have ladders left take the bigger step and update the total bricks
                val = -heappop(used_bricks)
                total_bricks -= val
                ladder += 1
        
        #if we have reached the end return the last index
        return len(heights)-1
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n)
