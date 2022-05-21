# Top Down DP (Memoization)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dct = {}
        
        def change(curr_amount):
            if curr_amount in dct:
                return dct[curr_amount]
            elif curr_amount == 0:
                return 0
            elif curr_amount < 0:
                return 1000000000 # dummy
            else:
                dct[curr_amount] = min(change(curr_amount - coin) + 1 for coin in coins)
                return dct[curr_amount]

        ans = change(amount)
        return ans if ans < 1000000000 else -1

# Bottom Up DP (DP Table)
# Faster and less memory space
class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [100000000] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
                
        return dp[amount] if dp[amount] < 100000000 else -1