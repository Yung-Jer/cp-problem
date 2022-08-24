class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and not (1162261467 % n)