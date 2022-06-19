# Since the list of numbers generated is sure of this example: [2, 12, 22, 32, ....], hence actually we just have to find
# how many steps we need to repetitively add k until it matches the unit-digit of num.
# e.g. num = 40, k = 8 (we need 5 steps)
# e.g. num = 58, k = 9 (we need 2 steps)
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        if k > num: return -1
        
        _seen = [False] * 10
        temp = k
        count = 0
        
        while (not _seen[temp % 10]): # to avoid 0 cases or duplicate cases after 1 round
            _seen[temp % 10] = True
            count += 1
            if (num % 10 == temp % 10): #if it matches, break
                break
            temp += k
        # at his moment, temp should be the same as num, otherwise it has looped through all the possible unit-digits
        if not _seen[num % 10] or temp > num: 
            return -1
        else:
            return count