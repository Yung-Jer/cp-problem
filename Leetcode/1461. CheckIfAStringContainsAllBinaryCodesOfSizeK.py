class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        dct = set()
        for i in range(len(s) - k + 1):
            if s[i:i+k] not in dct:
                dct.add(s[i:i+k])
        return len(dct) == 2**k