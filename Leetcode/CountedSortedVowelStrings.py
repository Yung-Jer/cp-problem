class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Init a dp table such that the rows are the length (n) and the columns are the number of vowels (5)
        dp = [[0] * 5 for i in range(n)]

        # Base case of dp table (when n = 1):
        for i in range(5):
            dp[0][i] = i+1

        # Iterate through the dp table and fill in the values
        for i in range(1, n):
            # For any n given, if the number of vowels is 1, then there will only be 1 possible combination, which is aaaa.....aa
            dp[i][0] = 1
            for j in range(1, 5):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n-1][4]