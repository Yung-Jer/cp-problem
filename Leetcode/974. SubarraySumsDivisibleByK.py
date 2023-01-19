class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        _seen = {0: 1}
        res = 0
        total = 0

        for i in nums:
            total += i
            re = total % k
            if re in _seen:
                res += _seen[re]
                _seen[re] += 1
            else:
                _seen[re] = 1
        
        return res