from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        return "".join(sorted(s, key = lambda x: (-cnt[x], -ord(x))))