class Solution:
    def findErrorNums(self, nums: "list[int]") -> "list[int]":
        _seen = set()
        temp = 0
        for i, num in enumerate(nums):
            if num in _seen:
                rep = num
            else:
                temp ^= num
            temp ^= (i+1)
            _seen.add(num)
        
        return [rep, temp]