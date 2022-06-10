class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m  = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dct = {}
        dct[(m-1, n-1)] = 1
        
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        
        def dfs(x, y):
            if (x, y) in dct:
                return dct[(x, y)]
            elif (x, y) == (m-1, n-1):
                return dct[(x, y)]
            elif x >= m or y >= n or obstacleGrid[x][y] == 1:
                dct[(x, y)] = 0
                return dct[(x, y)]
            else:
                dct[(x, y)] = dfs(x+1, y)+dfs(x, y+1)
                return dct[(x, y)]
        return dfs(0, 0)