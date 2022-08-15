class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        n = len(s)
        map1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        map2 = {"I": set(["V", "X"]), "X": set(["L", "C"]), "C": set(["D", "M"])}
        
        for i in range(n-1, -1, -1):
            if i < n-1 and s[i] in map2 and s[i+1] in map2[s[i]]:
                res -= map1[s[i]]
            else:
                res += map1[s[i]]
        return res