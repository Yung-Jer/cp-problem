# O(n) solution

import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for i in nums:
            idx = bisect.bisect_left(ans, i)
            if idx == len(ans):
                ans.append(i)
            else:
                ans[idx] = i
        return len(ans)

# O(n^2) solution
class Solution2:
    def lengthOfLIS(self, nums: list[int]) -> int:
        _seen = {}
        n = len(nums)
        res = [1]
        
        def dp(index):
            if index in _seen:
                return _seen[index]
            elif index == n - 1:
                return 1
            count = 1
            for i in range(index + 1, n):
                if nums[i] > nums[index]:
                    count = max(count, 1 + dp(i))
            _seen[index] = count
            res[0] = max(res[0], count)
            return count
        
        for i in range(n-1, -1, -1):
            dp(i)
            
        return res[0]