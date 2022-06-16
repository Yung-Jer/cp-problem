# Method 1: DP with O(N) memory
# Run slower than method 2 because checking every index is expensive

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

# Method 2: Expanding from the middle with O(1) memory
# Run faster than method 1 because we do not need to check every index
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def helper(left, right):
            
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
            
        return max([max(helper(i,i), helper(i,i+1), key = len) for i in range(n)], key = len)