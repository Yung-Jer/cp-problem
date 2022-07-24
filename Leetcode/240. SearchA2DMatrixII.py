# Method 1: Binary Search O(mlogn)

import bisect
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        first_col = [i[0] for i in matrix]
        row_idx = bisect.bisect_left(first_col, target)
        
        if row_idx < m and matrix[row_idx][0] == target:
            return True
        for i in range(row_idx):
            row = matrix[i]
            col_idx = bisect.bisect_left(row, target)
            if col_idx == n:
                continue
            if matrix[i][col_idx] == target:
                return True
        return False

# Method 2: Going up or right O(m+n)
class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        i = m-1
        j = 0
        
        while i >= 0 and j < n:
            ele = matrix[i][j]
            if ele == target:
                return True
            elif ele < target:
                j += 1
            else:
                i -= 1
        return False