import heapq
import collections

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

# Method 2: DP with sliding window to find max dp value within range using deque

class Solution2:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [-10000000000] * n
        dp[0] = nums[0]
        
        q = collections.deque()
        for i in range(1, n):
            while q and dp[i-1] >= dp[q[-1]]:
                q.pop()
            q.append(i-1)
            while q[0] < i-k:
                q.popleft()
            dp[i] = dp[q[0]] + nums[i]
        return dp[-1]