class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        suffix = sorted([w[::-1] for w in words], reverse = True)
        # ["time", "me", "bell"] => ["lleb", "emit", "em"]
        res = 0
        n = len(words)
        res += len(suffix[0]) + 1
        
        for i in range(1, n):
            if not suffix[i-1].startswith(suffix[i]):
                res += len(suffix[i]) + 1
        return res
            