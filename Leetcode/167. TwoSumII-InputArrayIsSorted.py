# Since it is confirmed that there is exactly one solution, hence we do not need to return a base case of []
import bisect

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i in range(n):
            a = numbers[i]
            b = target - a
            idx = bisect.bisect_left(numbers, b, lo=i+1, hi=n)
            
            if idx < n and a + numbers[idx] == target:
                return [i+1, idx+1]

class Solution2:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total < target:
                l += 1
            else:
                r -= 1