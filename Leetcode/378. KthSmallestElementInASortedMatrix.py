import functools
import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        matrix = functools.reduce(lambda a, b: a + b, matrix)
        heap = []
        for i in matrix:
            if len(heap) < k:
                heapq.heappush(heap, -i)
            else:
                heapq.heappushpop(heap, -i)
        return -heap[0]