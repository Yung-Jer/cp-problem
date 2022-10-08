class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n-2):
            sec = i+1
            thi = n-1
            remain = target - nums[i]          
            while sec < thi:
                _sum = nums[sec] + nums[thi]
                if abs(remain - _sum) < abs(target - res_sum):
                    res_sum = _sum + nums[i]
                if _sum == remain:
                    return target
                elif _sum < remain:
                    sec += 1
                else:
                    thi -= 1

                    
        return res_sum