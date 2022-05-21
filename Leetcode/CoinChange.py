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