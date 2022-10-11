import bisect
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        k = 3
        lst = [float('inf')] * (k - 1)
        for num in nums:
            idx = bisect.bisect_left(lst, num)
            if idx == k - 1:
                return True
            lst[idx] = num
        return False