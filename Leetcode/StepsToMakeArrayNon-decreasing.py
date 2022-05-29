class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            cur = 0
            while stack and nums[stack[-1][0]] < nums[i]:
                idx, count = stack.pop()
                cur = max(cur+1, count)
            ans = max(ans, cur)
            stack.append([i, cur])
        return ans