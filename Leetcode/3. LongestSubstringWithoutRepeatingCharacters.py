import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = collections.defaultdict(int)
        left = 0
        max_len = 0
        n = len(s)
        
        for right in range(n):
            count[s[right]] += 1
            if count[s[right]] > 1:
                while left < right and count[s[right]] > 1:
                    count[s[left]] -= 1
                    left += 1
            max_len = max(max_len, right-left+1)
        return max_len