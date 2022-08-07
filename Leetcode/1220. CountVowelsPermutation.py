class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp[j] means the number of strings with length of 1 initially that end with j-th vowel
        dp = [1] * 5
        
        for _ in range(n-1):
            temp = [0] * 5
            for j in range(5):
                if j == 0: 
                    temp[0] = dp[1] + dp[2] + dp[4]
                elif j == 1:
                    temp[1] = dp[0] + dp[2]
                elif j == 2:
                    temp[2] = dp[1] + dp[3]
                elif j == 3:
                    temp[3] = dp[2]
                else:
                    temp[4] = dp[2] + dp[3]
            dp = temp
        
        return sum(dp) % (10**9 + 7)