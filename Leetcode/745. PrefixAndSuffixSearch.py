import collections

class WordFilter:

    def __init__(self, words: list[str]):
        self.pre = collections.defaultdict(set)
        self.suf = collections.defaultdict(set)
        _seen = set()
        
        for i in range(len(words)-1,-1,-1): # We want to get the largest possible index
            w = words[i]
            if w not in _seen:
                _seen.add(w)
                for j in range(len(w)+1):
                    self.pre[w[:j]].add(i)
                    self.suf[w[j:]].add(i)
                    

    def f(self, prefix: str, suffix: str) -> int:
        pre = self.pre[prefix]
        suf = self.suf[suffix]
        intersect = pre & suf
        return max(intersect) if intersect else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

# Credit to: https://leetcode.com/jae2021/
# Refer from: https://leetcode.com/problems/prefix-and-suffix-search/discuss/1557843/Python3-BF-using-hashtag-greater-Trie-using-hashtag-greater-Two-Dictionaries-with-set