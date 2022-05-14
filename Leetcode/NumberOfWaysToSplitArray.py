class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        curr_sum = 0
        cnt = 0
        for i in range(len(nums)-1):
            curr_sum += nums[i]
            total_sum -= nums[i]
            if curr_sum >= total_sum:
                cnt+=1
                
        return cnt