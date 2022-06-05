class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        n, m = len(nums), len(operations)
        dct = {}
        
        for i in range(n):
            if nums[i] not in dct:
                dct[nums[i]] = i

        for i in range(m):

            val = dct.pop(operations[i][0])
            dct[operations[i][1]] = val
            
        inv_map = {v: k for k, v in dct.items()}
        new_nums = []
        for i in range(n):
            new_nums.append(inv_map[i])
        return new_nums