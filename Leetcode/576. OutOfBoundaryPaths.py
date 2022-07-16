class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        _seen = {}
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def dp(x, y, move):
            if (x, y, move) in _seen:
                return _seen[(x, y, move)]
            elif x < 0 or y < 0 or x >= m or y >= n:
                return 1
            elif move == 0:
                return 0
            else:
                res = 0
                for i, j in direction:
                    res += dp(x+i, y+j, move-1)
                _seen[(x, y, move)] = res
                return res
        
        return dp(startRow, startColumn, maxMove) % (10**9 + 7)