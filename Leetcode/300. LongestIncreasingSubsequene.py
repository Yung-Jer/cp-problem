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