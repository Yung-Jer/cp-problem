from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        cnt=defaultdict(lambda :[0,""])
        for i in words:
            cnt[i]=[cnt[i][0]-1,i]
        val = list(cnt.values())
        ans = heapq.nsmallest(k,val)
        res=[]
        for i in ans:
            res.append(i[1])
        return res
        