# check if a string, s3, is a interweaving string of s1 and s2, 
# which s1 is broken down to a1,a2,a3,a4,a5, ..... and s2 is broken down to b1,b2,b3,b4,b5,..... 
# and s3 == a1,b1,a2,b2,..... or s3 == b1,a1,b2,a2,......

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        _seen = {}
        m = len(s1)
        n = len(s2)
        o = len(s3)
        
        def dp(i, j):
            if (i, j) in _seen:
                return _seen[(i, j)]
            elif i == m and j == n:
                return True
            elif i == m:
                return s2[j:] == s3[i+j:]
            elif j == n:
                return s1[i:] == s3[i+j:]
            elif s1[i] == s3[i+j] and s2[j] == s3[i+j]:
                _seen[(i,j)] = dp(i+1,j) or dp(i, j+1)
                return _seen[(i,j)]
            elif s1[i] == s3[i+j]:
                _seen[(i,j)] = dp(i+1,j)
                return _seen[(i,j)]
            elif s2[j] == s3[i+j]:
                _seen[(i,j)] = dp(i, j+1)
                return _seen[(i,j)]
            else:
                _seen[(i,j)] = False
                return False
        return dp(0, 0) if m + n == o else False