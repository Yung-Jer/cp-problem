class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        
        dp = [10000000000] * (n+1)
        dp[0], dp[1] = 0, 0
        
        for i in range(2, n+1):
            dp[i] = min(dp[i], dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]