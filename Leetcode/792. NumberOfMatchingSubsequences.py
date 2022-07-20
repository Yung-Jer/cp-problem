import collections
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        d = collections.defaultdict(list)
        
        for i, char in enumerate(list(s)):
			#save the corresponding index for each character in 's'
            d[char].append(i)
        
        res = 0
        for word in words:
            idx = -1 # dummy index
            cnt = 0 # this is to check whether all the characters in word are processed
            for char in word:
                if char not in d:
                    break
				# find the index of the current char which is slightly greater than the previous index
                inst_idx = bisect.bisect_right(d[char], idx)
				# if the previous index is larger than all the indices of the current char
                if inst_idx >= len(d[char]):
                    break
                else:
                    cnt += 1
					# update the previous index to the current index
                    idx = d[char][inst_idx]
			# if all the characters in the word is being processed, then it is a subsequence of the string 's'
            if cnt == len(word):
                res += 1
        return res