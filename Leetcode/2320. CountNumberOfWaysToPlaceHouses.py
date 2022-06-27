class Solution:
    def countHousePlacements(self, n: int) -> int:
        _seen = {}
        def fib(m):
            if m in _seen:
                return _seen[m]
            elif m == 1:
                _seen[m] = 2
                return 2
            elif m == 2:
                _seen[m] = 3
                return 3
            else:
                _seen[m] = fib(m-1) + fib(m-2)
                return _seen[m]
        return (fib(n))**2 % (10**9 + 7)