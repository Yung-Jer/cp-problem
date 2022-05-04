## Need to use two pointers, which one is smol_idx, and large_idx, another one is keeping track of variable prev
## If only compare nums[i] with nums[i-1], then it will not work, because for cases like [1,3,2,2,2], the logic does not work

class Solution(object):
    def findUnsortedSubarray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """

            if len(nums) < 2:
                return 0

            smol_idx = len(nums)-1
            large_idx = 0

            prev = nums[0]
            for i in range(0,len(nums)):
                if nums[i] < prev:
                    large_idx = i
                else:
                    prev = nums[i]

            prev = nums[-1]
            for j in range(len(nums)-1, -1, -1):
                if prev < nums[j]:
                    smol_idx = j
                else:
                    prev = nums[j]
            return large_idx - smol_idx + 1 if large_idx != 0 else 0