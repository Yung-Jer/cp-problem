class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        visited = [[0] * n for _ in range(m)]
        
        def dfs(i, j):
            if i >= 0 and j >= 0 and i < m and j < n and grid[i][j] == "1" and not visited[i][j]:
                dir = [(0, 1), (1,0), (0, -1), (-1, 0)]
                visited[i][j] = 1
                for dx, dy in dir:
                    dfs(i + dx, j + dy)
                    
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    res += 1
        return res