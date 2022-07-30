import functools
import collections

class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        counter = functools.reduce(lambda a,b: a|b,map(collections.Counter, words2))
        res = []
        
        for word in words1:
            if collections.Counter(word) >= counter:
                res.append(word)
        
        return res