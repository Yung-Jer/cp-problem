# Surprisingly, same solution in Python 2 will TLE while in Python 3 will AC.

class Solution:
    def maxProduct(self, words: list[str]) -> int:
        max_val = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not set(words[i]) & set(words[j]):
                    max_val = max(max_val, len(words[i]) * len(words[j]))
        return max_val

# Bitmask Solution:'zyxwvutsrqponmlkjihgfedcba' as bit set, as 1 represents the presence of a character.
class Solution2:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        
        bitmask = [0] * n
        lengths = [0] * n
        
        for i in range(n):
            for c in words[i]:
                bitmask[i] = bitmask[i] | 1 << (ord(c) - ord('a'))
            lengths[i] = len(words[i])
            
        max_length = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (bitmask[i] & bitmask[j]):
                    max_length = max(max_length, lengths[i] * lengths[j])
        return max_length