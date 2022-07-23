from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        temp = SortedList() # BST
        
        for i in range(n-1, -1, -1):
            temp.add(nums[i])
            res[i] = temp.index(nums[i])

        # Same result produced by the following code:
        # for i in range(n-1, -1, -1):
        #     res[i] = temp.bisect_left(nums[i])
        #     temp.add(nums[i])
            
        return res