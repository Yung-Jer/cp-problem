import collections

class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        ans = 0
        
        dct = collections.defaultdict(set)
        for idea in ideas:
            tail = idea[1:]
            dct[idea[0]].add(tail)
        
        for i in dct.keys():
            for j in dct.keys():
                if i != j:
                    a = len(dct[i]-dct[j])
                    b = len(dct[j]-dct[i])
                    ans += a*b
        return ans