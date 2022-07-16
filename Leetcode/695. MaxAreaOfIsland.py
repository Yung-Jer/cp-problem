class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        w = len(grid)
        l = len(grid[0])
        area = 0
        
        visited = [[0] * l for i in range(w)]
        
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(x,y):
            if x < 0 or y < 0 or x >= w or y >= l:
                return 0
            elif not grid[x][y]:
                return 0
            elif grid[x][y] and visited[x][y]:
                return 0
            else:
                visited[x][y] = 1
                return 1 + sum([dfs(x + i, y + j) for i, j in direction])
            
        for i in range(w):
            for j in range(l):
                area = max(area, dfs(i,j))
        
        return area