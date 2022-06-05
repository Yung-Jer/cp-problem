class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        def helper(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            else:
                new_nums = []
                for i in range(n//2):
                    if i & 1 == 0:
                        new_nums.append(min(nums[2 * i], nums[2 * i + 1]))
                    else:
                        new_nums.append(max(nums[2 * i], nums[2 * i + 1]))

                return helper(new_nums)
        
        return helper(nums)