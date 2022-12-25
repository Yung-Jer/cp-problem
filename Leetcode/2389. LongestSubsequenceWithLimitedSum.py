from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        arr = [0]
        n = len(nums)
        m = len(queries)
        ans = []
        nums.sort()

        for i in range(n):
            arr.append(arr[-1] + nums[i])

        for i in range(m):
            idx = bisect_right(arr, queries[i])
            ans.append(idx-1)
        return ans
