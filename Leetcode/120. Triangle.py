class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dct = {}
        n = len(triangle)
        
        def traverse(row, idx):
            if row >= n or idx > row:
                return 0
            elif (row, idx) in dct:
                return dct[(row, idx)]
            else:
                dct[(row,idx)] = triangle[row][idx] + min(traverse(row+1,idx), traverse(row+1,idx+1))
                return dct[(row,idx)]
        return traverse(0,0)