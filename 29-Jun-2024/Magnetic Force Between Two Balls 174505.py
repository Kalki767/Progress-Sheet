# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        '''Approach: Binary Search. The problem asks to maximize the minimum
        force between two balls. To make the problem more clear if there are
        m balls then there would be m-1 forces between them so our task is
        when we find the minimum between the forces we need to maximize that
        value as much as we can. For this problem how about if we approach
        the problem by deciding the least magnetic force between two balls
        and check if we can succesfully place all the balls in the given
        positions. We are saying the least magnetic force because the magnetic
        force between the two can be greater that wouldn't affect our result
        because we are simply trying to maximize the minimum. So how do we
        know where to put the next ball we can simply add the force on the
        current position and try to find that position in our position list.
        If we try the naive way of finding the next position it would take
        much more time complexity. Therefore we can use binary search to find
        the next index of the next position. But we have one pre condition
        to perform binary search we first need to sort the given input. So
        once we check if we could succesfully place all the balls by the
        given magnetic force we increment our force and check again. But
        this process is also time inefficient so we perform binary search
        on the output. '''

        #sort the input 
        position.sort()

        #define function to check if we can place all the balls succesfully given the least strength
        def check(force):

            balls = m - 1 #one ball will always be placed in the first position nomatter what
            index = 0

            while balls > 0: #iterate until we have nomore balls to place
                next_position = position[index] + force #calculate the next position

                next_index = bisect_left(position,next_position) #find the index of that position by using binary search
                if next_index == len(position): #if the index results in outof bound while we have balls to place we simply return False 
                    return False

                index = next_index #The next index to start would be what we found previously
                balls -= 1 #since we placed one ball succesfully we decrease the number of balls by one

            return True

        ''' set the left and right boundaries for performing the binary 
        search. here The right is set to the maximum beacuse at most we could
        have that value if the starting position is 0 and we have to place 
        2 balls. and the minimum would be 1 since the positions are distinct.'''
        left, right = 1,max(position)
        answer = 1

        #perform binary search
        while left <= right:
            mid = left + (right-left)//2
            if check(mid): #if this function return true update the answer and the left
                left = mid + 1
                answer = max(answer,mid)
            else:
                right = mid - 1

        return answer

        #Time Complexity: O(nlogn)
        #Space Complexity: O(1) #if we don't consider the stack space if we consider the stack space O(n)