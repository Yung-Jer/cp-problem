class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        left = 0
        right = sum(nums)
        dct = {}
        ans = n+1 # dummy, larger than deleting all n numbers
        
        for i in range(n):
            left += nums[i]
            right -= nums[i]
            diff = x - right
            dct[left] = i
            
            if left == x:
                ans = min(ans, i+1)
            if right == x:
                ans = min(ans, n-i-1)
            if diff in dct:
                ans = min(ans, dct[diff] + n - i)

                
        return ans if ans != n+1 else -1