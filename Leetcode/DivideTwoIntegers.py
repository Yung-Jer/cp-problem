class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_positive = (dividend > 0) == (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while dividend >= divisor:
            temp, rounds = divisor, 1
            while dividend >= temp:
                dividend -= temp
                ans += rounds
                temp = temp<< 1
                rounds = rounds << 1
        if not is_positive:
            ans = -ans
        return min(max(-2**31, ans), 2**31-1)