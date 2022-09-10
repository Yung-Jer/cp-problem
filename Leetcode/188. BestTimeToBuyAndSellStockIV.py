class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        _seen = {}
        n = len(prices) - 1
        
        def dp(i, can_buy, num_transac):
            if i > n or num_transac == 0:
                return 0
            elif (i, can_buy, num_transac) in _seen:
                return _seen[(i, can_buy, num_transac)]
            a,b,c,d = 0,0,0,0
            if can_buy:
                a = -prices[i] + dp(i+1, False, num_transac)
                b = dp(i+1, can_buy, num_transac)
            else:
                c = prices[i] + dp(i+1, True, num_transac-1)
                d = dp(i+1, can_buy, num_transac)
            _seen[(i, can_buy, num_transac)] = max(a,b,c,d)
            return _seen[(i, can_buy, num_transac)]
        
        return dp(0, True, k)