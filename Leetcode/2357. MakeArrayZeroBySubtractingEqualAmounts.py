class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        a = set([0])
        nums = set(nums)
        
        return len(nums - a)