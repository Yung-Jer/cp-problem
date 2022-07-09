import heapq

class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        heap = []
        score = 0
        
        for i in range(n):
            maxscore = 0
            if heap:
                maxscore, idx = heap[0]
                while idx + k < i:
                    maxscore, idx = heapq.heappop(heap)
                heapq.heappush(heap, (maxscore, idx))
            score = nums[i] + -1 * maxscore
            heapq.heappush(heap, (-score, i))
        return score