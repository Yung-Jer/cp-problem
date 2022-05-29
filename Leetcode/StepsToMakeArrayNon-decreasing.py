# Idea is to store [index, how many steps to remove all elements smaller than current element on the right]

class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            cur = 0
            while stack and nums[stack[-1][0]] < nums[i]:
                idx, count = stack.pop()
                # Since next element is also smaller than current element, we take max(1, next element's count)
                cur = max(cur+1, count) 
            ans = max(ans, cur)
            stack.append([i, cur])
        return ans