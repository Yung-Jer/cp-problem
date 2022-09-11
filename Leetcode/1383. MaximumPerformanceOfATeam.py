from heapq import heappop, heappush
class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        sorted_combi = list(sorted(zip(efficiency, speed), reverse=True))
        q = []
        _sum = 0
        ans = float('-inf')
        
        for i, j in sorted_combi:
            while len(q) >= k:
                _sum -= heappop(q)
            heappush(q, j)
            _sum += j
            ans = max(ans, _sum * i)
        return ans % (10**9 + 7)