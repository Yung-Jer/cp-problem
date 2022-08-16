from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        _seen = Counter(s)
        print(_seen)
        for i in range(len(s)):
            if _seen[s[i]] == 1:
                return i
        return -1