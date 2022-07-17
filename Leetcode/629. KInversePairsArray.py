class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        _seen = {}
        
        def dp(n, k):
            if (n, k) in _seen:
                return _seen[(n, k)]
            elif k == 0:
                return 1
            elif n <= 0 or k < 0:
                return 0
            else:
                _seen[(n, k)] = dp(n-1, k) + dp(n, k-1) - dp(n-1, k-n)
                return _seen[(n, k)]
            
        return dp(n, k) % (10**9 + 7)