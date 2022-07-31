class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self._sum = sum(nums)
        

    def update(self, index: int, val: int) -> None:
        a = self.nums[index]
        self.nums[index] = val
        self._sum += (val - a)
        

    def sumRange(self, left: int, right: int) -> int:
        return self._sum - sum(self.nums[:left]) - sum(self.nums[right+1:])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)