import bisect
class Solution:
    def intToRoman(self, num: int) -> str:
        lst = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (50, "L"), (90, "XC"), (100, "C"), (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")]
        
        res = ''
        temp = num
        while True:
            if temp == 1:
                res += 'I'
                break
            idx = bisect.bisect_left(lst, (temp, "#"))
            if idx < len(lst) and temp == lst[idx][0]:
                res += lst[idx][1]
                break
            res += lst[idx-1][1]
            temp -= lst[idx-1][0]
        return res
            