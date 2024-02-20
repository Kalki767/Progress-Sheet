class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        '''Approach: Greedy. the problem asked to find the maximum amount
        of height that we could change without changing the contour view
        in each side. contour view is a view that results when u are in
        a certain directions like east or north there are things that u can
        view more than the others which has the largest height. so the
        contour at index i in any direction is the maximum height across
        that view. so here first we find the contours we don't need to find
        four of them we can just find two because the others will be the
        reverse of those. the problem states we can add as much as we like
        but we have a constraint we can't surpass the contour at that index
        so since we have two contours to compare with and we don't want to
        surpass none of them we take the minimum difference from those two
        and add it to total. here we are being greedy on the amount we can
        add while considering the constraints'''
        n = len(grid)
        total = 0
        south = [0] * n
        west = [0] * n

        '''Step1: find the contours. we can do that by taking the maximum
        of the rows for south and the maximum of columns for west'''
        for index in range(n):
            south[index] = max(grid[index])
        for index in range(n):
            columns = [grid[rows][index] for rows in range(n)]
            west[index] = max(columns)

        '''Step2:iterate through the grid to know how much we can add before
        surpassing the contour. the west only changes with changing row and
        the south changes with column'''
        for rows in range(n):
            for cols in range(n):
                value = grid[rows][cols]
                total += min(west[rows] - value, south[cols] - value)
        return total
        #Time Complexity: O(n**2)
        #Space Complexity: O(n)