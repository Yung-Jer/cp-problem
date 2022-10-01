class Solution:
    def numDecodings(self, s: str) -> int:
        _seen = {}
        n = len(s)
        
        def dp(i):
            if i == n:
                return 1
            elif s[i] == '0':
                return 0
            elif i in _seen:
                return _seen[i]
            res = dp(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                res += dp(i+2)
            _seen[i] = res
            return res
        return dp(0)