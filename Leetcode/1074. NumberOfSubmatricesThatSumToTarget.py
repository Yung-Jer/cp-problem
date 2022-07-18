import collections

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        m , n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
                
        res = 0
        for l in range(n):
            for r in range(l, n):
                d = collections.defaultdict(int)
                _sum = 0
                d[0] = 1
                
                for i in range(m):
                    _sum += matrix[i][r]
                    if l:
                        _sum -= matrix[i][l-1]
                    res += d[_sum-target]
                    d[_sum] += 1
        return res