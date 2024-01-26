class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        max_width,i =0,0
        points.sort() #sorting the input so that no point is between two points
        while i<n-1:
            width = points[i+1][0]-points[i][0]
            max_width = max(max_width,width) #finding maximum width
            i+=1
        return max_width