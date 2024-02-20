class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''Approach: Greedy. the problem asks to find the minimum number of
        arrows needed to burst each and every ballon. here we are being greedy
        on the number of arrows that's to minimize them. to minimize them we
        need to shot overlapping ballons with one arrow. therefore all we
        need to do is find overlapping ballons by comparing the end of the 
        first with the start of the next'''
        '''Step1: initialize arrows with zero and sort the array so that we
        could exactly know which ballon comes after which ballon'''
        points.sort()
        arrows = 0
        minimum_end = points[0][1]

        '''Step2: iterate through the points while checking if they overlap
        if they do continue if they donot increase the arrow by one and
        update the minimum end'''
        for index in range(1,len(points)):
            if points[index][0] <= minimum_end:
                minimum_end = min(minimum_end, points[index][1])
                continue
            else:
                arrows += 1
                minimum_end = points[index][1]
        return arrows + 1
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        