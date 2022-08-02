import bisect

class Solution:
    def countExcellentPairs(self, nums: list[int], k: int) -> int:
        nums = list(set(nums))
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i].bit_count()
        nums.sort()
        res = 0
        for i in nums:
            idx = bisect.bisect_left(nums, k - i)
            res += (n - idx)
        return res