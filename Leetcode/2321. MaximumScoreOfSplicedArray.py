# Kadane Algorithm: Find the subarray with the largest sum

class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        sum1 = sum2 = 0
        local1 = local2 = max1 = max2 = 0
        
        for i in range(n):
            a, b = nums1[i], nums2[i]
            sum1 += a
            sum2 += b
            
            local1 = max(local1, 0) + b - a
            local2 = max(local2, 0) + a - b
            max1 = max(max1, local1)
            max2 = max(max2, local2)
            
        return max(max1 + sum1, max2 + sum2)