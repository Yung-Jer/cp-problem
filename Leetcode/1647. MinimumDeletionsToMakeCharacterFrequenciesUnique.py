import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        dct = collections.defaultdict(int)
        for c in s:
            dct[c] += 1
            
        arr = sorted(dct.values(), reverse = True)
        print(arr)
        curr_freq = len(s)
        dlt = 0
        
        for freq in arr:
            curr_freq = min(curr_freq, freq)
            dlt += (freq - curr_freq)
            
            if curr_freq > 0:
                curr_freq -= 1
        return dlt