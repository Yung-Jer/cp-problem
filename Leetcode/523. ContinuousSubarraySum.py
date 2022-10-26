class Solution:
    def checkSubarraySum(self, nums: "list[int]", k: int) -> bool:
        _seen = {0: -1}
        curr_sum = 0
        
        for idx, val in enumerate(nums):
            if k != 0:
                curr_sum = (curr_sum + val) % k
            else:
                curr_sum += val
            if curr_sum not in _seen:
                _seen[curr_sum] = idx
            else:
                if idx - _seen[curr_sum] >= 2:
                    return True
        return False