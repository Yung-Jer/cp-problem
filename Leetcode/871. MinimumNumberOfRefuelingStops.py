import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        stations.sort()
        stations.append([target, 0])
        
        pre_loc = 0
        heap = []
        cnt = 0
        
        
        for loc, fuel in stations:
            startFuel -= (loc - pre_loc)
            while heap and startFuel < 0:
                startFuel += (-1 * heapq.heappop(heap))
                cnt += 1
            if startFuel < 0:
                return -1
            heapq.heappush(heap, -fuel)
            pre_loc = loc
        
        return cnt