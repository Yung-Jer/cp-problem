class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target > k * n:
            return 0
        _seen = {}
        
        def dp(num_dice, target):
            if num_dice == 0 and target == 0:
                return 1
            elif num_dice == 0:
                return 0
            elif (num_dice, target) in _seen:
                return _seen[(num_dice, target)]
            res = 0
            for i in range(1, k+1):
                res += dp(num_dice - 1, target - i)
            _seen[(num_dice, target)] = res
            return res
        
        return dp(n, target) % (10**9 + 7)