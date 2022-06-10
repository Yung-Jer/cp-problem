class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])

        # Create a 2D array to store the prefix sum of each row and column
        self.prefix_sum = [[0]*(n+1) for i in range(m+1)]
        
        # Calculate the prefix sum of each row and column by doing dp[i+1][j+1] = matrix[i][j] + dp[i][j+1] + dp[i+1][j] - dp[i][j]
        for row in range(m):
            for col in range(n):
                self.prefix_sum[row+1][col+1] = matrix[row][col] + self.prefix_sum[row+1][col] + self.prefix_sum[row][col+1] - self.prefix_sum[row][col]

    # Region is defined as the prefix sum until row and column               
    # Region(Answer) = Region(row2,col2) - Region(row2, col1-1) - Region(row1-1, col2) + Region(row1-1, col1-1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row2+1][col1] - self.prefix_sum[row1][col2+1] + self.prefix_sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)