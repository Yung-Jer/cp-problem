class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        window_sum = 0
        left = 0
        right = 0
        n = len(nums)
        
        while right < n:
            window_sum += nums[right]
            
            # Remove all subarrays with scores larger or equal to k
            while left <= right and window_sum * (right - left + 1) >= k:
                window_sum -= nums[left]
                left += 1 
            # If there is one element >= k, then skip this, restart with left = right
            if left > right:
                right = left
                continue
            # if (i,j) subarray's score is smaller than k, then th subarrays of (i,j) subarray is also not valid
            ans += right - left + 1
            right += 1
            
        return ans

# Credit to Leetcode user: https://leetcode.com/Bakerston/
# Refer from: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/discuss/2138959/Python-Explanation-with-pictures-sliding-window
            