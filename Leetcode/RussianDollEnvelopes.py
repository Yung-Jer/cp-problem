import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        arr = [i[1] for i in envelopes]
        
        res = []
        res.append(arr[0])
        
        for i in range(1, len(arr)):
            if arr[i] > res[-1]:
                res.append(arr[i])
            else:
                idx = bisect.bisect_left(res, arr[i])
                res[idx] = arr[i]
                
        return len(res)