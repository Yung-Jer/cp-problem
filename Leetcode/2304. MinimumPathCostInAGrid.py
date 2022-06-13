class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dct = {}
        
        def traverse(row, col):
            if row == m - 1:
                return grid[row][col]
            elif (row, col) in dct:
                return dct[(row, col)]
            else:
                ans = 1000000000000
                for i in range(n):
                    ans = min(ans, grid[row][col] + moveCost[grid[row][col]][i] + traverse(row+1, i))
                dct[(row, col)] = ans
                return ans
            
        return min(traverse(0, j) for j in range(n))