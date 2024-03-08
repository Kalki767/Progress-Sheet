class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        '''Approach: Binary Search and Sorting. The problem asks to find the
        right interval of each interval. The right meaning on the right side
        so for an interval to be on the right side the starting point of
        that interval should atleast be greater than or equal to the end of 
        the current interval. Therefore using the fact that the starting points
        are unique we can hold the indexes of each starting points for future
        reference. Then we can store the starting points in a list sort them
        and then try to find for each end the bisect left of it which would be
        return either the position of itself or the position of where it should
        be inserted so if the result from the bisect left is equal to the length 
        of interval then we couldn't get an interval and we would simply append
        -1 other wise we would append the index in our dictionary.'''
        index_of_start = {}
        starting_points = []
        answer = []

        #Storing the indexes and the start points
        for index in range(len(intervals)):
            start_point = intervals[index][0]
            index_of_start[start_point] = index
            starting_points.append(start_point)

        starting_points.sort()

        #for finding the right interval
        for start, end in intervals:
            right = bisect_left(starting_points,end)
            if right == len(starting_points):
                answer.append(-1)
            else:
                point = starting_points[right]
                answer.append(index_of_start[point])

        return answer
        #Time Complexity: O(nlogn)
        #Space Complexity: O(n)