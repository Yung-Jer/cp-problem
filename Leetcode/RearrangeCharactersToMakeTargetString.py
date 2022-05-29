class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        if len(target) > len(s):
            return 0
        dct = {}
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = 1
            else:
                dct[s[i]] += 1
        
        dct2 = {}
        for i in range(len(target)):
            if target[i] not in dct2:
                dct2[target[i]] = 1
            else:
                dct2[target[i]] += 1
                
        ans = 100000000000
        for i in dct2:
            if dct.get(i, -1) == -1:
                ans = 0
                break
            ans = min(ans, dct[i] // dct2[i])
            
        return ans if ans != 100000000000 else 0