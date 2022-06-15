import collections

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        _seen = collections.defaultdict(int)
        words.sort(key = len)
        
        for word in words:
            _seen[word] = max( _seen[ word[:i] + word[i+1:] ] + 1 for i in range(len(word)) )
            
        return max(_seen.values())