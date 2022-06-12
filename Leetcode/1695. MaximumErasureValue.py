class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        _seen = set()
        left = 0
        _sum = 0
        ans = 0
        
        
        for i in range(n):
            while nums[i] in _seen:
                _sum -= nums[left]
                _seen.remove(nums[left])
                left += 1
            _seen.add(nums[i])
            _sum += nums[i]
            ans = max(ans, _sum)
        return ans