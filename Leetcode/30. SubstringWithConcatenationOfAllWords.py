class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        _seen = {}
        for i in words:
            _seen[i] = 1 if i not in _seen else _seen[i] + 1
        print(_seen)
        m = len(words)
        n = len(words[0])
        res = []
        
        for i in range(0, len(s) - m*n + 1):
            curr = {}
            for j in range(i, i + m*n, n):
                temp = s[j:j+n]
                curr[temp] = 1 if temp not in curr else curr[temp] + 1
            if _seen == curr:
                res.append(i)
        return res
            