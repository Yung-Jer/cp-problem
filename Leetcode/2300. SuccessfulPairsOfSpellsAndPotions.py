import bisect

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        dct = {}
        ans = []
        
        for i in spells:
            if i in dct:
                ans.append(dct[i])
            else:
                least = success / i
                idx = bisect.bisect_left(potions, least)
                ans.append(m-idx)
                dct[i] = m-idx
        return ans