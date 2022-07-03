# Method 1: Using Naive comparing method

class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        res = 1
        flag = True
        for i in range(1, len(nums)):
            if flag:
                if nums[i] != nums[i-1]:
                    sign = 1 if nums[i] > nums[i-1] else -1
                    flag = False
                    res += 1
            else:
                if sign == 1 and nums[i] < nums[i-1]:
                    res += 1
                    sign *= -1
                elif sign == -1 and nums[i] > nums[i-1]:
                    res += 1
                    sign *= -1
        return res if len(nums) > 1 else 1

# Method 2: Using alternating update statement
class Solution2:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        peak = 1
        deep = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                peak = deep + 1
            elif nums[i] < nums[i-1]:
                deep = peak + 1
        return min(len(nums), max(peak, deep))