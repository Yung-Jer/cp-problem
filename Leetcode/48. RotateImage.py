class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = list(map(list, map(reversed, zip(*matrix))))
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                matrix[i][j] = temp[i][j]