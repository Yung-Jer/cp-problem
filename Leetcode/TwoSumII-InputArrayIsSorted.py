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