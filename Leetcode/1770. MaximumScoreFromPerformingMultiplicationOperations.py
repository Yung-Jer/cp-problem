class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n = len(nums)
        dp = [0] * (len(multipliers) + 1)
        for m in range(len(multipliers) - 1, -1, -1):
            pd = [0] * (m + 1)
            for l in range(m, -1, -1):
                pd[l] = max(dp[l + 1] + multipliers[m] * nums[l], 
                            dp[l] + multipliers[m] * nums[n - 1 - (m - l)])
            dp = pd
        return dp[0]

# class Solution: # TLE
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#         n, m = len(nums), len(multipliers)
#         _seen = {}
        
#         def dp(l, num):
#             if num == m:
#                 return 0
#             elif (l, num) in _seen:
#                 return _seen[(l, num)]
#             _seen[(l, num)] = max(nums[l] * multipliers[num] + dp(l+1, num+1), nums[n-1-(num-l)] * multipliers[num] + dp(l, num+1))
#             return _seen[(l, num)]
        
#         return dp(0, 0)