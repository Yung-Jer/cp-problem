from collections import Counter
import heapq

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        cnt = Counter(nums)
        keys = list(cnt.keys())
        heapq.heapify(keys)
        
        while keys:
            top = keys[0]
            for i in range(top, top + k):
                if i not in cnt:
                    return False
                cnt[i] -= 1
                if cnt[i] == 0:
                    heapq.heappop(keys)
        return True