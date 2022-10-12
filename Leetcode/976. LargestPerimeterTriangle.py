from collections import deque
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse = True)
        q = deque(nums)
        while len(q) >= 3 and q[0] >= q[1] + q[2]:
            q.popleft()
        return 0 if len(q) < 3 else (q[0] + q[1] + q[2])