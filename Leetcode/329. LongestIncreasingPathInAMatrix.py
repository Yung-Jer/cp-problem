class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        longest_ans = 0
        dct = {}
        m = len(matrix)
        n = len(matrix[0])
        
        def findpath(x, y):
            # if write 'if (x, y) in dct.keys()' it will spend O(N) time in Python 2 because of constructing a list of keys,
            # or a larger constant in Python 3 because of generating a view of dictionary key view
            if (x, y) in dct:
                return dct[(x, y)]
            
            # new starting point
            maxlength = 1
            num = matrix[x][y]
            
            # traversing
            for i, j in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[x][y]:
                    # current (1) + neighbour's depth (findpath(i, j))
                    maxlength = max(maxlength, findpath(i, j) + 1)
            
            dct[(x, y)] = maxlength
            return maxlength
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest_ans = max(longest_ans, findpath(i, j))
                
        return longest_ans