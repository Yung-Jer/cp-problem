class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0,0)
        dct = set()
        
        for i in range(len(s)):
            dct.add((i,i))
        
        for end in range(len(s)):
            start = end
            
            while start >= 0:
                if s[start] == s[end]:
                    if (end-start == 1) or (end-start > 1 and (start+1, end-1) in dct):
                        dct.add((start, end))
                        
                        if (end-start > res[1]-res[0]):
                            res = (start, end)
                start -= 1
                
        return s[res[0]:res[1]+1]