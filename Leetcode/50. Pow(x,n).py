class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        res = 1
        while n:
            if n & 1 == 0:
                x *= x
                n = n >> 1
            else:
                res *= x
                n -= 1
        return res