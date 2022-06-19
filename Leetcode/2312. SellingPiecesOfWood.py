# Similar to DP solution for puzzle
# To cut a piece of wood, you must make a vertical or horizontal cut across the entire height or width of the piece to split it into two smaller pieces.


# Every cut makes the original piece into two smaller piece of the same length or same height.
# piece[row][col] = piece[row-k][col] + piece[k][col]
# or
# piece[row][col] = piece[row][col-k] + piece[row][k]

# Take the picture below as an example, originally every cell of dp is 0 (no price)
# Update dp table with the prices given
# dp[heigh][width] = price

# Let's see how we update dp, start by row = 1 and row = 1:

# dp[1][1] = 0
# For dp[1][2] (size of 1*2), we can either sell it directly, or cut it into two 1*1. Put the higher price in dp[1][2].
# For dp[1][3] (size of 1*3), we can either sell it directly, or cut it into 1*1 and 1*2. Put the higher price in dp[1][3].

# For dp[1][4] (size of 1*4), we can either:
# sell it directly.
# cut it into 1*1 and 1*3.
# cut it into 1*2 and 1*2.
# Put the higher price in dp[1][4].


# Update all the cells and return dp[m][n] as the best price for the whole piece of wood.

class Solution:
    def sellingWood(self, m: int, n: int, prices: list[list[int]]) -> int:
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for h,w,p in prices:
            dp[h][w] = p
        
        for row in range(1,m+1):
            for col in range(1,n+1):
                for c in range(1, col//2 + 1):
                    dp[row][col] = max(dp[row][col], dp[row][col-c] + dp[row][c])
                for r in range(1, row//2 + 1):
                    dp[row][col] = max(dp[row][col], dp[row-r][col] + dp[r][col])
                    
        return dp[m][n]

# Credit to: https://leetcode.com/Bakerston/
# Refer from: https://leetcode.com/problems/selling-pieces-of-wood/discuss/2168135/Python-Explanation-with-pictures-DP