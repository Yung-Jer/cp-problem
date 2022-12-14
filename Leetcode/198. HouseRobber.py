class Solution:
    def rob(self, nums: List[int]) -> int:
        _seen = {}
        length = len(nums)

        def recur(i):
            if i >= length:
                return 0
            elif i in _seen:
                return _seen[i]
            _sum = max(recur(i+1), nums[i] + recur(i+2))
            _seen[i] = _sum
            return _sum
        
        return recur(0)