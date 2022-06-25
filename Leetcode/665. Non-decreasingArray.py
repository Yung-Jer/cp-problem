# first loop through the array once to get whether how many "decreases" the array has 
# decreases is defined as nums[k] < nums[k-1]
# if decreases > 1: return False

# construct diff array: if contiguous 2 elements have sum smaller than 0, 
# AND the following contiguous 2 elements have sum smaller than 0 again, 
# then return false 
# (i.e. diff[i] + diff[i+1] < 0 and diff[i+1] + diff[i+2] < 0)

class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        arr = []
        n = len(nums)
        count = 0
        
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            arr.append(diff)
            if diff < 0:
                count += 1
            if count > 1:
                return False
        
        print(arr)
        m = len(arr)
        for i in range(1, m):
            _sum = arr[i-1] + arr[i]
            if _sum < 0:
                if i < m-1 and (arr[i] + arr[i+1] < 0):
                    return False
        return True