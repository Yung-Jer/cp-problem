class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def mapping(a, b):
            if len(a) != len(b):
                return False
            n = len(a)
            map1, map2 = {}, {}
            for i in range(n):
                map1[a[i]] = b[i]
                map2[b[i]] = a[i]
            for i in range(n):
                if map1[a[i]] != b[i] or map2[b[i]] != a[i]:
                    return False
            return True

        return [w for w in words if mapping(w, pattern)]
                