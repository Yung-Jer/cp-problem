class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        _seen = set(nums)
        res = 0
        
        for i in nums:
            if i - 1 in _seen:
                continue
            curr_length = 1
            while i + 1 in _seen:
                curr_length += 1
                i += 1
            res = max(res, curr_length)
        
        return res