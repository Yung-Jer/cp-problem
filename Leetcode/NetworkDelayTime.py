# Find the single shortest path from a given source
import collections
import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        d = collections.defaultdict(list)
        for u, v, w in times:
            d[u].append((v,w))
            
        pq = []
        pq.append((0, k))
        visited = set()
        # Instead of storing the list of distance from source to each node (D), we just want to take the max cost after traversing
        # the graph WITHOUT negative weighted edges.
        max_cost = 0

        while pq:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            max_cost = max(cost, max_cost)
            
            for pair in d[node]:
                neighbour, weight = pair
                if neighbour not in visited:
                    new_cost = cost + weight
                    heapq.heappush(pq, (new_cost, neighbour))
                    
        
        return max_cost if len(visited) == n else -1