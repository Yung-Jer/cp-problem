
# the largest height diff we will use ladders, the others we will just use brick
# use minheap, once the heap size goes beyond ladders' number, we just heappop to ensure get 
# the smallest height diff, bricks -= diff

import heapq

class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        pq = []
        n = len(heights)
        
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(pq, diff)
            if len(pq) > ladders:
                bricks -= heapq.heappop(pq)
            if bricks < 0:
                return i - 1
        return n - 1