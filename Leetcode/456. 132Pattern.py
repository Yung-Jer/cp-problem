class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        stack = []
        sec_num = -10**9 - 1 # the second largest number, initialized to -10^9 - 1 such that nothing is smaller than it
        
        # Try to find nums[i] < second_num < stck[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < sec_num: # if the current number is smaller than the second largest number, return True
                return True
            else:
                # if the current number is larger than the stack[-1], pop the stack until you get the largest number smaller than the current number 
                # stack[-1] will always be the largest element
                # second number will always be the second largest number
                while stack and stack[-1] < nums[i]: 
                    sec_num = stack.pop()
                stack.append(nums[i])
        return False