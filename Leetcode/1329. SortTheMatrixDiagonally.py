class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if m == 1 or n == 1:
            return mat
        s = m - 1
        while s >= 0:
            row, col = s, 0
            temp = []
            while row < m and col < n:
                temp.append(mat[row][col])
                row += 1
                col += 1
            temp.sort()
            row -= 1
            col -= 1
            while row >= 0 and col >= 0:
                mat[row][col] = temp.pop()
                row -= 1
                col -= 1
            s -= 1
        
        t = 1
        while t < n:
            row, col = 0, t
            temp = []
            while row < m and col < n:
                temp.append(mat[row][col])
                row += 1
                col += 1
            temp.sort()
            row -= 1
            col -= 1
            while row >= 0 and col >= 0:
                mat[row][col] = temp.pop()
                row -= 1
                col -= 1
            t += 1
        return mat
                