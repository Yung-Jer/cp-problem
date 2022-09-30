import heapq
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        buildings = sorted([(start, -height, end) for start, end, height in buildings] + [(end, 0, 0) for _, end, _ in buildings])
        
        heap = [(0, float('inf'))] # (-height, end)
        res = [[0,0]] # [x, height]
        for start, negH, end in buildings:
            while heap[0][1] <= start:
                heapq.heappop(heap)
            if negH:
                heapq.heappush(heap, (negH, end))
            if res[-1][1] != -heap[0][0]:
                res.append([start, -heap[0][0]])
                
            
        return res[1:]