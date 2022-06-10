import bisect

class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        cnt = 0
        idx = 0
        while idx < len(nums):
            print(idx)
            new_idx = bisect.bisect_right(nums, nums[idx] + k)
            cnt += 1
            idx = new_idx
        return cnt