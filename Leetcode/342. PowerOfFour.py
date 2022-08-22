import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return math.log(n, 4).is_integer() if n > 0 else False