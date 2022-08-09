class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        _seen = set(arr)
        arr.sort()
        dp = dict.fromkeys(arr, 1)
        
        for i, num in enumerate(arr):
            for j in range(i):
                a = arr[j]
                b = num // a
                if num % a == 0 and b in _seen:
                    dp[num] += dp[a] * dp[b]
                    
        return sum(dp.values()) % (10**9 + 7)