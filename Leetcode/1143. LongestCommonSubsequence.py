def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        _seen = {}
        n, m = len(text1), len(text2)
        
        def dp(i, j):
            if i == n or j == m:
                return 0
            elif (i, j) in _seen:
                return _seen[(i, j)]
            if text1[i] == text2[j]:
                res = 1 + dp(i+1, j+1)
            else:
                res = max(dp(i+1, j), dp(i, j+1))
            _seen[(i, j)] = res
            return res
        
        return dp(0, 0)