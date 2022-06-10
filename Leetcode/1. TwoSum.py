class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        count = {}
        for i, a in enumerate(nums):
            b = target - a
            if b in count:
                return [count[b], i]
            else:
                count[a] = i