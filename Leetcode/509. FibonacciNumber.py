class Solution:
    def fib(self, n: int) -> int:
        _seen = {0: 0, 1: 1}
        
        def helper(n):
            if n in _seen:
                return _seen[n]
            else:
                _seen[n] = helper(n-1) + helper(n-2)
                return _seen[n]
        
        return helper(n)