import itertools

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        n = len(cookies)
        ans = 1000000000
        _seen = set()
        
        for combi in list(itertools.permutations(cookies)):
            child = [0] * k
            i = 0
            for ele in combi:
                child[i] += ele
                i = (i + 1) % k
            temp = tuple(child)
            if temp in _seen:
                continue
            else:
                _seen.add(temp)
                ans = min(ans, max(child))
                
        return ans