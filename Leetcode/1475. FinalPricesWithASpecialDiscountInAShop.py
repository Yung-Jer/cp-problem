class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = prices[:]
        for i in range(len(prices)-1,-1,-1):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    res[i] -= prices[j]
                    break
        return res