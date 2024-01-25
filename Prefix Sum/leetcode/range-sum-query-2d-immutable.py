class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #Approach: 2D prefix_sum
        #Step1: assigning prefix_sum and updating it's value for each element in the matrix
        self.prefix_sum = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        for i in range(1,len(self.prefix_sum)):
            for j in range(1,len(self.prefix_sum[0])):
                self.prefix_sum[i][j]=self.prefix_sum[i-1][j]+self.prefix_sum[i][j-1]-self.prefix_sum[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        calculated_sum = self.prefix_sum[row2+1][col2+1]-self.prefix_sum[row1][col2+1]-self.prefix_sum[row2+1][col1]+self.prefix_sum[row1][col1]
        return calculated_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)